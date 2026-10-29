# Mode: slides (MCQ / CQ teaching slides)

Reference look (from the user's references): black board, 16:9, logo top-left (optional second logo
top-right), question at the top, **options stacked on the right** in light rounded boxes, the **left
side stays empty** so the teacher can solve live with a pen/smart board. CQ: board tag (yellow),
stimulus, table/diagram and the asked part (yellow label) in the **right panel**; left side empty.

Demo: `demos/08-slides/mcq-slides.tex`, `cq-slides.tex` (+ `png/` 1920×1080 exports).

## Skeleton
```latex
\documentclass{article}
\usepackage{edtech-slides}
\slidesetup{logo=my-logo-white.png, footer={অধ্যায় ২ · ভেক্টর · MCQ}, labels={A,B,C,D}}
\begin{document}
\mcqslide[tag=বোর্ড স্টাইল]{21}{$-7<x+3<5$ কে পরম মানের সাহায্যে প্রকাশ কর:}
  {$|x+4|<6$}{$|x+1|<3$}{$|x+3|<6$}{$|x+2|<4$}
\cqslide[tag=কু. বো. ২০২২]{%
  উদ্দীপক লেখা …\par\medskip
  \begin{tabular}{|c|c|}\hline … \\\hline\end{tabular}   % white rules automatically
  \slidepart{গ}{প্রশ্ন …}
  \slidepart{ঘ}{প্রশ্ন …}}
\end{document}
```
Build: `scripts/build.sh deck.tex 60` then `scripts/export_slides.sh deck.pdf` → `png/deck-N.png`.

## Options (`\slidesetup{…}` globally or `[…]` per slide)
| key | default | meaning |
|---|---|---|
| `bg`, `fg` | black, white | background / text colour (user may want dark blue `HTML 0B1D3A`, green board `HTML 12301F`) |
| `accent` | etyellow | question number, tag (CQ), part labels |
| `optbg`, `optfg` | light grey, black | option boxes |
| `labels` | `A,B,C,D` | use `ক,খ,গ,ঘ` for Bangla-medium decks |
| `logo`, `logoright` | — | image files (use light/white logos on dark slides) |
| `footer` | — | small grey text bottom-left (chapter / class name) |
| `qsize`, `optsize`, `cqsize` | 27, 25, 23 | font sizes (pt). Reduce by 2–3 for long questions. |
| `tag` | — | board/source tag e.g. `ঢা. বো. ১৯` (only real tags — see SKILL.md §3.2) |

## Rules
- One question per slide. If the stem is > 3 lines, lower `qsize`; if an option is > 1 line, lower `optsize`.
- MCQ with a figure: put the figure in the question (it is pre-boxed, so TikZ works) and keep it left-aligned
  under the stem so the right column still holds the options.
- CQ: one slide per asked part (গ on one slide, ঘ on the next) unless the user wants both together.
  Repeat the stimulus on each slide (the board is erased between parts).
- Diagrams on dark slides: TikZ uses the current text colour (white) — set accents with `etyellow`, `cyan!70`, `green!60`.
- Never place anything in the left 45 % except the question stem and logo.
- Deliver PDF + PNGs (OBS/video editors use PNG). Offer a "solution slide" variant only if asked.
