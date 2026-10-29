#!/usr/bin/env bash
# One-time setup for Bangla EdTech Studio (Linux: Debian/Ubuntu, macOS: Homebrew).
# Windows: see references/setup.md (MiKTeX/TeX Live + fonts + Python).
set -euo pipefail
FONT_DIR="${FONT_DIR:-$HOME/.fonts}"; [ "$(uname)" = "Darwin" ] && FONT_DIR="$HOME/Library/Fonts"
mkdir -p "$FONT_DIR"

if command -v apt-get >/dev/null; then
  SUDO=""; [ "$(id -u)" -ne 0 ] && SUDO="sudo"
  $SUDO apt-get update -qq
  $SUDO DEBIAN_FRONTEND=noninteractive apt-get install -y -qq \
    texlive-xetex texlive-latex-extra texlive-pictures texlive-science texlive-fonts-extra \
    fonts-noto-core fonts-dejavu poppler-utils ffmpeg libcairo2-dev libpango1.0-dev pkg-config \
    libzbar0 python3-venv
elif command -v brew >/dev/null; then
  brew install --cask mactex-no-gui || true      # full TeX Live (XeLaTeX + all packages)
  brew install poppler ffmpeg pango cairo pkg-config zbar python
else
  echo "Install TeX Live (with XeLaTeX), poppler, ffmpeg, cairo/pango and zbar manually." >&2
fi

# Fonts (Google Fonts, OFL): Tiro Bangla (body), Hind Siliguri (headings/slides), Noto Serif/Sans Bengali
G=https://raw.githubusercontent.com/google/fonts/main/ofl
for f in tirobangla/TiroBangla-Regular.ttf tirobangla/TiroBangla-Italic.ttf \
         hindsiliguri/HindSiliguri-Regular.ttf hindsiliguri/HindSiliguri-SemiBold.ttf hindsiliguri/HindSiliguri-Bold.ttf; do
  [ -f "$FONT_DIR/$(basename "$f")" ] || curl -fsSL -o "$FONT_DIR/$(basename "$f")" "$G/$f"
done
N=https://raw.githubusercontent.com/notofonts/notofonts.github.io/main/fonts
for f in NotoSerifBengali/hinted/ttf/NotoSerifBengali-Regular.ttf NotoSerifBengali/hinted/ttf/NotoSerifBengali-Bold.ttf \
         NotoSansBengali/hinted/ttf/NotoSansBengali-Regular.ttf NotoSansBengali/hinted/ttf/NotoSansBengali-Bold.ttf; do
  [ -f "$FONT_DIR/$(basename "$f")" ] || fc-list | grep -q "$(basename "$f" .ttf)" || curl -fsSL -o "$FONT_DIR/$(basename "$f")" "$N/$f" || true
done
command -v fc-cache >/dev/null && fc-cache -f >/dev/null

# Python tools in an isolated venv
VENV="${VENV:-$HOME/.edtech-venv}"
python3 -m venv "$VENV"
"$VENV/bin/pip" install -q -U pip setuptools wheel
"$VENV/bin/pip" install -q manim qrcode[pil] pyzbar pypdf pillow youtube-transcript-api yt-dlp
echo
echo "Done. Check:"
echo "  xelatex --version | head -1"
echo "  fc-list | grep -iE 'Tiro Bangla|Hind Siliguri|Noto Serif Bengali'"
echo "  $VENV/bin/manim --version"
