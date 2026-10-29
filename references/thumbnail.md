# Mode: thumbnail (prompt pack for an image-generation model)

The agent does **not** draw the thumbnail; it produces a precise, copy-paste prompt (plus an optional
layout-guide PNG) that the user pastes into an image model together with **their own photo and logo**.

Demo: `demos/11-thumbnail/thumbnail-prompts.md`, `layout-1-one-shot.png`, `layout-2-exam-alert.png`.

## 1. Style system distilled from the references (IMG_9427, IMG_9428)
Common anatomy (16:9, 1280×720):
- **Person cut-out** occupies 35–42 % on one side (left or right), waist/chest-up, looking toward the text
  or at camera, often pointing/arms crossed; white 4–8 px outline + glow/rim light; never covered by text.
- **Text block** on the other side, left-aligned, 3–4 lines max: small pill tag (class/subject) →
  HUGE topic word(s) in heavy Bangla display type with 3D extrude/thick black stroke → secondary line →
  ribbon/banner ("ONE SHOT CLASS", "বোর্ড প্রশ্ন সলভ").
- **Badges/stickers:** class tag top-right/left ("SSC-25", "HSC ICT", "Chapter-3"), circular red stamp
  ("১০০% কমন"), tiny emoji/icons (🔥 ✅ ⚠️), teacher name card at the bottom of the person.
- **Logo** small in a top corner. **Colour:** one dominant gradient + one accent (yellow/red), high contrast.
- Typography: Bangla bold display (Li Ador Noirrit, Hind Siliguri Bold, Kalpurush-style), white or yellow
  fill, 6–10 px black stroke, slight perspective; English words in a heavy grotesk (Anton/Montserrat Black).

Themes (pick by video type):
| Theme | When | Palette | Signature elements |
|---|---|---|---|
| T1 One-Shot Chapter | full chapter class | emerald→black or royal-blue→navy | subject doodles 8 %, ONE SHOT ribbon, ১০০% কমন stamp |
| T2 Exam Alert | last-minute, suggestion, mistakes | dark red→black + yellow | angled stripes, warning icons, "মিস করলে চলবে না!" |
| T3 Course / Announcement | batch launch, routine, update | deep navy + cyan glow | glass cards, "বিস্তারিত ডিটেইলস", date chip |
| T4 Motivation / Tips | study tips, routine, mindset | black + gold/yellow | "TOP 6 TIPS" numerals, spotlight, serious face |
| T5 Clean Brand | language/pedagogy, premium courses | white/pink-red or white/blue | flat shapes, two-line headline, teacher name strip |
| T6 Problem-Solve | MCQ/CQ solve, board question | purple→magenta or green | big "CQ SOLVING" stamp, question-mark icons |

## 2. Intake form (ask the user to fill; defaults in brackets)
```
১. ক্লাস/পরীক্ষা: (SSC 26 / HSC 27 / Admission)
২. বিষয় + অধ্যায়/টপিক:
৩. ভিডিওর ধরন: one-shot / exam alert / CQ-MCQ solve / course announcement / tips / অন্যান্য
৪. মূল হেডলাইন (২–৪ শব্দ): [agent suggests 3 options]
৫. সাব-লাইন / রিবন টেক্সট: [agent suggests]
৬. ব্যাজ/স্ট্যাম্প: (১০০% কমন / ONE SHOT / NEW / Part-1 …)
৭. শিক্ষকের নাম ও পদবি (ঐচ্ছিক):
৮. ছবি: attached? পোজ (arms crossed / pointing / thinking / surprised) [arms crossed]
৯. লোগো: attached? কোন কোণে [top-left]
১০. রং/থিম পছন্দ: [theme from table]
১১. যে মডেল ব্যবহার করবে: GPT-Image / Gemini / Ideogram / Midjourney / Flux [GPT-Image]
```

## 3. Prompt template (fill every {…}; keep section order)
```
Create a YouTube thumbnail, 16:9, 1280x720, ultra sharp, high contrast, Bangladeshi EdTech style.

SUBJECT: Use the attached person photo exactly (same face, same clothes, no beautification, no face change).
Place the person as a clean cut-out on the {LEFT|RIGHT} {38}% of the frame, {waist-up}, {pose}, {expression}.
Add a thin white rim-light outline ({6}px) and a soft shadow.

BACKGROUND: {palette gradient with hex}, {theme signature elements}, subtle {subject} doodles at 8% opacity,
no clutter behind the face.

TEXT BLOCK ({opposite side} {58}%, vertically centred, left aligned, 6% safe margin):
  tag (pill, {colours}): "{tag}"
  line 1 ({size/style}): "{headline 1}"
  line 2 ({size/style}): "{headline 2}"
  ribbon ({colours}, slight tilt): "{ribbon}"
  stamp ({colours}): "{stamp}"
TOP-{LEFT}: the attached logo, small (≈9% of frame height), 4% margin.
{optional: name card under the person: "{name}" + "{designation}"}

TYPOGRAPHY: heavy Bangla display face (like Li Ador Noirrit Bold / Hind Siliguri Bold), perfect Bangla
conjuncts, max 3 sizes, readable at 160px width.

TEXT LOCK — render these strings EXACTLY, character by character, nothing else:
"{s1}" | "{s2}" | …

AVOID: extra words, fake logos, watermarks, misspelled Bangla, distorted hands/face, text over the face,
more than 2 accent colours, low contrast, small text.
```
Always also output the **clean-plate variant** (same scene, the text area left empty, "Do not render any
letters") because many models still break Bangla glyphs; the user then types the TEXT LOCK strings in
Canva/Photoshop. Optionally render a layout-guide PNG (zones + text) with PIL to attach as a composition
reference: `python scripts/thumbnail_layout.py spec.json layout.png`.

## 4. Model-specific tips
- GPT-Image / Gemini: attach photo + logo, paste prompt as-is; ask for 2–3 variations.
- Ideogram: best at text; set "Magic prompt: off", aspect 16:9; include TEXT LOCK.
- Midjourney/Flux: use `--ar 16:9 --style raw`; use the photo as an image/character reference; prefer the clean-plate variant.
- Headline ≤ 4 words, one idea; numbers in Bangla digits unless the brand uses Latin ("SSC-26").
