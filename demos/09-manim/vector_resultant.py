"""
Demo: ভেক্টরের লব্ধি — সামান্তরিক সূত্র   (HSC Physics 1st Paper, Chapter 2)
Render:  manim -qh --fps 30 vector_resultant.py VectorResultant
"""
from manim_bangla import *
import numpy as np


class VectorResultant(Scene):
    def construct(self):
        title_card(self, "ভেক্টরের লব্ধি", "সামান্তরিক সূত্র", hold=0.8)

        # ---------- geometry (P along x-axis, Q at angle theta) ----------
        O = np.array([-4.3, -1.6, 0])
        s = 0.42                      # 1 unit = 0.42 scene units  (P=6, Q=8)
        P, Q = 6, 8
        theta = ValueTracker(60)

        def q_end():
            t = np.deg2rad(theta.get_value())
            return O + s * Q * np.array([np.cos(t), np.sin(t), 0])

        p_end = O + s * P * RIGHT
        vP = Arrow(O, p_end, buff=0, color=COL["P"], stroke_width=6)
        lP = MT(r"\vec P", color=COL["P"]).next_to(vP, DOWN, buff=0.15)
        vQ = always_redraw(lambda: Arrow(O, q_end(), buff=0, color=COL["Q"], stroke_width=6))
        lQ = always_redraw(lambda: MT(r"\vec Q", color=COL["Q"]).next_to(
            (O + q_end()) / 2, LEFT, buff=0.2))
        arc = always_redraw(lambda: Angle(Line(O, p_end), Line(O, q_end()), radius=0.6, color=WHITE))
        lth = always_redraw(lambda: MT(r"\theta", size=34).move_to(
            O + 0.95 * np.array([np.cos(np.deg2rad(theta.get_value() / 2)),
                                 np.sin(np.deg2rad(theta.get_value() / 2)), 0])))

        cap = caption(self, "একই বিন্দুতে দুটি ভেক্টর P ও Q, মাঝের কোণ θ")
        self.play(GrowArrow(vP), Write(lP))
        self.play(GrowArrow(vQ), Write(lQ))
        self.play(Create(arc), Write(lth))
        self.wait(0.5)

        # ---------- parallelogram + resultant ----------
        cap = caption(self, "সামান্তরিক সম্পূর্ণ করি — কর্ণটিই লব্ধি R", cap)
        d1 = always_redraw(lambda: DashedLine(p_end, p_end + (q_end() - O), color=COL["Q"]))
        d2 = always_redraw(lambda: DashedLine(q_end(), p_end + (q_end() - O), color=COL["P"]))
        self.play(Create(d1), Create(d2))
        vR = always_redraw(lambda: Arrow(O, p_end + (q_end() - O), buff=0, color=COL["R"], stroke_width=7))
        lR = always_redraw(lambda: MT(r"\vec R", color=COL["R"]).next_to(
            (O + p_end + (q_end() - O)) / 2, UP + LEFT * 0.2, buff=0.1))
        self.play(GrowArrow(vR), Write(lR))
        self.wait(0.6)

        # ---------- components of Q ----------
        cap = caption(self, "Q কে ভাঙি: P বরাবর Q cosθ, লম্বভাবে Q sinθ", cap)
        tip = p_end + (q_end() - O)
        foot = np.array([tip[0], O[1], 0])
        ext = DashedLine(p_end, foot, color=GREY_B)
        perp = DashedLine(tip, foot, color=GREY_B)
        lc = MT(r"Q\cos\theta", size=30, color=GREY_A).next_to(ext, DOWN, buff=0.12)
        ls = MT(r"Q\sin\theta", size=30, color=GREY_A).next_to(perp, RIGHT, buff=0.12)
        self.play(Create(ext), Create(perp), FadeIn(lc), FadeIn(ls))
        self.wait(0.4)

        # ---------- derivation on the right ----------
        cap = caption(self, "পিথাগোরাসের উপপাদ্য থেকে লব্ধির মান", cap)
        eq1 = MT(r"R^2=(P+Q\cos\theta)^2+(Q\sin\theta)^2", size=34)
        eq2 = MT(r"R=\sqrt{P^2+Q^2+2PQ\cos\theta}", size=40, color=COL["R"])
        eq3 = MT(r"\tan\alpha=\frac{Q\sin\theta}{P+Q\cos\theta}", size=36)
        col = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.45, aligned_edge=LEFT).to_edge(RIGHT, buff=0.5).shift(UP * 1.2)
        self.play(Write(eq1))
        self.play(TransformMatchingShapes(eq1.copy(), eq2))
        box = SurroundingRectangle(eq2, color=COL["R"], buff=0.15)
        self.play(Create(box), Write(eq3))
        self.wait(0.8)

        # ---------- numeric example ----------
        cap = caption(self, "উদাহরণ: P = 6, Q = 8, θ = 60°", cap)
        ex = VGroup(
            MT(r"R=\sqrt{36+64+2\cdot6\cdot8\cdot\tfrac12}=\sqrt{148}", size=32),
            MT(r"R\approx 12.17\ \text{unit}", size=36, color=COL["R"]),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).next_to(col, DOWN, buff=0.6, aligned_edge=LEFT)
        self.play(Write(ex[0]))
        self.play(Write(ex[1]))
        self.wait(1.0)

        # ---------- live: theta changes, R changes ----------
        self.play(FadeOut(VGroup(ext, perp, lc, ls, ex)))
        cap = caption(self, "θ বাড়লে লব্ধি ছোট হয়, θ কমলে বড় হয়", cap, color=COL["R"])
        rval = always_redraw(lambda: VGroup(
            MT(r"\theta=", size=36), DecimalNumber(theta.get_value(), num_decimal_places=0, font_size=36),
            MT(r"^\circ\quad R=", size=36),
            DecimalNumber(np.sqrt(P**2 + Q**2 + 2*P*Q*np.cos(np.deg2rad(theta.get_value()))),
                          num_decimal_places=2, font_size=36, color=COL["R"]),
        ).arrange(RIGHT, buff=0.1).next_to(col, DOWN, buff=0.7, aligned_edge=LEFT))
        self.add(rval)
        self.play(theta.animate.set_value(140), run_time=3, rate_func=smooth)
        self.play(theta.animate.set_value(10), run_time=3, rate_func=smooth)
        self.play(theta.animate.set_value(60), run_time=1.5)
        self.wait(0.5)

        # ---------- takeaway ----------
        self.play(FadeOut(cap))
        take = VGroup(
            BN("মনে রাখো", size=34, color=COL["R"], weight=BOLD),
            MT(r"\theta=0^\circ\Rightarrow R_{\max}=P+Q", size=34),
            MT(r"\theta=180^\circ\Rightarrow R_{\min}=|P-Q|", size=34),
            MT(r"\theta=90^\circ\Rightarrow R=\sqrt{P^2+Q^2}", size=34),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        panel = SurroundingRectangle(take, color=WHITE, buff=0.3, corner_radius=0.15)
        g = VGroup(panel, take).to_edge(DOWN, buff=0.3).to_edge(RIGHT, buff=0.5)
        target = VGroup(eq2, box).copy().next_to(g, UP, buff=0.35).align_to(g, RIGHT)
        self.play(FadeOut(VGroup(eq1, eq3, rval)), VGroup(eq2, box).animate.move_to(target))
        self.play(Create(panel), LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in take], lag_ratio=0.25))
        self.wait(2)
