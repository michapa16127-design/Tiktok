"""Builds an .ass subtitle file in the bold word-by-word 'viral caption' style."""
from srt_utils import Word


def _ts(t: float) -> str:
    t = max(t, 0.0)
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    cs = int(round((t - int(t)) * 100))
    return f"{h:d}:{m:02d}:{s:02d}.{cs:02d}"


def build_ass(
    words: list[Word],
    video_w: int,
    video_h: int,
    font_name: str = "Liberation Sans",
    font_size: int | None = None,
    margin_v_ratio: float = 0.37,
    fill_color: str = "&H00FFFFFF",  # white text
    outline_color: str = "&H00000000",  # black outline
    outline_width: float | None = None,
) -> str:
    """Returns the full contents of an .ass file.

    Layout mirrors the analyzed reference clip: one (or two) bold words at
    a time, centered, positioned in the lower-middle third of the frame,
    white fill with a heavy black outline so it reads over any background.
    """
    if font_size is None:
        font_size = int(video_w * 0.095)
    if outline_width is None:
        outline_width = max(2, int(font_size * 0.09))
    margin_v = int(video_h * margin_v_ratio)

    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {video_w}
PlayResY: {video_h}
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.601

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Word,{font_name},{font_size},{fill_color},&H000000FF,{outline_color},&H00000000,-1,0,0,0,100,100,0,0,1,{outline_width},0,2,40,40,{margin_v},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    for w in words:
        text = w.text.upper().replace("\n", " ")
        lines.append(
            f"Dialogue: 0,{_ts(w.start)},{_ts(w.end)},Word,,0,0,0,,{text}"
        )
    return header + "\n".join(lines) + "\n"
