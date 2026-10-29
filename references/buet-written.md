# Mode: buet-written (BUET / engineering admission written paper)

Look (user reference): every page framed by a thin rectangle, questions numbered `01.` `02.` in bold
Latin, Bangla question followed by the English version in square brackets, generous blank answer space,
optional QR (video solution) at the right of each question, black footer bar inside the frame with the
set name, page number outside bottom-right, optional light diagonal watermark. Usually 2 questions/page.

Demo: `demos/07-buet-written/buet-written.tex`.

```latex
\documentclass[11pt]{article}
\usepackage[tiro,letter]{edtech}
\geometry{left=20mm,right=19mm,top=19mm,bottom=27mm}
\etset{footer={BUET Written Practice · ভেক্টর}, watermark={EduBrand}, ytid=VIDEOID, qrsize=1.5cm}
\buetframe
\pagestyle{empty}
\begin{document}
\wq{08:40}{বাংলা প্রশ্ন … [English version …]
  \begin{center}\begin{tikzpicture} … \end{tikzpicture}\end{center}}{\stretch{1}}
\wq{}{… (no QR) …}{\stretch{1.4}}        % 4th arg = answer space (\stretch{} shares the page)
\newpage
\wq[10]{21:50}{… with marks …}{8cm}       % [marks] optional, printed at the end of the question
\end{document}
```

Rules
- Build with `FILL_ALLOW=all scripts/build.sh file.tex`: the blank area here is answer-writing space by design. Everything else on the page must still be tight (no gap above a question).
- Subjects: Physics, Chemistry, Higher Math (and English if asked). Difficulty: multi-step, numeric,
  derivations; SI units; give constants inside the question.
- English text must be a faithful translation of the Bangla (same numbers, same symbols).
- Answer space: two questions per page with `\stretch{1}` / `\stretch{1.4}`; a question with a large figure gets the larger share.
- If the user wants solutions, add a separate "Solution" PDF (same frame) — never on the question pages.
- QR: only when a real video + timestamp exists (see notes.md for the QR rules). Verify with `scripts/verify_qr.py`.
