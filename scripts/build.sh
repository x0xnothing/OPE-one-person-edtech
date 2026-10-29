#!/usr/bin/env bash
# Usage: scripts/build.sh path/to/file.tex [dpi]
# Compiles with XeLaTeX (2 passes) and renders PNG previews (preview-1.png …) for visual QA.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEX="$1"; DPI="${2:-150}"
DIR="$(cd "$(dirname "$TEX")" && pwd)"; BASE="$(basename "$TEX" .tex)"
export TEXINPUTS="$HERE/templates//:$HERE/assets//:${TEXINPUTS:-}"
cd "$DIR"
for i in 1 2; do xelatex -interaction=nonstopmode -halt-on-error "$BASE.tex" > /dev/null || { grep -E "^!" -A4 "$BASE.log" | head -30; exit 1; }; done
grep -i "Missing character" "$BASE.log" | sort -u | head -5 || true
rm -f "$BASE"-preview-*.png preview-*.png; pdftoppm -r "$DPI" -png "$BASE.pdf" "$BASE-preview"
PYBIN="${EDTECH_PY:-$(command -v python3)}"; [ -x /opt/edvenv/bin/python ] && PYBIN=/opt/edvenv/bin/python; [ -x "$HOME/.edtech-venv/bin/python" ] && PYBIN="$HOME/.edtech-venv/bin/python"
"$PYBIN" "$HERE/scripts/check_fill.py" "$BASE.pdf" ${FILL_ALLOW:+--allow-pages "$FILL_ALLOW"} || echo "!! PAGE-FILL RULE BROKEN — fix before delivering (SKILL.md §3.9)"
echo "OK -> $DIR/$BASE.pdf ($(pdfinfo "$BASE.pdf" | awk '/Pages/{print $2}') pages)"
