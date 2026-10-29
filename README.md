# 🎓 Bangla EdTech Studio — One-Person EdTech (OPE)

> **এক ফোল্ডারে পুরো "ওয়ান-পারসন এডটেক স্টুডিও"।**
> যেকোনো AI এজেন্টকে এই স্কিলটা দিলে সে একই মানের, একই ডিজাইন-সিস্টেমে বানাতে পারবে —
> বোর্ড প্রশ্নপত্র, মডেল টেস্ট, বুয়েট রিটেন, কিউআর-সহ/ছাড়া নোট, প্র্যাকটিস শিট, স্লাইড,
> থাম্বনেল প্রম্পট, Manim ভিডিও আর ছবি → প্রিন্ট-রেডি প্রশ্ন।

![XeLaTeX](https://img.shields.io/badge/PDF-XeLaTeX-blue)
![Manim](https://img.shields.io/badge/Video-Manim-orange)
![Language](https://img.shields.io/badge/Language-বাংলা-green)
![Level](https://img.shields.io/badge/Level-SSC%20%7C%20HSC%20%7C%20Admission-purple)

---

## ✨ কী কী বানানো যায়

| # | জিনিস | মোড | আউটপুট |
|---|-------|------|---------|
| ১ | SSC/HSC বোর্ড MCQ প্রশ্নপত্র (+ উত্তরমালা) | `board-mcq` | PDF |
| ২ | HSC বোর্ড CQ (সৃজনশীল) প্রশ্নপত্র | `board-cq` | PDF |
| ৩ | মডেল টেস্ট (MCQ + CQ) | `model-test` | PDF |
| ৪ | বই-স্টাইল নোট — **কিউআর সহ** (YouTube টাইমস্ট্যাম্প) | `note-qr` | PDF |
| ৫ | বই-স্টাইল নোট — কিউআর ছাড়া | `note-noqr` | PDF |
| ৬ | প্র্যাকটিস শিট (উত্তর পাশে, সমাধান শেষে) | `practice-sheet` | PDF |
| ৭ | বুয়েট-স্টাইল রিটেন পেপার | `buet-written` | PDF |
| ৮ | MCQ ও CQ টিচিং স্লাইড (16:9, কালো বোর্ড) | `slides` | PDF + PNG |
| ৯ | Manim এক্সপ্লেইনার ভিডিও (বাংলা) | `manim` | MP4 (1080p) |
| ১০ | ছবি / হাতে-লেখা → প্রিন্ট-রেডি প্রশ্ন | `photo-to-print` | PDF |
| ১১ | থাম্বনেল প্রম্পট + লেআউট গাইড | `thumbnail` | প্রম্পট প্যাক |

সব PDF-এর একটাই ডিজাইন সিস্টেম — `templates/edtech.sty` · সব স্লাইডের — `templates/edtech-slides.sty`

---

## 🚀 কোন এজেন্টে কীভাবে দেবেন

| এজেন্ট | কী করবেন |
|---|---|
| **Claude Code / Claude (Skills সাপোর্ট)** | পুরো ফোল্ডারটা `~/.claude/skills/bangla-edtech-studio/` তে রাখুন। এরপর শুধু বলুন — *"HSC ফিজিক্স ভেক্টরের ২৫টা MCQ বোর্ড প্রশ্ন বানাও"* |
| **Codex / Cursor / অন্য কোডিং এজেন্ট** | ফোল্ডারটা প্রজেক্টে রাখুন, প্রথম মেসেজে বলুন: *"`SKILL.md` পড়ে সেই অনুযায়ী কাজ করো"* |
| **ChatGPT / Gemini (ফাইল আপলোড)** | `EDTECH_SKILL_ALL_IN_ONE.md` আপলোড করুন — সব নির্দেশনা + টেমপ্লেট একটাই ফাইলে। কোড চালানোর সুবিধা থাকলে PDF পর্যন্ত বানাবে, না থাকলে `.tex` দেবে — Overleaf-এ (Compiler: **XeLaTeX**) চালালেই PDF |

প্রথমবার নিজের কম্পিউটারে: `bash scripts/setup.sh` · Windows হলে `references/setup.md` দেখুন।

---

## 📸 ডেমো — প্রতিটা আলাদা করে

> সবগুলো ডেমো একসাথে এক ফাইলে: 📚 **[ALL-DEMOS.pdf](ALL-DEMOS.pdf)** (২০ পৃষ্ঠা)
> প্রতিটা ডেমোর সোর্স (`.tex`) ওই ডেমোর ফোল্ডারেই আছে — নিজে কম্পাইল করে যাচাই করতে পারবেন।

### ১ · বোর্ড MCQ প্রশ্নপত্র

বোর্ড-স্টাইল MCQ পেপার — সেট-কোড, সময়, পূর্ণমানসহ আসল পরীক্ষার ফরম্যাট, শেষে উত্তরমালা ও ব্যাখ্যা।

<img src="demos/01-board-mcq/board-mcq-preview-1.png" width="49%"> <img src="demos/01-board-mcq/board-mcq-preview-2.png" width="49%">

📄 [PDF](demos/01-board-mcq/board-mcq.pdf) · 💻 [সোর্স .tex](demos/01-board-mcq/board-mcq.tex)

### ২ · বোর্ড CQ (সৃজনশীল) প্রশ্নপত্র

উদ্দীপকসহ সৃজনশীল প্রশ্ন — জ্ঞান/অনুধাবন/প্রয়োগ/উচ্চতর দক্ষতার ধাপ মেনে, বোর্ডের আসল কাঠামোয়।

<img src="demos/02-board-cq/board-cq-preview-1.png" width="49%"> <img src="demos/02-board-cq/board-cq-preview-2.png" width="49%">

📄 [PDF](demos/02-board-cq/board-cq.pdf) · 💻 [সোর্স .tex](demos/02-board-cq/board-cq.tex)

### ৩ · মডেল টেস্ট

MCQ + CQ একসাথে পূর্ণাঙ্গ মডেল টেস্ট — কলেজ/কোচিংয়ের পরীক্ষার হুবহু ফরম্যাটে।

<img src="demos/03-model-test/model-test-preview-1.png" width="49%"> <img src="demos/03-model-test/model-test-preview-2.png" width="49%">

📄 [PDF](demos/03-model-test/model-test.pdf) · 💻 [সোর্স .tex](demos/03-model-test/model-test.tex)

### ৪ · নোট — কিউআর সহ ⭐

লেকচারের ট্রান্সক্রিপ্ট + স্লাইড থেকে বই-স্টাইল নোট। প্রতিটা কনসেপ্ট আর গণিতের পাশে **ছোট QR** —
স্ক্যান করলেই YouTube ভিডিওর ঠিক সেই টাইমস্ট্যাম্পে (`&noapp=1`, সরাসরি ব্রাউজারে খোলে)।

<img src="demos/04-note-qr/note-qr-preview-1.png" width="49%"> <img src="demos/04-note-qr/note-qr-preview-2.png" width="49%">

📄 [PDF](demos/04-note-qr/note-qr.pdf) · 💻 [সোর্স .tex](demos/04-note-qr/note-qr.tex) · 📥 [ইনপুট (ট্রান্সক্রিপ্ট/স্লাইড)](demos/04-note-qr/input/)

### ৫ · নোট — কিউআর ছাড়া

একই বই-স্টাইল নোট, QR ছাড়া — প্রিন্ট বা অফলাইন পড়ার জন্য পরিষ্কার সংস্করণ।

<img src="demos/05-note-noqr/note-noqr-preview-1.png" width="49%"> <img src="demos/05-note-noqr/note-noqr-preview-2.png" width="49%">

📄 [PDF](demos/05-note-noqr/note-noqr.pdf) · 💻 [সোর্স .tex](demos/05-note-noqr/note-noqr.tex)

### ৬ · প্র্যাকটিস শিট

দুই-কলাম প্র্যাকটিস শিট — প্রশ্নের পাশে সংক্ষিপ্ত উত্তর, বিস্তারিত সমাধান শেষে।

<img src="demos/06-practice-sheet/practice-sheet-preview-1.png" width="49%"> <img src="demos/06-practice-sheet/practice-sheet-preview-2.png" width="49%">

📄 [PDF](demos/06-practice-sheet/practice-sheet.pdf) · 💻 [সোর্স .tex](demos/06-practice-sheet/practice-sheet.tex)

### ৭ · বুয়েট-স্টাইল রিটেন

ইঞ্জিনিয়ারিং ভর্তি-স্টাইলের রিটেন পেপার — উত্তর লেখার জায়গাসহ, দ্বিভাষিক (বাংলা + English) প্রশ্ন।

<img src="demos/07-buet-written/buet-written-preview-1.png" width="49%"> <img src="demos/07-buet-written/buet-written-preview-2.png" width="49%">

📄 [PDF](demos/07-buet-written/buet-written.pdf) · 💻 [সোর্স .tex](demos/07-buet-written/buet-written.tex)

### ৮ · টিচিং স্লাইড (MCQ + CQ)

16:9 কালো-বোর্ড স্লাইড — ক্লাসে পড়ানোর জন্য বড় ফন্ট, পরিষ্কার ডায়াগ্রাম, এক স্লাইডে এক প্রশ্ন।

<img src="demos/08-slides/mcq-slides-preview-1.png" width="49%"> <img src="demos/08-slides/cq-slides-preview-1.png" width="49%">

📄 [MCQ স্লাইড PDF](demos/08-slides/mcq-slides.pdf) · [CQ স্লাইড PDF](demos/08-slides/cq-slides.pdf) · 💻 [সোর্স](demos/08-slides/)

### ৯ · Manim ভিডিও 🎬

বাংলা ক্যাপশনসহ Manim এক্সপ্লেইনার — ভেক্টরের লব্ধি (সামান্তরিক সূত্র), 1080p।

<img src="demos/09-manim/poster.png" width="70%">

▶️ **[ভিডিও দেখুন — vector_resultant_1080p.mp4](demos/09-manim/vector_resultant_1080p.mp4)** · 💻 [সোর্স .py](demos/09-manim/vector_resultant.py)

### ১০ · ছবি → প্রিন্ট-রেডি প্রশ্ন

ছবি বা হাতে-লেখা প্রশ্নের ছবি দিলে OCR + ডায়াগ্রাম রিবিল্ড করে প্রিন্ট-রেডি পেপার, সাথে যাচাই-তালিকা।

<img src="demos/10-photo-to-print/photo-to-print-preview-1.png" width="49%"> <img src="demos/10-photo-to-print/photo-to-print-preview-2.png" width="49%">

📄 [PDF](demos/10-photo-to-print/photo-to-print.pdf) · 💻 [সোর্স .tex](demos/10-photo-to-print/photo-to-print.tex) · ✅ [যাচাই তালিকা](demos/10-photo-to-print/verify.md)

### ১১ · থাম্বনেল প্রম্পট + লেআউট

YouTube থাম্বনেলের স্টাইল-সিস্টেম — রেডি প্রম্পট আর লেআউট গাইড (ইমেজ মডেলের জন্য)।

<img src="demos/11-thumbnail/layout-1-one-shot.png" width="49%"> <img src="demos/11-thumbnail/layout-2-exam-alert.png" width="49%">

📝 [থাম্বনেল প্রম্পট প্যাক](demos/11-thumbnail/thumbnail-prompts.md)

---

## 📂 রিপো-র গঠন

```
SKILL.md                    ← রাউটার + সব নিয়ম (এজেন্ট প্রথমে এটাই পড়ে)
EDTECH_SKILL_ALL_IN_ONE.md  ← পুরো স্কিল এক ফাইলে (ChatGPT/Gemini আপলোডের জন্য)
references/                 ← প্রতিটা মোডের আলাদা গাইড (11টা)
templates/
  edtech.sty                ← সব PDF-এর ডিজাইন সিস্টেম
  edtech-slides.sty         ← 16:9 স্লাইড সিস্টেম
  manim_bangla.py           ← Manim বাংলা হেল্পার
scripts/
  setup.sh                  ← এক-শট ইনস্টলার (Linux/macOS)
  build.sh                  ← XeLaTeX বিল্ড + প্রিভিউ + পেজ-ভরাট চেক
  check_fill.py             ← পেজ-ভরাট নিয়মের অটো-চেক
  verify_qr.py              ← PDF-এর সব QR ডিকোড + লিংক যাচাই
  fetch_transcript.py       ← YouTube ট্রান্সক্রিপ্ট সংগ্রহ
  export_slides.sh          ← স্লাইড PDF → 1920×1080 PNG
  thumbnail_layout.py       ← থাম্বনেল লেআউট হেল্পার
assets/                     ← লোগো (প্লেসহোল্ডার — নিজের লোগো বসান)
demos/                      ← 11টা মোডের ডেমো (PDF + প্রিভিউ + সোর্স)
```

---

## ⚠️ পেজ-ভরাট নিয়ম (খুব গুরুত্বপূর্ণ)

কোনো PDF-এ কোনো পেজ অর্ধেক বা ৩০–৪০% ফাঁকা রেখে পরের পেজে যাওয়া যাবে না — পেজ আগে ভরবে, তারপর পরের পেজ।
শুধু ডকুমেন্টের একদম শেষ পেজ ছোট হতে পারে। `scripts/build.sh` প্রতিবার নিজে থেকে `check_fill.py` চালায়;
কোনো পেজে `FAIL` এলে ফাইল ডেলিভারি হবে না (বিস্তারিত: `SKILL.md` §3.9)।
*ব্যতিক্রম: বুয়েট রিটেনের উত্তর লেখার ফাঁকা জায়গা (ইচ্ছাকৃত), স্লাইড, কভার পেজ।*

## 🔗 কিউআর নোটের জন্য যা লাগবে

১) YouTube ভিডিও লিংক ২) টাইমস্ট্যাম্পসহ ট্রান্সক্রিপ্ট (এজেন্ট নিজে আনতে না পারলে: ভিডিওর নিচে
`…more → Show transcript` → সব কপি) ৩) লেকচার স্লাইড।
ডেমোতে ভিডিও আইডি `XXXXXXXXXXX` প্লেসহোল্ডার — আসল কাজে আপনার ভিডিও আইডি বসবে।

## 🔤 ফন্ট

ডিফল্ট **Tiro Bangla** (বডি) + **Noto Serif Bengali Bold** (বোল্ড) + **Hind Siliguri** (হেডিং/স্লাইড)।
Noto Serif চাইলে: `\usepackage[notoserif]{edtech}` · ইংরেজি ও ম্যাথ: Times-ধাঁচের (TeX Gyre Termes)।

## 🏷️ লোগো / ব্র্যান্ড

এজেন্টকে আপনার লোগো (PNG, ট্রান্সপারেন্ট হলে ভালো) দিন আর বলুন কোথায় চান — হেডার, কভার ব্যানার,
স্লাইডের কোণে। কালো স্লাইডের জন্য সাদা/হালকা ভার্সন দিন। `assets/`-এর লোগোগুলো শুধু প্লেসহোল্ডার।

---

*Made for one-person Bangla edtech creators — একজন শিক্ষকই পুরো স্টুডিও।*
