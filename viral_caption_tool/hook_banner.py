"""Renders the top 'hook headline' banner (white rounded box, bold black text)
that mirrors the reference clip's opening pattern-interrupt text."""
import textwrap

from PIL import Image, ImageDraw, ImageFont

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def _load_font(size: int) -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def render_hook_banner(
    text: str,
    video_w: int,
    out_path: str,
    max_width_ratio: float = 0.84,
    font_size: int | None = None,
    pad_x: int = 28,
    pad_y: int = 20,
    corner_radius: int = 22,
) -> str:
    """Draws a white rounded-rect banner with bold black wrapped text and
    saves it as a transparent PNG sized to fit the text. Returns out_path.
    """
    box_w = int(video_w * max_width_ratio)
    if font_size is None:
        font_size = int(video_w * 0.052)
    font = _load_font(font_size)

    # Wrap text to fit inside box_w (minus padding), by trial character count.
    tmp_img = Image.new("RGBA", (10, 10))
    tmp_draw = ImageDraw.Draw(tmp_img)
    avg_char_w = tmp_draw.textlength("Ag", font=font) / 2
    wrap_chars = max(10, int((box_w - 2 * pad_x) / max(avg_char_w, 1)))
    wrapped = textwrap.fill(text, width=wrap_chars)

    bbox = tmp_draw.multiline_textbbox((0, 0), wrapped, font=font, spacing=6, align="center")
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    box_w = int(text_w + 2 * pad_x)
    box_h = int(text_h + 2 * pad_y)

    img = Image.new("RGBA", (box_w, box_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle(
        [(0, 0), (box_w - 1, box_h - 1)],
        radius=corner_radius,
        fill=(255, 255, 255, 255),
    )
    draw.multiline_text(
        (box_w / 2 - bbox[0] - text_w / 2, box_h / 2 - bbox[1] - text_h / 2),
        wrapped,
        font=font,
        fill=(17, 17, 17, 255),
        align="center",
        spacing=6,
    )
    img.save(out_path)
    return out_path


def render_handle(
    handle: str,
    video_w: int,
    out_path: str,
    font_size: int | None = None,
) -> str:
    """Renders a small bold white '@handle' watermark with a soft shadow."""
    if font_size is None:
        font_size = int(video_w * 0.045)
    font = _load_font(font_size)
    tmp = Image.new("RGBA", (10, 10))
    d = ImageDraw.Draw(tmp)
    bbox = d.textbbox((0, 0), handle, font=font)
    w, h = int(bbox[2] - bbox[0] + 12), int(bbox[3] - bbox[1] + 12)
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
        draw.text((6 + dx - bbox[0], 6 + dy - bbox[1]), handle, font=font, fill=(0, 0, 0, 180))
    draw.text((6 - bbox[0], 6 - bbox[1]), handle, font=font, fill=(255, 255, 255, 255))
    img.save(out_path)
    return out_path
