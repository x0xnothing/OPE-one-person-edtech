# Mode: practice (practice sheet)

Look (user reference IMG_9136): two columns with a thin column rule; centred chapter title
("অধ্যায়-২" / "ভেক্টর"); blue full-width **topic bars** ("Topic-1: ভেক্টরের লব্ধি") grouping questions
**type-wise**; `Problem-01 :` label in Latin serif, the source tag flush right in blue brackets, the
**answer right under each problem** (`উত্তর :` / `সমাধান :`); black footer bar: subject | page | chapter.

Demo: `demos/06-practice-sheet/practice-sheet.tex` (written problems + MCQ topic + solutions at the end).

## Ask the student (once)
1. Question type(s): Written (default) / MCQ / CQ — mixed is fine, one Topic bar per type/topic.
2. Answers: short answer under each problem (default ✔).
3. Full solutions? → **"শেষে একসাথে চাও, নাকি প্রতিটি প্রশ্নের ঠিক পরে?"**
   `\solutionsatend` (default) → `\printsolutions` adds the "সমাধান" section right after the last problem (no forced new page — page-fill rule);
   `\solutionsinline` → a blue solution box right after each problem.

```latex
\documentclass[10pt]{article}
\usepackage[tiro]{edtech}
\geometry{left=12mm,right=12mm,top=12mm,bottom=20mm,footskip=10mm}
\etset{subject={পদার্থবিজ্ঞান ১ম পত্র}, chapter={অধ্যায় ০৩: গতিবিদ্যা}}
\pagestyle{barfoot}
\setlength{\columnseprule}{0.4pt}
\solutionsatend            % or \solutionsinline
\begin{document}
\begin{center}{\headfont\bfseries\Large অধ্যায়-৩}\\{\headfont\bfseries\LARGE গতিবিদ্যা}\end{center}
\begin{multicols}{2}
\topicbar{Topic-1: সমত্বরণ}
\problem{question text}[source tag]{short answer}
\solution{full working (math, tikz allowed)}
\topicbar{Topic-3: MCQ অনুশীলন}
\pmcq[source]{stem}{a}{b}{c}{d}{(খ) answer — optional one-line reason}
\end{multicols}
\printsolutions[সমাধান]          % only with \solutionsatend
\end{document}
```
CQ items inside a practice sheet: use `\cqstyle{book}` + `\cq{…}` inside the columns and put the
short answers of গ/ঘ in a line after it (`\textbf{উত্তর :} (গ) … (ঘ) …`).

Rules: problems ordered easy → hard inside each topic; every answer re-solved; units on every answer;
source tags only if real (else "বোর্ড স্টাইল", "ভর্তি পরীক্ষা স্টাইল", "অনুশীলনী"); fill the page.
