#!/usr/bin/env python3
"""
Render a 1280x720 LAYOUT GUIDE (wireframe) for a thumbnail prompt — attach it to the image model as a
composition reference. It is not the final art.

Usage:  python thumbnail_layout.py spec.json out.png
spec.json example:
{
  "person_side": "right", "bg": "#08462C",
  "tag": "পদার্থবিজ্ঞান ১ম পত্র",
  "lines": [["আদর্শ গ্যাস", 104, "#FFD60A"], ["ও গ্যাসের গতিতত্ত্ব", 66, "#FFFFFF"]],
  "ribbon": "ONE SHOT CLASS", "stamp": "১০০% কমন"
}
Needs a Bangla-capable font with Raqm shaping in Pillow (Hind Siliguri is used if installed).
"""
import json, sys, os
from PIL import Image, ImageDraw, ImageFont

CANDIDATES = [os.path.expanduser("~/.fonts/HindSiliguri-Bold.ttf"),
              os.path.expanduser("~/Library/Fonts/HindSiliguri-Bold.ttf"),
              "C:/Windows/Fonts/HindSiliguri-Bold.ttf",
              "/usr/share/fonts/truetype/noto/NotoSansBengali-Bold.ttf"]
FONT = next((p for p in CANDIDATES if os.path.exists(p)), None)


def F(size):
    return ImageFont.truetype(FONT, size) if FONT else ImageFont.load_default()


def hexrgb(h):
    h = h.lstrip("#"); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def main(spec, out):
    s = json.load(open(spec, encoding="utf-8"))
    W, H = 1280, 720
    bg = hexrgb(s.get("bg", "#101010"))
    im = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(im)
    right = s.get("person_side", "right") == "right"
    box = (760, 110, 1220, 720) if right else (60, 120, 520, 720)
    d.rounded_rectangle(box, radius=30, outline="white", width=4)
    d.text(((box[0] + box[2]) // 2, (box[1] + box[3]) // 2), "PERSON\nCUT-OUT", font=F(40), fill="white", anchor="mm", align="center")
    d.rounded_rectangle((40, 30, 200, 90), radius=10, outline="white", width=3)
    d.text((120, 60), "LOGO", font=F(28), fill="white", anchor="mm")
    x0, y = (70 if right else 560), 150
    if s.get("tag"):
        tb = d.textbbox((0, 0), s["tag"], font=F(34))
        d.rounded_rectangle((x0, y, x0 + tb[2] + 40, y + 56), radius=28, fill=(227, 38, 46))
        d.text((x0 + 20, y + 28), s["tag"], font=F(34), fill="white", anchor="lm"); y += 80
    for txt, size, col in s.get("lines", []):
        d.text((x0, y), txt, font=F(size), fill=hexrgb(col), stroke_width=6, stroke_fill="black"); y += int(size * 1.18)
    if s.get("ribbon"):
        tb = d.textbbox((0, 0), s["ribbon"], font=F(38))
        d.rectangle((x0, y + 10, x0 + tb[2] + 40, y + 70), fill=(255, 214, 10))
        d.text((x0 + 20, y + 40), s["ribbon"], font=F(38), fill="black", anchor="lm")
    if s.get("stamp"):
        cx, cy = x0 + 520, y + 170
        d.ellipse((cx - 80, cy - 80, cx + 80, cy + 80), outline=(227, 38, 46), width=8)
        d.text((cx, cy), s["stamp"], font=F(30), fill=(227, 38, 46), anchor="mm")
    d.text((W - 20, H - 14), "layout guide — not final art", font=F(20), fill=(200, 200, 200), anchor="rs")
    im.save(out); print("wrote", out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
