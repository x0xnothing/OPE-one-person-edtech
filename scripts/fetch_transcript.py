#!/usr/bin/env python3
"""
Get a timestamped transcript for a YouTube lecture and normalise it to one line per cue:

    [mm:ss] text            (or [h:mm:ss] for long videos)

Usage
  python fetch_transcript.py <youtube-url-or-id> [--lang bn en] [-o transcript.txt]
  python fetch_transcript.py --from-file lecture.srt|.vtt|.txt [-o transcript.txt]

Order of attempts:
  1. youtube-transcript-api  (manual or auto captions)
  2. yt-dlp auto-subs (.vtt)
  3. give up -> ask the student to paste the transcript WITH timestamps
     (YouTube: "...more" -> "Show transcript" -> copy; or any SRT/VTT file)
"""
import argparse, re, subprocess, sys, tempfile, glob, os

ID_RE = re.compile(r"(?:v=|youtu\.be/|shorts/|embed/|live/)([A-Za-z0-9_-]{11})")


def vid_of(s):
    m = ID_RE.search(s)
    return m.group(1) if m else (s if re.fullmatch(r"[A-Za-z0-9_-]{11}", s) else None)


def fmt(sec):
    sec = int(float(sec)); h, r = divmod(sec, 3600); m, s = divmod(r, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def via_api(vid, langs):
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        return None
    try:
        api = YouTubeTranscriptApi()
        if hasattr(api, "fetch"):                       # v1.x
            tr = api.fetch(vid, languages=langs)
            return [(s.start, s.text) for s in tr]
        tr = YouTubeTranscriptApi.get_transcript(vid, languages=langs)   # v0.x
        return [(d["start"], d["text"]) for d in tr]
    except Exception as e:
        print(f"[api] {e.__class__.__name__}: {str(e)[:200]}", file=sys.stderr)
        return None


def parse_vtt_srt(text):
    cues, cur_t = [], None
    for line in text.splitlines():
        m = re.match(r"(?:(\d+):)?(\d{1,2}):(\d{2})[.,](\d{3})\s*-->", line.strip())
        if m:
            h = int(m.group(1) or 0); cur_t = h * 3600 + int(m.group(2)) * 60 + int(m.group(3)); continue
        line = re.sub(r"<[^>]+>", "", line).strip()
        if cur_t is not None and line and not line.isdigit() and line != "WEBVTT":
            if not cues or cues[-1][1] != line:
                cues.append((cur_t, line))
    return cues


def parse_plain(text):
    """Lines like '0:00 text', '[00:00] text', '1:02:03 - text' (YouTube 'Show transcript' copy)."""
    cues, pend = [], None
    for raw in text.splitlines():
        line = raw.strip()
        m = re.match(r"^\[?(?:(\d+):)?(\d{1,2}):(\d{2})\]?\s*[-–:]?\s*(.*)$", line)
        if m:
            t = int(m.group(1) or 0) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
            if m.group(4): cues.append((t, m.group(4)))
            else: pend = t
        elif line and pend is not None:
            cues.append((pend, line)); pend = None
    return cues


def via_ytdlp(vid, langs):
    with tempfile.TemporaryDirectory() as d:
        cmd = ["yt-dlp", "--skip-download", "--write-auto-subs", "--write-subs", "--sub-format", "vtt",
               "--sub-langs", ",".join(langs), "-o", os.path.join(d, "%(id)s"), f"https://www.youtube.com/watch?v={vid}"]
        try:
            subprocess.run(cmd, check=True, capture_output=True, timeout=180)
        except Exception as e:
            print(f"[yt-dlp] {str(e)[:200]}", file=sys.stderr); return None
        files = sorted(glob.glob(os.path.join(d, "*.vtt")))
        return parse_vtt_srt(open(files[0], encoding="utf-8").read()) if files else None


def merge(cues, window=6):
    """Join cues into ~6-second lines so the agent reads sentences, not fragments."""
    out = []
    for t, txt in cues:
        if out and t - out[-1][0] < window:
            out[-1] = (out[-1][0], out[-1][1] + " " + txt)
        else:
            out.append((t, txt))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video", nargs="?")
    ap.add_argument("--from-file")
    ap.add_argument("--lang", nargs="+", default=["bn", "en", "hi"])
    ap.add_argument("-o", "--out", default="transcript.txt")
    a = ap.parse_args()
    cues, vid = None, None
    if a.from_file:
        txt = open(a.from_file, encoding="utf-8").read()
        cues = parse_vtt_srt(txt) if "-->" in txt else parse_plain(txt)
    else:
        vid = vid_of(a.video or "")
        if not vid: sys.exit("could not read a YouTube video id")
        cues = via_api(vid, a.lang) or via_ytdlp(vid, a.lang)
    if not cues:
        sys.exit("NO TRANSCRIPT. Ask the student to paste it with timestamps "
                 "(YouTube → … more → Show transcript → copy all), or to upload an .srt/.vtt file.")
    with open(a.out, "w", encoding="utf-8") as f:
        if vid: f.write(f"# video_id: {vid}\n")
        for t, txt in merge(cues):
            f.write(f"[{fmt(t)}] {txt}\n")
    print(f"wrote {a.out} ({len(cues)} cues)")


if __name__ == "__main__":
    main()
