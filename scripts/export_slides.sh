#!/usr/bin/env bash
# Export every slide of a 16:9 slide PDF to 1920x1080 PNGs (for OBS / video editors / smart boards)
# Usage: scripts/export_slides.sh slides.pdf [outdir]
set -euo pipefail
PDF="$1"; OUT="${2:-$(dirname "$PDF")/png}"; mkdir -p "$OUT"
pdftoppm -png -scale-to-x 1920 -scale-to-y 1080 "$PDF" "$OUT/$(basename "$PDF" .pdf)"
ls "$OUT"
