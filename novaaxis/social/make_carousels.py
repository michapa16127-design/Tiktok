#!/usr/bin/env python3
"""Rendert die Karussell-Folien aus carousels.json als 1080x1350 PNG.

Nutzung:  python3 make_carousels.py
Benötigt nur Python 3 und einen Chromium-/Chrome-Browser (Pfad via CHROME_BIN).
Texte ändern: carousels.json bearbeiten und das Skript erneut ausführen.
"""
import argparse
import html
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).parent
CHROME = os.environ.get("CHROME_BIN") or next(
    (p for p in (
        "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell",
        "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
        "google-chrome", "chromium", "chromium-browser",
    ) if os.path.exists(p) or subprocess.run(["which", p], capture_output=True).returncode == 0),
    None,
)

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:__H__px}
body{font-family:'Liberation Sans','Helvetica Neue',Arial,sans-serif;color:#fff;
 background:linear-gradient(160deg,#070d24 0%,#101c45 58%,#0b2a40 100%);position:relative;overflow:hidden}
.rings{position:absolute;right:-220px;top:-220px;width:760px;height:760px;opacity:.28}
.wrap{position:absolute;left:84px;right:84px;top:150px;bottom:190px;display:flex;flex-direction:column;justify-content:center}
.kicker{color:#e8b04a;font-weight:700;letter-spacing:.14em;font-size:36px;text-transform:uppercase;margin-bottom:34px}
.line{width:120px;height:6px;background:#e8b04a;border-radius:3px;margin-bottom:46px}
h1{font-size:92px;line-height:1.08;font-weight:800;letter-spacing:-.01em}
.cover h1{font-size:104px}
p{margin-top:48px;font-size:46px;line-height:1.38;color:#c9d6f2}
.cover p{color:#e8b04a;font-size:40px;letter-spacing:.06em}
.url{margin-top:56px;align-self:flex-start;background:#e8b04a;color:#0a1230;font-weight:800;
 font-size:70px;padding:22px 44px;border-radius:22px}
.hint{margin-top:30px;font-size:44px;color:#e8b04a;font-weight:700;letter-spacing:.04em}
.foot{position:absolute;left:84px;right:84px;bottom:70px;display:flex;justify-content:space-between;
 font-size:30px;letter-spacing:.2em;color:#7f93c4;font-weight:700}
"""

RINGS = """<svg class="rings" viewBox="0 0 200 200" fill="none" stroke="#5ad1c4" stroke-width=".6">
<circle cx="100" cy="100" r="95"/><circle cx="100" cy="100" r="70"/><circle cx="100" cy="100" r="45"/>
<path d="M100 5v190M5 100h190" stroke="#e8b04a"/></svg>"""


def slide_html(s, n, total):
    e = html.escape
    cls = "cover" if s["type"] == "cover" else ""
    body = f'<div class="kicker">{e(s["kicker"])}</div><div class="line"></div><h1>{e(s["title"])}</h1>'
    if s.get("text"):
        body += f'<p>{e(s["text"])}</p>'
    if s.get("url"):
        body += f'<div class="url">{e(s["url"])}</div>'
    if s.get("hint"):
        body += f'<div class="hint">{e(s["hint"])}</div>'
    return (f'<!doctype html><html lang="de"><head><meta charset="utf-8"><style>{CSS}</style></head>'
            f'<body class="{cls}">{RINGS}<div class="wrap {cls}">{body}</div>'
            f'<div class="foot"><span>NOVAAXIS</span><span>{n}/{total}</span></div></body></html>')


def main():
    global CSS
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="carousels.json", help="JSON mit den Folien")
    ap.add_argument("--out", default="posts", help="Ausgabeordner (relativ)")
    ap.add_argument("--height", type=int, default=1350, help="1350 = Karussell 4:5, 1920 = Reel 9:16")
    ap.add_argument("--suffix", default="", help="Suffix für den Unterordner, z. B. _9x16")
    a = ap.parse_args()
    if not CHROME:
        sys.exit("Kein Chrome/Chromium gefunden. Setze CHROME_BIN.")
    CSS = CSS.replace("__H__", str(a.height))
    data = json.loads((HERE / a.data).read_text(encoding="utf-8"))
    for folder, slides in data.items():
        out_dir = HERE / a.out / (folder + a.suffix)
        out_dir.mkdir(parents=True, exist_ok=True)
        for old in out_dir.glob("folie-*.png"):
            old.unlink()
        for i, s in enumerate(slides, 1):
            with tempfile.TemporaryDirectory() as tmp:
                page = Path(tmp) / "s.html"
                page.write_text(slide_html(s, i, len(slides)), encoding="utf-8")
                png = out_dir / f"folie-{i}.png"
                subprocess.run(
                    [CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                     f"--window-size=1080,{a.height}", f"--screenshot={png}", f"file://{page}"],
                    check=True, capture_output=True)
            print("ok", png.relative_to(HERE))


if __name__ == "__main__":
    main()
