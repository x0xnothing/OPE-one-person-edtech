#!/usr/bin/env python3
"""
PAGE-FILL CHECK — no page may move on to the next page while leaving a big empty area.

For every page (except the last) it measures the largest vertical white band
  * across the full page width, and
  * inside the left half and the right half separately (catches an empty column in 2/3-column layouts),
between the first content row and the footer/bottom margin.

Usage:  python check_fill.py file.pdf [--max 0.08] [--allow-pages 2,3] [--dpi 60]
  --max          largest allowed empty band as a fraction of page height (default 0.08 = 8 %)
  --allow-pages  pages where white space is part of the design: "2,3" or "all"
                 (ONLY for answer-writing space in BUET/written papers or a cover page)
Exit code 1 if any non-last page breaks the rule. The last page is reported (info) but never fails.
"""
import argparse, glob, os, subprocess, sys, tempfile
from PIL import Image


def bands(px, w, h, x0, x1, thr=235):
    """Return list of (start,end) white row-bands within columns x0..x1 (ignores ~1px rules)."""
    rows = []
    for y in range(h):
        dark = 0
        for x in range(x0, x1, 2):
            if px[x, y] < thr:
                dark += 1
                if dark > 2: break
        rows.append(dark > 2)
    content = [y for y, c in enumerate(rows) if c]
    if not content: return [], None, None
    top, bot = content[0], content[-1]
    out, run = [], None
    for y in range(top, h):
        if not rows[y]:
            run = y if run is None else run
        else:
            if run is not None: out.append((run, y)); run = None
    if run is not None: out.append((run, h))     # trailing white to the page edge
    return out, top, bot


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf"); ap.add_argument("--max", type=float, default=0.08)
    ap.add_argument("--allow-pages", default=""); ap.add_argument("--dpi", default="60")
    a = ap.parse_args()
    allow_all = a.allow_pages.strip() == "all"
    allow = set() if allow_all else {int(p) for p in a.allow_pages.split(",") if p.strip()}
    bad = 0
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(["pdftoppm", "-gray", "-r", a.dpi, a.pdf, os.path.join(d, "p")], check=True)
        files = sorted(glob.glob(os.path.join(d, "p-*.pgm")), key=lambda f: int(f.rsplit("-", 1)[1][:-4]))
        n = len(files)
        for f in files:
            pg = int(f.rsplit("-", 1)[1][:-4])
            im = Image.open(f); px = im.load(); w, h = im.size
            margin = int(0.075 * h)                     # normal bottom margin (+footer) is not "empty"
            worst, where = 0.0, ""
            for name, x0, x1 in (("page", 0, w), ("left half", 0, w // 2), ("right half", w // 2, w)):
                bl, top, bot = bands(px, w, h, x0, x1)
                for s, e in bl:
                    size = (e - s - (margin if e >= h - 1 else 0)) / h
                    if size > worst:
                        worst, where = size, f"{name}, {100*s/h:.0f}%–{100*e/h:.0f}% of page height"
            last = pg == n
            if worst > a.max and not last and pg not in allow and not allow_all:
                bad += 1; tag = "FAIL"
            else:
                tag = "info" if (last and worst > a.max) else "ok  "
            print(f"[{tag}] page {pg}/{n}: largest empty band {100*worst:4.1f}%  ({where})")
    if bad:
        print(f"\n{bad} page(s) leave empty space before the next page. Fix: make blocks breakable, "
              "move/resize figures, remove forced \\newpage/\\clearpage, or add content (see SKILL.md §3.9).")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
