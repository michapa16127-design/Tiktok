#!/usr/bin/env python3
"""Baut aus je zwei 9:16-Folien ein 15-s-Video mit Musik (ffmpeg nötig).

Nutzung: python3 make_slide_videos.py carousels_woche2.json
Die Folien müssen vorher mit make_carousels.py (--height 1920 --suffix _9x16) gerendert sein.
Musik: selbst erzeugte Ambient-Pads (music/ambient_*.m4a), reihum verwendet.
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
MUSIC = sorted((HERE / "music").glob("ambient_*.m4a"))


def main():
    data = json.loads((HERE / (sys.argv[1] if len(sys.argv) > 1 else "carousels_woche2.json")).read_text(encoding="utf-8"))
    for i, folder in enumerate(data):
        d = HERE / "posts" / f"{folder}_9x16"
        out = d / "zwei_folien_musik.mp4"
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error",
             "-loop", "1", "-t", "8", "-i", str(d / "folie-1.png"),
             "-loop", "1", "-t", "8", "-i", str(d / "folie-2.png"),
             "-i", str(MUSIC[i % len(MUSIC)]),
             "-filter_complex", "[0:v][1:v]xfade=transition=fade:duration=0.8:offset=7.2,format=yuv420p[v]",
             "-map", "[v]", "-map", "2:a", "-t", "15", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
             "-r", "30", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", str(out)],
            check=True)
        print("ok", out.relative_to(HERE))


if __name__ == "__main__":
    main()
