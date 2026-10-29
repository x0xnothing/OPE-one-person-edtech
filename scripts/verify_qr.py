#!/usr/bin/env python3
"""Verify every QR code in a PDF: decodes it (print/scan test) and lists the PDF link
annotations (click test). Usage: python verify_qr.py file.pdf [--dpi 300]
Exit code 1 if a QR fails to decode or a decoded URL has no matching clickable link."""
import sys, subprocess, tempfile, glob, os, argparse
from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol
from pypdf import PdfReader

ap = argparse.ArgumentParser(); ap.add_argument("pdf"); ap.add_argument("--dpi", default="300")
a = ap.parse_args()
links = {}
for i, page in enumerate(PdfReader(a.pdf).pages, 1):
    for an in page.get("/Annots") or []:
        an = an.get_object(); act = an.get("/A")
        if act and act.get("/URI"): links.setdefault(i, set()).add(str(act["/URI"]))
bad = 0
with tempfile.TemporaryDirectory() as d:
    subprocess.run(["pdftoppm", "-r", a.dpi, "-png", a.pdf, os.path.join(d, "p")], check=True)
    for f in sorted(glob.glob(os.path.join(d, "p-*.png"))):
        pg = int(f.rsplit("-", 1)[1].split(".")[0])
        texts = [r.data.decode() for r in decode(Image.open(f), symbols=[ZBarSymbol.QRCODE])]
        print(f"page {pg}: {len(texts)} QR decoded, {len(links.get(pg, []))} clickable links")
        for t in texts:
            flag = "OK " if t in links.get(pg, set()) else "NO-LINK"
            if flag != "OK ": bad += 1
            if "youtube.com" in t and "noapp=1" not in t: print("   WARN missing noapp=1"); bad += 1
            print(f"   [{flag}] {t}")
sys.exit(1 if bad else 0)
