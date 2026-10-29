# Setup (do this once per machine)

## Linux (Debian/Ubuntu) and macOS
```bash
bash scripts/setup.sh
```
Installs TeX Live (XeLaTeX + packages), poppler (pdftoppm), ffmpeg, cairo/pango, zbar, the fonts
(Tiro Bangla, Hind Siliguri, Noto Serif/Sans Bengali) and a Python venv (`~/.edtech-venv`) with
manim, pyzbar, pypdf, qrcode, youtube-transcript-api, yt-dlp.

## Windows
1. **TeX Live** (recommended, full scheme) from tug.org/texlive — or MiKTeX with "install missing packages on the fly = yes".
2. **Fonts:** download & install (right-click → Install for all users):
   Tiro Bangla, Hind Siliguri (fonts.google.com), Noto Serif Bengali, Noto Sans Bengali (fonts.google.com/noto).
   TeX Gyre Termes / Termes Math and DejaVu come with TeX Live.
3. **Python 3.11+**, then `pip install manim pyzbar pypdf qrcode[pil] youtube-transcript-api yt-dlp`.
   Manim on Windows also needs ffmpeg on PATH (`winget install ffmpeg`).
4. **poppler** for previews: `winget install poppler` (gives `pdftoppm`). zbar for pyzbar: bundled wheel works on Windows.
5. Use Git-Bash/WSL to run `scripts/*.sh`, or run the equivalent commands by hand.

## Verify
```bash
xelatex --version | head -1
fc-list | grep -iE "Tiro Bangla|Hind Siliguri|Noto Serif Bengali"
kpsewhich qrcode.sty circuitikz.sty tcolorbox.sty siunitx.sty mhchem.sty
manim --version
```

## Compile
```bash
scripts/build.sh path/to/file.tex        # 2 XeLaTeX passes + <name>-preview-N.png (150 dpi)
scripts/build.sh path/to/file.tex 220    # sharper previews
```
`build.sh` sets `TEXINPUTS` so `\usepackage{edtech}` and `logo-placeholder.png` are found from any folder.
Without the script: `TEXINPUTS=<skill>/templates//:<skill>/assets//: xelatex file.tex` (run twice).

## Troubleshooting
| Symptom | Fix |
|---|---|
| `Missing character: There is no X in font …` | glyph not in that font. Latin/Bangla switching is automatic in body text; inside `\headfont`/slides use Hind Siliguri (has both). Symbols (★ ✓ ☐) → `{\symfont ★}` (DejaVu Sans). |
| Bangla conjuncts broken (ক্ষ, ন্ত্র) | font not loaded with `Script=Bengali`, or text pasted in ANSI (Bijoy). Re-type / convert to Unicode. |
| Bold Bangla looks thin | Tiro Bangla has no bold; edtech.sty maps bold to Noto Serif Bengali Bold — make sure it is installed. |
| `Font "Tiro Bangla" not found` | run `fc-cache -f`; on Windows install "for all users" and restart the TeX front-end. |
| Table rule gaps / content in wrong row | `\\` inside a `p{}` cell ends the row. Use `>{\raggedright}p{..}` (no `\arraybackslash`) and end rows with `\tabularnewline`, or wrap cell content in a minipage. |
| TikZ "A node must have a label text" with `rnd`/math in coordinates | wrap computed coordinates in braces: `({0.1+2*rnd},{(#2-0.2)*rnd})`. |
| Inner TikZ picture positioned wrongly inside a node | do not nest tikzpictures inside nodes; build the content in a `\savebox` first (see edtech-slides.sty). |
| Huge vertical gaps | a `twoside` document is `\flushbottom`; edtech.sty sets `\raggedbottom` — keep it. |
| QR prints but is not clickable | use `\ytqr` / `\urlqr` / `\linkbox` (dvipdfmx annotation); plain `\href{}{\qrcode..}` does not work in XeLaTeX. |
| Manim `Text` shows boxes | font name wrong → `fc-list | grep -i bengali`, use the exact family name. |
| Manim `Tex` with Bangla fails | use `BT()` from manim_bangla.py (XeLaTeX template, `.xdv` output). |
