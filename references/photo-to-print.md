# Mode: photo-to-print (photographed / handwritten paper → print-ready paper)

Input: one or more photos/scans of a question paper (printed or handwritten), possibly skewed, with
pens, shadows, scribbles, watermarks. Output: a clean, print-ready PDF in the requested style
(board CQ/MCQ, model test, practice sheet …) + `verify.md`.

Demo: `demos/10-photo-to-print/` (`input/photo-1.jpeg`, `input/photo-2.jpeg` → `photo-to-print.pdf`, `verify.md`).

## Procedure
1. **Inspect** each photo at full resolution; crop/zoom regions (PIL: `crop().resize(×2–3, LANCZOS)`)
   until every character is readable. Do not guess from a thumbnail.
2. **Transcribe exactly** into a plain-text draft, line by line: header fields (board, code, set, subject,
   paper, time, marks, instruction sentence verbatim), question numbers, stimuli, parts, marks, options.
   - Keep the original wording/spelling/punctuation (e.g. "করো" vs "কর", "মনোযোগসহকারে").
   - Convert numbers faithfully: Bangla digits stay Bangla; Latin digits inside formulae stay Latin.
   - Chemistry → `\ce{}`, units → `\SI{}{}`, math → LaTeX.
3. **Diagrams**: identify every figure (beakers, circuits, graphs, geometry, tables). Rebuild in TikZ /
   circuitikz / pgfplots / tabular with the same labels, values, arrangement and relative proportions.
   Graphs: same axes, ticks, intercepts and curve shape. Never paste the photo.
4. **Separate noise from content**: handwriting/marks by a reader (ticks, circles, "২+" scribbles,
   underlines), pens/clips, third-party watermarks or teacher names → not reproduced; list them in verify.md.
5. **Doubts** → `verify.md` table (# | photo | where | what you saw | what you typeset | why). Ask the user only
   about items that change meaning (a number, a unit, a word that could be two words).
6. **Typeset** with the matching template (board CQ: `\boardcqheader{…, instr={verbatim}}` + `\cq`;
   MCQ: `\boardmcqheader` + `\mcq`). If the user wants a *model-test* look instead of the original look,
   keep the content identical and change only the layout.
7. **Do not copy the photo's page breaks.** Typeset continuously and let pages fill (page-fill rule); the
   "[পর পৃষ্ঠা দ্রষ্টব্য" marker only at the end of a page that really continues. One question paper = one PDF.
8. **QA**: build, then compare each preview side by side with the photo — every question, every part,
   every mark, every label in each diagram. Count questions and options. Re-read numbers digit by digit.

Handwritten originals: the same, plus — expand obvious abbreviations only if the user asks; keep the
writer's numbering; if a figure is a rough sketch, redraw it neatly but do not add information that is not
on the sketch (no invented values or labels).
