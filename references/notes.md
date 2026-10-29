# Modes: note-qr (interactive note with YouTube-timestamp QR) and note (no QR)

Target look = Bangladeshi printed guide books (user references IMG_8912–8915, 9304–9305):
chapter banner (black slanted label "দশম অধ্যায়", big Bangla title + English title, arrow box at right
holding the full-video QR or the logo) → black "Board Questions Analysis" / "Lecture Map" bar + table →
slanted title "গুরুত্বপূর্ণ সূত্রাবলি ও বিশ্লেষণ" → 2-column table (সূত্রাবলি | বিশ্লেষণ with diagrams) →
"দ্রুত মনে রাখো"/"একক রূপান্তর" double-rule box → then 2-column pages: `Type 01` header, dashed concept
box, red "ভিডিওতে বলা টিপস" box, "প্রশ্ন ▸ ১" problems, solutions with গ/ঘ black labels and a
"দেওয়া আছে," side column separated by a vertical rule, `(Ans.)` flush right.
Running header: page number + dotted leader + **Brand ▸ book title** (alternating sides), brand pill footer.

Demos: `demos/04-note-qr/` (with `input/transcript.txt`, `input/slides.md`, `input/concept-map.json`),
`demos/05-note-noqr/`.

---------------------------------------------------------------------------------------------------
## A. note-qr — pipeline

### Step 1 — collect inputs
1. YouTube link (required) → video id.
2. Transcript **with timestamps**: try `python scripts/fetch_transcript.py <url> -o transcript.txt`
   (youtube-transcript-api, then yt-dlp auto-subs). If it fails (no captions / network), ask the student:
   "ভিডিওর নিচে …more → Show transcript → সব কপি করে দাও (টাইমস্ট্যাম্পসহ)" or an .srt/.vtt file;
   normalise with `--from-file`.
3. Lecture slides (PDF/images/text) — optional but strongly preferred.

### Step 2 — analyse: build `concept-map.json` (do this before any LaTeX)
Treat the transcript as the **teaching script**; slides are the skeleton.
- Segment the lecture into **Types** (topic blocks). Signals: "এবার/এখন আমরা …", "টাইপ", "পরের টপিক",
  slide changes, long pauses, a new formula being introduced.
- For every concept/formula record the **first timestamp where it is explained** (not where it is merely named).
- For every worked math/problem record the timestamp where the teacher **starts reading the question**.
- Extract teacher-only knowledge that is NOT on the slides → tips boxes:
  cue words: "মনে রাখবা/রাখো", "লিখে রাখো", "নোট করো", "ট্রিক", "শর্টকাট", "কমন ভুল", "ভুল করে",
  "পরীক্ষায় আসে/এসেছে", "বোর্ডে", "important", "খেয়াল করো", "সাবধান", "এক্সেপশন".
- Note importance from emphasis/repetition ("বারবার এসেছে" → ★★★★★).
- Keep exact numbers from the board/whiteboard as said; if the transcript is ambiguous (ASR errors in
  numbers/units), cross-check with slides; if still unsure, solve it yourself and flag in `verify.md`.
Schema (see the demo file): `video_id, chapter, types[ {id,title,start,importance, concepts[{name,t,slide}],
tips[{t,text,not_in_slides}], maths[{t,text}] } ]`.

### Step 3 — write the note
- `\etset{ytid=<VIDEO_ID>, qrsize=1.3cm}` once; then every QR is `\ytqr{mm:ss}` (or `h:mm:ss`).
- URL produced: `https://www.youtube.com/watch?v=ID&t=<seconds>s&noapp=1` — `noapp=1` keeps it in the browser.
- Place a QR: chapter banner → `\ytqr[1.55cm]{00:00}` (full video); Lecture Map table → clickable times
  `\ytlink{04:15}{04:15}`; each formula row → `\withqr{t}{…}`; each concept box, each tip, each worked
  problem → `\withqr[1.35cm]{t}{…}`. One QR per idea — never two QRs side by side.
- QR minimum printed size 1.3 cm (≥ 1.5 cm if the note will be photocopied). Label under every QR (mm:ss).
- Use `\ytqrid{OTHERID}{mm:ss}` when a note mixes several videos.
- Lecture Map table replaces "Board Questions Analysis": columns টাইপের নাম | গুরুত্ব | ভিডিওতে | যা যা আছে | পৃষ্ঠা.

### Step 4 — verify
`scripts/build.sh note.tex` → look at every page → `python scripts/verify_qr.py note.pdf`
(each QR decodes, is clickable, has `noapp=1`, timestamps match concept-map.json).

---------------------------------------------------------------------------------------------------
## B. note (no QR)
Same layout, inputs = slides (+ transcript if given, used only for tips/explanations).
Banner right box holds `\etlogo[1.1cm]` (or stays empty). "Board Questions Analysis" table only with
real data from the user — otherwise either omit it or label **ডেমো ডেটা** (SKILL.md §3.2).

---------------------------------------------------------------------------------------------------
## Building blocks (edtech.sty)
```latex
\documentclass[10pt,twoside]{article}
\usepackage[tiro]{edtech}
\geometry{left=13mm,right=13mm,top=17mm,bottom=17mm,headsep=5mm}
\etset{brand=EduBrand, book={HSC Physics 1st Paper · Chapter-10}, chapter={আদর্শ গ্যাস …}, logo=logo.png, ytid=ID}
\pagestyle{note}
\chapterbanner{দশম অধ্যায়}{আদর্শ গ্যাস ও গ্যাসের গতিতত্ত্ব}{Ideal Gas \& Kinetic Theory of Gas}{\ytqr[1.55cm]{00:00}}
\sectionbar{Lecture Map — ভিডিও অনুযায়ী টপিক ভাগ}
\slantedtitle{গুরুত্বপূর্ণ সূত্রাবলি ও বিশ্লেষণ}
% formula table: left column >{\raggedright}p{..} (so \\ breaks lines), right column centred X with tikz
\begin{remember}[একক রূপান্তর] … \end{remember}
\typehead{01}{টাইপের নাম}
\begin{conceptbox} \withqr{17:45}{\textbf{কনসেপ্ট:} …} \begin{roundbox} • … \end{roundbox}\end{conceptbox}
\begin{tipbox} \withqr{07:50}{…} \end{tipbox}          % [কমন ভুল] as optional title
\withqr{14:05}{\prashna{১} question … \hfill[ভিডিও ম্যাথ]}
\textbf{সমাধান:}\par \partlabel{গ}
\solgiven[0.36]{working … \ans}{\textbf{দেওয়া আছে,}\\ $P_1=…$}
```
Layout rules: page 1 = banner + map + formula table (+ remember box); following pages 2 columns
(`multicols` with `\columnseprule=0.4pt`). Use `\columnbreak` to start a Type at the top of a column.
Diagrams in the analysis column: draw with TikZ at `scale≈0.55–0.7`, labels ≥ `\scriptsize`.
Page-fill rule (SKILL.md §3.9): do NOT put `\newpage` between page 1 and the Type pages — let the 2-column part start wherever page 1 ends. Long formula tables → `xltabular` with `\endhead` so they can continue on the next page instead of jumping and leaving a gap.
