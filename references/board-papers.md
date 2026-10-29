# Modes: board-mcq, board-cq, model-test

Demos: `demos/01-board-mcq`, `demos/02-board-cq`, `demos/03-model-test`.

## Board standards (use unless the user says otherwise)
| Exam | MCQ | CQ |
|---|---|---|
| SSC science subjects | 25 Q, 25 min, 25 marks | 8 Q (answer 5 of 8 — or as the user's board says), 2 h 35 min, 50 marks |
| HSC science subjects | 25 Q, 25 min, 25 marks | 8 Q, answer 5, 2 h 35 min, 50 marks |
| Humanities/Business (70-mark CQ) | 30 Q, 30 min, 30 marks | 11 Q, answer 7, 2 h 30 min, 70 marks |
CQ part marks: ক ১, খ ২, গ ৩, ঘ ৪ (knowledge, comprehension, application, higher-order).
If the user names a different year/board pattern, follow the user.

## A. Real board look (`board-mcq`)
Top line: board/set name (left) · code (centre) · serial (right). Centre stack: exam name, subject, paper,
syllabus line, সময়, পূর্ণমান. Right: box with বিষয় কোড boxes + সেট box. Rule. বিশেষ দ্রষ্টব্য paragraph.
Bold line "প্রশ্নপত্রে কোনো প্রকার দাগ/চিহ্ন দেয়া যাবে না।" Two columns, no column rule.
```latex
\documentclass[11pt]{article}
\usepackage[tiro]{edtech}
\geometry{margin=15mm,top=12mm,bottom=14mm}
\pagestyle{empty}\setlength{\columnsep}{8mm}
\begin{document}
\boardmcqheader{name=যমুনা, center=১৩৬, serial=৪১০৮/২০২৬, subject=পদার্থবিজ্ঞান, paper={},
  time=২৫ মিনিট, marks=২৫, code=136, set=খ}
\begin{multicols}{2}
\mcq[গ]{stem}{opt1}{opt2}{opt3}{opt4}              % [answer] is stored for \answerkey
\mcqmulti[খ]{stem—}{i}{ii}{iii}                     % multiple-completion (i ও ii …) — options automatic
\stimulus[2]{passage / table / tikz}               % prints "নিচের উদ্দীপকটি পড় এবং ৫ ও ৬নং প্রশ্নের উত্তর দাও:"
\mcq[ক]{…}{…}{…}{…}{…}
\end{multicols}
\answerkey            % optional (teacher copy) — omit for the student copy
\end{document}
```
Options lay out automatically: 4 in a row (short), 2×2 (medium), or one per line (long).
Numbering: `\qnumstyle{danda}` (১।, default) or `\qnumstyle{dot}` (১.). Labels: `\optstyle{paren}` (ক) or `\optstyle{circled}` ⓚ.
For the student copy + teacher copy, compile twice with/without `\answerkey`.

## B. Real board look (`board-cq`)
```latex
\cqstyle{board}
\boardcqheader{name=…, center=১৭৪, serial=…, set=০২ সেট, subject=পদার্থবিজ্ঞান, paper=প্রথম পত্র,
  time={২ ঘণ্টা ৩৫ মিনিট}, marks=৫০, code=১৭৪, note={যে কোনো পাঁচটি প্রশ্নের উত্তর দিতে হবে।}}
\cq{stimulus (text + tikz/table)}{ক}{খ}{গ}{ঘ}           % marks ১ ২ ৩ ৪ in the right margin
\cq{…}{…}{…}{…}{…}[২][২][৩][৩]                          % custom marks
\cqpart{ঙ}{extra part}{২}                                % free-form part
\continued                                              % "[পর পৃষ্ঠা দ্রষ্টব্য" at page foot
```
`instr={…}` overrides the দ্রষ্টব্য sentence verbatim (photo-to-print uses this).
Geometry: `left=20mm,right=24mm` leaves the marks column.

## C. Book-style model test (`model-test`)
MCQ: 3 columns with rules, small font, circled options, numbers `১.`, header via `\modeltestheader`,
answer grid (`\answerkey`) at the bottom. CQ: 2 columns with rule, `\cqstyle{book}` → "১ ▸" numbering and `ক.` parts with marks at line end.
```latex
\modeltestheader{এক্সক্লুসিভ মডেল টেস্ট ০১}{রসায়ন প্রথম পত্র\etsep বহুনির্বাচনি অভীক্ষা}{২৫ মিনিট}{২৫}{176}{instruction text}
\optstyle{circled}\qnumstyle{dot}
\begin{multicols}{3}\small … \end{multicols}\answerkey
\newpage\setcounter{etq}{0}\cqstyle{book}
\modeltestheader{…}{রসায়ন প্রথম পত্র\etsep সৃজনশীল প্রশ্ন}{২ ঘণ্টা ৩৫ মিনিট}{৫০}{176}{…}
\begin{multicols}{2}\small \cq{…}{…}{…}{…}{…} … \end{multicols}
```
Logo: `\etlogo[0.8cm]` above the header (left) if the user wants branding.

## Page fill (SKILL.md §3.9)
Each paper must fill its pages. A 25-question MCQ or a CQ paper often ends at 70–85 % of a page: fix by
tuning the question font/spacing of the whole paper (`\fontsize{10}{14}\selectfont` inside the multicols,
`\columnsep`, margins), diagram scales, or by moving the answer key. If MCQ and CQ are two separate papers,
each starts on its own page (or better: two PDFs); the end of each paper is its "last page".

## Writing good questions (when the agent writes them)
- Follow the NCTB syllabus of the stated year; mix knowledge (জ্ঞানমূলক), comprehension, application, higher order.
- MCQ distractors must be plausible (common mistakes: wrong unit, sign, factor 2, g/mol vs kg/mol).
- Multiple-completion: exactly the combination you mark must be correct; check each statement separately.
- Stimulus-based MCQ sets: 2–3 questions per stimulus, all answerable from it.
- CQ: গ = direct calculation from the stimulus; ঘ = comparison/decision with calculation ("…কি না—গাণিতিকভাবে বিশ্লেষণ কর").
- Solve everything; keep a hidden solution list; never ship an unsolvable or ambiguous item.
- Balance: page breaks should not split a question from its options (each `\mcq` is a minipage; long stimulus sets may need `\columnbreak`).
