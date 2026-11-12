#!/usr/bin/env python3
"""Macht aus einer Idee einen fertigen Post: 2 Folien (4:5 und 9:16), 15-s-Video mit Musik, POST.md.

Beispiel:
  python3 new_post.py --slug 18_thema --kicker "SONNTAGABEND" --title "Dein Körper spannt sich an." \
    --text "Atme länger aus, als du ein." --cta-title "Finde heraus, warum." \
    --caption "Ein Satz." --hashtags "#a #b #c #d #novaaxis"
"""
import argparse
import json
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).parent
MUSIC = sorted((HERE / "music").glob("ambient_*.m4a"))


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--slug", required=True)
    a.add_argument("--kicker", required=True)
    a.add_argument("--title", required=True)
    a.add_argument("--text", default="")
    a.add_argument("--cta-kicker", default="ANGST WANDELN IN VERTRAUEN")
    a.add_argument("--cta-title", required=True)
    a.add_argument("--cta-text", default="Kostenloser Test · 30 Fragen · 10 Min.")
    a.add_argument("--hint", default="↑ Link in der Bio")
    a.add_argument("--caption", required=True, help="ein bis zwei Sätze")
    a.add_argument("--hashtags", required=True)
    a.add_argument("--music", type=int, default=0, help="0=a, 1=b, 2=c")
    a = a.parse_args()
    slides = [
        {"type": "cover", "kicker": a.kicker, "title": a.title, "text": a.text},
        {"type": "cta", "kicker": a.cta_kicker, "title": a.cta_title, "text": a.cta_text,
         "url": "app.novaaxis.org", "hint": a.hint},
    ]
    with tempfile.TemporaryDirectory() as tmp:
        data = Path(tmp) / "one.json"
        data.write_text(json.dumps({a.slug: slides}, ensure_ascii=False), encoding="utf-8")
        for extra in ([], ["--height", "1920", "--suffix", "_9x16"]):
            subprocess.run(["python3", str(HERE / "make_carousels.py"), "--data", str(data), *extra],
                           check=True, cwd=HERE, capture_output=True)
    d = HERE / "posts" / f"{a.slug}_9x16"
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error",
         "-loop", "1", "-t", "8", "-i", str(d / "folie-1.png"),
         "-loop", "1", "-t", "8", "-i", str(d / "folie-2.png"),
         "-i", str(MUSIC[a.music % len(MUSIC)]),
         "-filter_complex", "[0:v][1:v]xfade=transition=fade:duration=0.8:offset=7.2,format=yuv420p[v]",
         "-map", "[v]", "-map", "2:a", "-t", "15", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-r", "30", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", str(d / "zwei_folien_musik.mp4")],
        check=True)
    tags4 = " ".join(a.hashtags.split()[:4])
    (HERE / "posts" / a.slug / "POST.md").write_text(
        f"# {a.slug}\n\nDateien: `posts/{a.slug}/folie-1.png`, `folie-2.png` · Video: `posts/{a.slug}_9x16/zwei_folien_musik.mp4`\n\n"
        f"## TikTok / Instagram\n```\n👉 Gratis-Test: app.novaaxis.org (Link in der Bio)\n{a.caption}\n"
        f"💾 Speichern · 💬 TEST schreiben = Link per Nachricht\n🔗 app.novaaxis.org\n{a.hashtags}\n```\n\n"
        f"## Facebook / LinkedIn (Link klickbar)\n```\n{a.caption} Kostenloser Test (30 Fragen, ca. 10 Minuten):\n"
        f"👉 https://app.novaaxis.org/\n{tags4}\n```\n", encoding="utf-8")
    print("fertig:", HERE / "posts" / a.slug)


if __name__ == "__main__":
    main()
