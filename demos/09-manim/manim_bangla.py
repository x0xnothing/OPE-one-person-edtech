"""
manim_bangla.py — shared helpers for Bangla explainer videos (Manim Community >= 0.18)

    from manim_bangla import *          # put this file next to your scene file

Rules baked in:
  * black background, white text, one accent palette (COL)
  * Bangla prose  -> BN("...")          (Pango text shaping, Hind Siliguri / Tiro Bangla)
  * pure math     -> MT(r"...")         (MathTex, pdflatex, Latin Modern)
  * Bangla + math -> BT(r"... $x^2$ ...") (Tex compiled with XeLaTeX + fontspec Tiro Bangla)
  * safe layout   -> keep everything inside SAFE (no text touches the frame edge)
"""
from manim import *

config.background_color = BLACK

BN_FONT = "Hind Siliguri"        # clear on screen; alt: "Tiro Bangla", "Noto Sans Bengali"
BN_SERIF = "Tiro Bangla"

COL = dict(P=BLUE_C, Q=GREEN_C, R=YELLOW_C, hint=GREY_B, warn=RED_C, ok=TEAL_C)

# XeLaTeX template so Tex() can hold Bangla + math in one line
BN_TEX = TexTemplate(tex_compiler="xelatex", output_format=".xdv")
BN_TEX.add_to_preamble(r"""
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\setmainfont{Tiro Bangla}[Script=Bengali]
""")


def BN(text, size=36, color=WHITE, weight=NORMAL, font=BN_FONT, **kw):
    """Bangla text via Pango (correct conjuncts / matra shaping)."""
    return Text(text, font=font, font_size=size, color=color, weight=weight, **kw)


def MT(*tex, size=40, color=WHITE, **kw):
    return MathTex(*tex, font_size=size, color=color, **kw)


def BT(tex, size=36, color=WHITE, **kw):
    """Bangla + inline math in one object (XeLaTeX)."""
    return Tex(tex, tex_template=BN_TEX, font_size=size, color=color, **kw)


def title_card(scene, title, subtitle=None, hold=1.2):
    t = BN(title, size=60, weight=BOLD)
    grp = VGroup(t)
    if subtitle:
        s = BN(subtitle, size=34, color=COL["R"]).next_to(t, DOWN, buff=0.35)
        grp.add(s)
    scene.play(Write(t), run_time=1.2)
    if subtitle:
        scene.play(FadeIn(grp[1], shift=UP * 0.2))
    scene.wait(hold)
    scene.play(FadeOut(grp))


def caption(scene, text, old=None, size=30, color=WHITE):
    """Bottom subtitle line (teacher's voice). Replaces the previous caption."""
    c = BN(text, size=size, color=color).to_edge(DOWN, buff=0.45)
    if c.width > config.frame_width - 1:
        c.scale_to_fit_width(config.frame_width - 1)
    if old is None:
        scene.play(FadeIn(c, shift=UP * 0.15), run_time=0.5)
    else:
        scene.play(ReplacementTransform(old, c), run_time=0.5)
    return c


def labeled_vector(start, end, color, label_tex, label_dir=UP, size=40):
    v = Arrow(start, end, buff=0, color=color, stroke_width=6, max_tip_length_to_length_ratio=0.12)
    lab = MT(label_tex, size=size, color=color).next_to(v.get_center(), label_dir, buff=0.15)
    return v, lab
