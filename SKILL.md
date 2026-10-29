---
name: bangla-edtech-studio
description: >
  One-person Bangla EdTech production studio. Produces print-ready, publication-quality Bangla
  (SSC/HSC/Admission) material with XeLaTeX and teaching videos with Manim: MCQ/CQ teaching slides
  (black board, 16:9), SSC/HSC board-style MCQ & CQ question papers, model tests, BUET-style written
  papers, book-style notes with YouTube-timestamp QR codes (from lecture transcript + slides), notes
  without QR, two-column practice sheets with answers/solutions, thumbnail prompt packs for image
  models, Manim explainer videos with Bangla text, and photo/handwriting-to-print conversion.
  Use whenever the user asks for any of these, in Bangla or English (e.g. "স্লাইড বানাও",
  "বোর্ড প্রশ্ন", "মডেল টেস্ট", "নোট বানাও কিউআর সহ", "প্র্যাকটিস শিট", "থাম্বনেল", "মেনিম ভিডিও",
  "হাতে লেখা প্রশ্ন থেকে প্রিন্ট কপি").
---

# Bangla EdTech Studio

> **বাংলা সারাংশ:** এই স্কিল দিয়ে যেকোনো AI এজেন্ট — স্লাইড, বোর্ড প্রশ্নপত্র (MCQ/CQ), মডেল টেস্ট,
> বুয়েট রিটেন, কিউআর-সহ/ছাড়া নোট, প্র্যাকটিস শিট, থাম্বনেল প্রম্পট, মেনিম ভিডিও এবং
> ছবি/হাতের লেখা থেকে প্রিন্ট-রেডি প্রশ্ন — সব একই মানের, একই ডিজাইন-সিস্টেমে বানাতে পারবে।
> PDF সব সময় **XeLaTeX** দিয়ে, ভিডিও **Manim** দিয়ে। বাংলা ফন্ট: **Tiro Bangla** (ডিফল্ট) বা **Noto Serif Bengali**।

## 0. Files in this skill

```
SKILL.md                    ← you are here (router + rules)
references/                 ← read the ONE file for the requested mode before starting
  setup.md                  install XeLaTeX, fonts, Manim (Linux / macOS / Windows), troubleshooting
  slides.md                 MCQ / CQ teaching slides (16:9)
  board-papers.md           SSC/HSC board MCQ paper, board CQ paper, book-style model tests
  buet-written.md           BUET / engineering-admission written paper
  notes.md                  book-style notes WITH QR (transcript → timestamps) and WITHOUT QR
  practice-sheet.md         2-column practice sheet, answers, solutions (end / inline)
  thumbnail.md              thumbnail style system + intake form + prompt template
  manim-video.md            Manim explainer videos in Bangla (black background)
  photo-to-print.md         photo / handwritten paper → print-ready paper (OCR + diagram rebuild)
  diagrams.md               TikZ / circuitikz / pgfplots / mhchem cookbook + known pitfalls
  macros.md                 full command reference of edtech.sty / edtech-slides.sty
templates/
  edtech.sty                the design system for every PDF (fonts, colours, boxes, MCQ/CQ engines, QR)
  edtech-slides.sty         16:9 slide system built on edtech.sty
  manim_bangla.py           Manim helpers (Bangla text, XeLaTeX Tex, captions, palette)
scripts/
  setup.sh                  one-shot installer (Linux/macOS)
  build.sh                  compile .tex (XeLaTeX ×2) + PNG previews + automatic page-fill check
  check_fill.py             page-fill rule: fails if any non-last page leaves a big empty band
  verify_qr.py              decode every QR in a PDF + check each is a clickable link
  fetch_transcript.py       YouTube transcript → "[mm:ss] text" lines (or normalise SRT/VTT/pasted text)
  export_slides.sh          slide PDF → 1920×1080 PNGs
assets/                     placeholder logos (replace with the user's logo)
demos/                      2-page reference outputs for every mode (open them to see the target quality)
```

If your environment cannot read sub-files, use `EDTECH_SKILL_ALL_IN_ONE.md` (same content in one file).

## 1. Route the request

| User asks for | Mode | Read | Template / demo |
|---|---|---|---|
| MCQ slide / CQ slide, "স্লাইড" | `slides` | references/slides.md | demos/08-slides |
| বোর্ড প্রশ্ন (MCQ) | `board-mcq` | references/board-papers.md | demos/01-board-mcq |
| বোর্ড প্রশ্ন (CQ / সৃজনশীল) | `board-cq` | references/board-papers.md | demos/02-board-cq |
| মডেল টেস্ট (MCQ/CQ) | `model-test` | references/board-papers.md | demos/03-model-test |
| BUET / engineering written | `buet-written` | references/buet-written.md | demos/07-buet-written |
| নোট + কিউআর (YouTube) | `note-qr` | references/notes.md | demos/04-note-qr |
| নোট (কিউআর ছাড়া) | `note` | references/notes.md | demos/05-note-noqr |
| প্র্যাকটিস শিট | `practice` | references/practice-sheet.md | demos/06-practice-sheet |
| থাম্বনেল | `thumbnail` | references/thumbnail.md | demos/11-thumbnail |
| ভিডিও / Manim / "বুঝিয়ে দাও ভিডিওতে" | `manim` | references/manim-video.md | demos/09-manim |
| ছবি/হাতে লেখা → প্রিন্ট | `photo-to-print` | references/photo-to-print.md + board-papers.md | demos/10-photo-to-print |

Always also skim `references/diagrams.md` when the content has any figure, circuit, graph or apparatus.

## 2. Intake — ask only what is missing (one short message, Bangla)

Ask **at most once**, bundle questions, offer defaults. Never block on optional items.

| Item | Default if user says "তুমি ঠিক করো" |
|---|---|
| Class / exam (SSC / HSC / Admission), subject, paper, chapter/topic | — (required) |
| Content source: text, photo, slides, PDF, transcript, YouTube link, or "you write" | agent writes |
| Count (questions / slides / pages) | board standard (see board-papers.md) |
| Brand: platform name + logo file | no logo, brand text "EduBrand" removed |
| Bangla font | Tiro Bangla (`[tiro]`); alt Noto Serif Bengali (`[notoserif]`) |
| Paper size | A4 (Letter for BUET style) |
| Answers / solutions | MCQ: answer key at end. Practice: **ask** "সমাধান শেষে চাও, নাকি প্রতিটি প্রশ্নের পরেই?" |
| Slide theme | black background, white text, yellow accent |
| Note with QR: video link + transcript + slides | transcript fetched by agent if possible, else ask |

## 3. Non-negotiable quality rules

1. **Accuracy over speed.** Every number, unit, formula, chemical equation and answer must be correct.
   Solve every question you write *before* typesetting it; check answers twice (for MCQ make sure exactly
   one option is right; for CQ make sure the stimulus contains every value the parts need).
2. **Never fabricate records.** Board tags (ঢা. বো. ২৩ …), "যতবার এসেছে" counts, school names, years:
   only from the user's material or verifiable sources. Otherwise use neutral tags
   ("বোর্ড স্টাইল", "ভর্তি পরীক্ষা স্টাইল", "অনুশীলনী") or mark the table **"ডেমো ডেটা"**.
3. **Faithful transcription** (photo/handwriting): reproduce wording exactly as printed — including odd
   spellings — and list doubts in `verify.md` instead of silently "fixing". Do not reproduce third-party
   watermarks, logos or names that are not part of the question.
4. **Bangla typography:** Unicode Bangla only (no Bijoy/SutonnyMJ ANSI), danda `।`, Bangla digits for
   numbering/marks (১, ২ … via `\bnnum`), Latin digits inside math/units, `ক খ গ ঘ` for CQ parts,
   `(ক) (খ) (গ) (ঘ)` options, units via `\SI{}{}`, chemistry via `\ce{}`. Never break a unit from its number.
5. **Diagrams are drawn, never pasted** — TikZ/circuitikz/pgfplots, labelled exactly as the text,
   geometrically correct (angles, ratios, proportional lengths). No overlapping labels.
6. **Visual QA loop is mandatory**: `scripts/build.sh file.tex` → open every `*-preview-N.png` → fix
   overflow, overlaps, orphan headers, empty pages, broken glyphs (`Missing character` in log) → rebuild.
   A page is done only when you have looked at it.
7. **QR notes**: run `scripts/verify_qr.py file.pdf` — every QR must decode, be clickable, and contain
   `&noapp=1` and the correct `&t=<seconds>s`.
8. Keep the design system: use the macros in `templates/edtech.sty`; do not invent new looks per job
   unless the user asks. Brand logo only where the user wants it (header, banner, slides, footer).
9. **PAGE-FILL RULE (পেজ ভরাট নিয়ম) — applies to EVERY PDF.** A page may move on to the next page only
   when it is full: no page (except the very last page of the document) may leave an empty band larger than
   ~8 % of the page height — never 30–40 % blank at the bottom, never an empty column in a 2/3-column layout.
   `scripts/build.sh` runs `scripts/check_fill.py` automatically; **a `FAIL` line means the PDF is not
   deliverable.** Fix in this order:
   a. Remove forced breaks: no `\newpage`/`\clearpage` between parts of the same document (use `\flowbreak`).
      A new page is allowed only when a new, independent document starts — and then prefer a separate PDF.
   b. Let big blocks break: concept/tip/shadow boxes are `breakable`; long tables use `xltabular`
      (repeats header with `\endhead`) instead of `tabularx`; never wrap a long section in a minipage.
   c. Keep headings with their content (`\Needspace` is built into `\sectionbar`, `\topicbar`, `\typehead`,
      `\slantedtitle`) and keep each MCQ / short problem unsplit — but nothing larger.
   d. Re-order: move a following figure/table/box that fits into the gap; place a diagram beside text instead of below it.
   e. Tune (small steps, look again): diagram `scale`, `\columnsep`, font size/line spacing of that section
      (`\fontsize{10}{14}\selectfont`, `\fillpage{1.1}`), geometry margins by ≤ 3 mm.
   f. If the agent writes the content: add genuinely useful content (one more problem, a "মনে রাখো" box, a tip).
      Never fill with meaningless whitespace (`\vfill`, big `\vspace`) — that is still an empty page.
   Exceptions: the document's last page; designed answer-writing space (BUET/written papers →
   `FILL_ALLOW=all scripts/build.sh file.tex`); slides; a cover page. Re-run until every page is `ok`.
10. Deliver: `.pdf` + editable `.tex` (+ `png/` for slides, `.mp4` for videos, `verify.md` when relevant).

## 4. Toolchain (summary — details in references/setup.md)

- **XeLaTeX** (TeX Live 2023+): fontspec, unicode-math, tikz, circuitikz, pgfplots, tcolorbox, siunitx,
  mhchem, qrcode, multicol, tabularx, enumitem, fancyhdr, hyperref.
- **Fonts:** Tiro Bangla (body), Noto Serif Bengali Bold (bold Bangla), Hind Siliguri (headings, slides),
  TeX Gyre Termes (+ Termes Math) for Latin & math — Latin/Bangla switch automatically (XeTeX interchar).
- **Manim Community** ≥ 0.18 + ffmpeg + cairo/pango (Bangla via Pango `Text`, mixed via XeLaTeX `Tex`).
- **Python:** pyzbar, pypdf, qrcode, youtube-transcript-api, yt-dlp.
- Compile: `TEXINPUTS=<skill>/templates//:<skill>/assets//: xelatex -interaction=nonstopmode file.tex` (twice)
  — or simply `scripts/build.sh file.tex`.

## 5. Universal workflow

1. Read the mode reference. 2. Intake (§2). 3. Draft the **content** first (questions, solutions,
concept map) in plain text and self-check it. 4. Copy the closest demo `.tex` as the starting point.
5. Fill content using the macros. 6. Build → look at every preview → fix → rebuild (§3.6) — until `check_fill` shows no `FAIL` (§3.9).
7. Run mode-specific checks (QR verify, answer-key cross-check, page count). 8. Deliver with a 3–5 line
summary in Bangla: what was made, page count, anything the user must verify.

## 6. Branding / logo

- `\etset{brand=<name>, logo=<file.png>}` — header text, footer pill, chapter banner (`\etlogo`).
- Slides: `\slidesetup{logo=<white-or-transparent logo>, logoright=<second logo>}`. Prefer a transparent
  PNG/SVG→PDF; for black slides ask for a white/light version (or invert with ImageMagick if it is monochrome).
- Watermark (BUET / sheets): `\etset{watermark=<text>}` — very light, behind text.
- Never invent a logo or put another institution's logo on the user's material.
