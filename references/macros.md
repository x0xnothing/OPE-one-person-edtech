# Command reference — edtech.sty / edtech-slides.sty

Load: `\usepackage[tiro|notoserif, a4|letter|legal]{edtech}` (XeLaTeX only).

## Settings
| Command | Purpose |
|---|---|
| `\etset{brand=, book=, chapter=, subject=, logo=, logoheight=, ytid=, qrsize=, watermark=, footer=}` | global settings |
| `\etlogo[height]` | the logo image (nothing if no logo set) |
| `\bnnum{12}` → ১২ · `\bnarabic{counter}` · `\twodigit{5}` → 05 | Bangla digits |
| `\headfont` (Hind Siliguri) · `\latinserif` (Termes) · `\latinsans` (Heros) · `\symfont` (DejaVu) | font switches |
| colours: `etblack etblue etdeepblue etred etgray etgraydark etyellow etfill etaccent` | palette |

## QR / links
| `\ytqr[size]{mm:ss}` | QR → `youtube.com/watch?v=<ytid>&t=<s>s&noapp=1`, clickable + label |
| `\ytqrid[size]{ID}{h:mm:ss}` | QR for another video |
| `\urlqr[size]{url}[label]` | QR for any URL |
| `\ytlink{mm:ss}{text}` | clickable text link to the timestamp |
| `\withqr[size]{mm:ss}{content}` | content with a QR floated to its right |
| `\linkbox{url}{box content}` | make any box clickable (XeLaTeX-safe) |
| `\yturl{ID}{mm:ss}` | expands to the URL string |

## Page furniture
| `\pagestyle{note}` | dotted running header (page · brand ▸ book), brand pill footer (twoside) |
| `\pagestyle{barfoot}` | black footer bar: subject · page · chapter |
| `\buetframe` | page frame + black footer bar (`footer=`) + page number |
| `\chapterbanner{অধ্যায়}{বাংলা শিরোনাম}{English title}{right box content}` | chapter banner |
| `\sectionbar{text}` · `\slantedtitle{text}` · `\pilltitle{text}` · `\topicbar{text}` | section headings |
| `\typehead{01}{title}` | "Type 01  title" box |
| envs `conceptbox` (dashed) · `roundbox` · `shadowbox` · `tipbox[title]` (red) · `remember[title]` (double rule) | boxes |
| `\prashna{১}` · `\partlabel{গ}` · `\blacklabel{text}` · `\boardtag{…}` · `\srctag{…}` · `\stars{4}` · `\ans` · `\markat{৪}` | labels |
| `\solgiven[width]{working}{given}` | solution with "দেওয়া আছে" column |
| `\etsep` | ▶-in-circle separator for headers |

## Page fill
| `\flowbreak[0.1]` | new page only if < 10 % of the page is left — put before a new section/multicols instead of `\newpage` (avoids a lonely heading at the page foot) |
| `\fillpage{1.1}` | stretch line spacing of what follows to reach the page end (fine tuning) |
| `\Needspace{6\baselineskip}` | keep a heading with the following lines (already inside the heading macros) |
| `xltabular` env | breakable `tabularx` (use `\endfirsthead`/`\endhead` to repeat the header) |

## Question engines
| `\mcq[ans]{stem}{a}{b}{c}{d}` | auto-numbered MCQ, auto option layout |
| `\mcqmulti[ans]{stem}{i}{ii}{iii}` | multiple completion with standard options |
| `\stimulus[n]{passage}` | "নিচের উদ্দীপকটি পড় এবং … নং প্রশ্নের উত্তর দাও:" (n = number of linked questions) |
| `\options{a}{b}{c}{d}` | options only |
| `\answerkey[title]` | grid of stored answers |
| `\optstyle{circled|paren}` · `\qnumstyle{danda|dot}` | MCQ look |
| `\cq{stimulus}{ক}{খ}{গ}{ঘ}[m1][m2][m3][m4]` · `\cqpart{label}{text}{mark}` · `\cqstyle{board|book}` | CQ |
| `\boardmcqheader{name=,center=,serial=,exam=,subject=,paper=,syllabus=,time=,marks=,code=,set=}` | board MCQ header |
| `\boardcqheader{…, note=, instr=}` | board CQ header |
| `\modeltestheader{title}{subject line}{time}{marks}{code}{instruction}` | book/model-test header |
| `\codeboxes{176}` · `\continued` | subject-code boxes · "[পর পৃষ্ঠা দ্রষ্টব্য" |
| counter `etq` (questions) — reset with `\setcounter{etq}{0}` for a new paper in the same file |

## Practice sheet
| `\problem{text}[source]{answer}` · `\pmcq[source]{stem}{a}{b}{c}{d}{answer}` | numbered Problem-NN |
| `\solution{working}` · `\solutionsatend` / `\solutionsinline` · `\printsolutions[title]` | solutions |

## BUET written
| `\wq[marks]{mm:ss or empty}{question}{answer space}` | 01., 02. … with optional QR |

## Slides (edtech-slides.sty)
| `\slidesetup{bg,fg,accent,optbg,optfg,logo,logoright,footer,labels,qsize,optsize,cqsize}` | theme |
| `\mcqslide[tag=…]{no}{question}{A}{B}{C}{D}` | MCQ slide |
| `\cqslide[tag=…]{content}` + `\slidepart{গ}{text}` | CQ slide |
| `\titleslide{title}{subtitle}` | title slide |
