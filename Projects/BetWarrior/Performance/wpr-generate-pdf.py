#!/usr/bin/env python3
"""
WPR PDF Generator — screenshot approach
Captura cada página como PNG 1280x720 e combina em PDF landscape.
Uso: python3 wpr-generate-pdf.py [nome_saida.pdf]
"""

import subprocess, sys, os, tempfile
from PIL import Image

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE   = os.path.dirname(os.path.abspath(__file__))

PAGES = [
    ("capa",  os.path.join(BASE, "wpr-cover.html")),
    ("p1p2",  os.path.join(BASE, "weekly-report-slide.html")),
    ("p3",    os.path.join(BASE, "weekly-report-slide-p3.html")),
]

def screenshot(html_path, png_path):
    cmd = [
        CHROME,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--hide-scrollbars",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=5000",
        "--window-size=1280,720",
        f"--screenshot={png_path}",
        f"file://{html_path}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if not os.path.exists(png_path):
        print(f"  ERRO: {result.stderr[-300:]}")
        return False
    size_kb = os.path.getsize(png_path) // 1024
    print(f"  OK — {size_kb}KB")
    return True

def pngs_to_pdf(png_paths, output_path):
    images = []
    for p in png_paths:
        img = Image.open(p).convert("RGB")
        images.append(img)

    if not images:
        print("Nenhuma imagem para combinar.")
        return

    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:],
        resolution=144,
    )
    size_kb = os.path.getsize(output_path) // 1024
    print(f"\nPDF final: {output_path}")
    print(f"  {len(images)} páginas · {size_kb}KB")

def main():
    output_name = sys.argv[1] if len(sys.argv) > 1 else "WPR_Brasil_Mai01-07_2026.pdf"
    output_path = os.path.join(BASE, "Entregas", output_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        pngs = []
        for label, html_path in PAGES:
            print(f"Capturando {label}...")
            png_path = os.path.join(tmp, f"{label}.png")
            if screenshot(html_path, png_path):
                pngs.append(png_path)

        if len(pngs) == len(PAGES):
            pngs_to_pdf(pngs, output_path)
            os.system(f'open "{output_path}"')
        else:
            print("Falha — nem todas as páginas foram capturadas.")
            sys.exit(1)

if __name__ == "__main__":
    main()
