#!/usr/bin/env python3
"""make_viral_clip.py

Recreates the production style analyzed from the reference TikTok clip:
  - a white "pattern interrupt" hook banner pinned near the top
  - bold word-by-word animated captions (white text, heavy black outline)
    synced to speech, in the lower-middle third of the frame
  - an optional bold creator-handle watermark

Usage:
    python3 make_viral_clip.py \\
        --video input.mp4 \\
        --srt script.srt \\
        --hook "23-Jähriger kündigt seinen Job wegen Mini-AI Aufgaben (789€ pro Tag)" \\
        --handle "@dein.handle" \\
        --out output.mp4

The --srt file can be phrase-level (normal subtitles) or word-level; phrase
cues are automatically split into per-word timing. Use --chunk 2 to show
two words at a time instead of one.
"""
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from build_ass import build_ass
from hook_banner import render_handle, render_hook_banner
from srt_utils import cues_to_words, group_words, parse_srt

HERE = Path(__file__).resolve().parent


def probe_dimensions(video_path: str) -> tuple[int, int]:
    out = subprocess.run(
        [
            "ffprobe",
            "-v", "error",
            "-select_streams", "v:0",
            "-show_entries", "stream=width,height",
            "-of", "json",
            video_path,
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    data = json.loads(out.stdout)
    stream = data["streams"][0]
    return int(stream["width"]), int(stream["height"])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--video", required=True, help="Input talking-head video")
    ap.add_argument("--srt", required=True, help="Subtitle file (.srt) with the spoken script")
    ap.add_argument("--hook", required=True, help="Hook headline text for the top banner")
    ap.add_argument("--handle", default=None, help="Optional '@handle' watermark, bottom-left")
    ap.add_argument("--chunk", type=int, default=1, help="Words shown per caption (default: 1)")
    ap.add_argument("--hook-y-ratio", type=float, default=0.17, help="Vertical position of the hook banner (0-1)")
    ap.add_argument("--out", required=True, help="Output video path")
    args = ap.parse_args()

    if shutil.which("ffmpeg") is None:
        sys.exit("ffmpeg not found on PATH")

    video_w, video_h = probe_dimensions(args.video)

    cues = parse_srt(args.srt)
    if not cues:
        sys.exit(f"No subtitle cues found in {args.srt}")
    words = group_words(cues_to_words(cues), chunk_size=args.chunk)

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        ass_path = tmp / "captions.ass"
        ass_path.write_text(build_ass(words, video_w, video_h))

        banner_path = render_hook_banner(args.hook, video_w, str(tmp / "hook.png"))
        hook_y = int(video_h * args.hook_y_ratio)

        filter_parts = [f"[0:v][1:v]overlay=(W-w)/2:{hook_y}[v1]"]
        inputs = ["-i", args.video, "-i", banner_path]
        last_label = "v1"

        if args.handle:
            handle_path = render_handle(args.handle, video_w, str(tmp / "handle.png"))
            inputs += ["-i", handle_path]
            margin = int(video_w * 0.045)
            filter_parts.append(f"[{last_label}][2:v]overlay={margin}:H-h-{margin}[v2]")
            last_label = "v2"

        ass_escaped = str(ass_path).replace("\\", "/").replace(":", "\\:")
        filter_parts.append(f"[{last_label}]ass='{ass_escaped}'[vout]")

        filter_complex = ";".join(filter_parts)

        cmd = [
            "ffmpeg", "-y",
            *inputs,
            "-filter_complex", filter_complex,
            "-map", "[vout]",
            "-map", "0:a?",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20",
            "-c:a", "aac", "-b:a", "160k",
            args.out,
        ]
        subprocess.run(cmd, check=True)

    print(f"Fertig: {args.out}")


if __name__ == "__main__":
    main()
