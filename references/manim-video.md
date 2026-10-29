# Mode: manim (explainer video in Bangla)

Input: a topic name, a question (text/photo), or a concept the student is stuck on.
Output: `.mp4` 1920×1080, 30 fps, **black background**, Bangla captions/labels, LaTeX math, clean animated
diagrams that build the idea step by step; optional voice-over.

Demo: `demos/09-manim/vector_resultant.py` → `vector_resultant_1080p.mp4` (39 s).
Helpers: `templates/manim_bangla.py` (copy next to the scene file).

## 1. Plan before code — write `storyboard.md`
| # | time | what is on screen | caption (Bangla, ≤ 12 words) | math |
|---|------|-------------------|------------------------------|------|
Structure that works:
1. Title card (topic + one-line promise) — 2–3 s.
2. Intuition: draw the physical situation (objects, vectors, graph) before any formula.
3. Build the model: label quantities on the diagram, one at a time, same colours as in the math.
4. Derivation: 2–4 equation lines, `TransformMatchingTex` between steps, box the final result.
5. Worked example with numbers (if a question was given: read it → given data → solve → answer with unit).
6. "What if" with a `ValueTracker` (change angle/mass/length and watch the result update live).
7. Takeaway panel "মনে রাখো" with 2–4 bullets.
For a given **question**: show the question text first (BT/BN), extract "দেওয়া আছে" into a side panel,
draw the figure exactly as described, then solve step by step; end with `(Ans.)` and a sanity check.

## 2. Code rules
```python
from manim_bangla import *          # BLACK bg, BN(), MT(), BT(), caption(), title_card(), COL
class Scene1(Scene):
    def construct(self):
        title_card(self, "ভেক্টরের লব্ধি", "সামান্তরিক সূত্র")
        cap = caption(self, "একই বিন্দুতে দুটি ভেক্টর P ও Q")   # bottom caption, replace with caption(..., cap)
        eq  = MT(r"R=\sqrt{P^2+Q^2+2PQ\cos\theta}", color=COL["R"])
        mix = BT(r"লব্ধির মান $R=\sqrt{148}\approx 12.17$")       # Bangla + math in one line (XeLaTeX)
```
- Bangla prose → `BN()` (Pango shaping: conjuncts correct). Pure math → `MT()`. Mixed → `BT()`.
- Never put Bangla inside `MathTex` (pdflatex cannot shape it).
- Consistent colours: the same quantity has the same colour in diagram and equations (`COL` palette).
- Keep a 0.5-unit safe margin; check the extreme states of every `ValueTracker` (objects must stay in frame).
- Captions at the bottom, equations on the right, diagram on the left — never overlapping.
- Use `always_redraw` for geometry that depends on trackers; `Angle`, `DashedLine`, `Arrow(buff=0)`.
- Pacing: `self.wait(0.5–1.0)` after each new idea; total 30–120 s per concept.

## 3. Render & QA
```bash
manim -ql --fps 15 scene.py Scene1          # fast draft (480p) — check framing
# extract frames and LOOK at them:  ffmpeg -ss 12 -i media/videos/scene/480p15/Scene1.mp4 -frames:v 1 f12.png
manim -qh --fps 30 scene.py Scene1          # final 1080p30 → media/videos/scene/1080p30/Scene1.mp4
```
Check frames at every caption change and at tracker extremes: no clipped text, no overlaps, labels next to
the right objects, numbers correct.

## 4. Optional voice-over
If the user wants narration: write the script per storyboard row, generate Bangla TTS (e.g. `edge-tts
--voice bn-BD-NabanitaNeural` or the user's own recording), then either time animations with
`self.wait(duration)` per line or mux afterwards: `ffmpeg -i video.mp4 -i voice.mp3 -c:v copy -c:a aac -shortest out.mp4`.
