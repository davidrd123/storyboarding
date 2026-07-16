"""Risograph type-asset generator.

Renders glyph-perfect black-on-transparent PNGs (straight lines + circular halo
arcs) for import into the single-color riso layout tool. Pillow draws the type so
Latin strings stay correct (NB2 garbles them); the tool then tints + halftones
each PNG as its own spot-ink layer.

Run:
    uv run --with pillow python scripts/riso_type.py

Output: risograph/type-assets/*.png  (RGBA, black text, transparent ground,
autocropped + small pad). Halo rings come as top-arc, bottom-arc, and combined.
"""
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent.parent / "risograph" / "type-assets"
OUT.mkdir(parents=True, exist_ok=True)

FONTS = {
    "herc": "/System/Library/Fonts/Supplemental/Herculanum.ttf",          # carved Roman caps
    "copper": "/System/Library/Fonts/Supplemental/Copperplate.ttc",       # engraver's caps
    "bodoni": "/System/Library/Fonts/Supplemental/Bodoni 72.ttc",         # high-contrast display
    "caslon": "/System/Library/Fonts/Supplemental/BigCaslon.ttf",         # elegant serif
    "arialblack": "/System/Library/Fonts/Supplemental/Arial Black.ttf",   # heavy sans (VS)
    "didot": "/System/Library/Fonts/Supplemental/Didot.ttc",
}
BLACK = (0, 0, 0, 255)
PAD = 24


def load(font_key: str, size: int) -> ImageFont.FreeTypeFont:
    path = FONTS[font_key]
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.truetype(path, size, index=0)


def autocrop(img: Image.Image, pad: int = PAD) -> Image.Image:
    bbox = img.getbbox()
    if not bbox:
        return img
    l, t, r, b = bbox
    l, t = max(0, l - pad), max(0, t - pad)
    r, b = min(img.width, r + pad), min(img.height, b + pad)
    return img.crop((l, t, r, b))


def render_line(text: str, font_key: str, size: int, tracking: int = 0,
                name: str = "line") -> Path:
    """Straight letterspaced line, black on transparent."""
    font = load(font_key, size)
    # measure with tracking
    widths = [font.getlength(ch) for ch in text]
    total_w = int(sum(widths) + tracking * (len(text) - 1)) + 4 * PAD
    ascent, descent = font.getmetrics()
    total_h = ascent + descent + 4 * PAD
    img = Image.new("RGBA", (total_w, total_h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    x = 2 * PAD
    y = 2 * PAD
    for ch, w in zip(text, widths):
        d.text((x, y), ch, font=font, fill=BLACK)
        x += w + tracking
    out = autocrop(img)
    p = OUT / f"{name}.png"
    out.save(p)
    return p


def _glyph_tile(ch: str, font: ImageFont.FreeTypeFont) -> Image.Image:
    bbox = font.getbbox(ch)
    x0, y0, x1, y1 = bbox
    w, h = max(1, x1 - x0), max(1, y1 - y0)
    tile = Image.new("RGBA", (w + 8, h + 8), (0, 0, 0, 0))
    ImageDraw.Draw(tile).text((4 - x0, 4 - y0), ch, font=font, fill=BLACK)
    return tile


def _draw_arc(img: Image.Image, cx: float, cy: float, radius: int,
              text: str, font: ImageFont.FreeTypeFont,
              *, bottom: bool, tracking: float) -> None:
    """Composite `text` onto `img` along a circular arc centered at top/bottom.

    Letters read L->R either way. Top: tops radiate outward. Bottom: tops point
    inward (toward center) so the word stays upright/readable along the bottom.
    Angle is measured clockwise from 12 o'clock; x = cx + R*sin, y = cy - R*cos.
    """
    advances = [font.getlength(ch) * tracking for ch in text]
    span = sum(advances) / radius  # radians subtended
    if bottom:
        start, step = math.pi + span / 2.0, -1.0   # begin lower-left, sweep right
    else:
        start, step = -span / 2.0, 1.0             # begin upper-left, sweep right
    cum = 0.0
    for ch, adv in zip(text, advances):
        ang = start + step * (cum + adv / 2.0) / radius
        x = cx + radius * math.sin(ang)
        y = cy - radius * math.cos(ang)
        tile = _glyph_tile(ch, font)
        deg = math.degrees(ang)
        rt = tile.rotate((-deg + 180.0) if bottom else (-deg),
                         expand=True, resample=Image.BICUBIC)
        img.alpha_composite(rt, (int(x - rt.width / 2), int(y - rt.height / 2)))
        cum += adv


def render_arc(text: str, font_key: str, size: int, radius: int,
               *, bottom: bool = False, tracking: float = 1.18,
               name: str = "arc") -> Path:
    """Single arc (top or bottom) on its own transparent canvas, autocropped."""
    font = load(font_key, size)
    canvas = 2 * (radius + size) + 4 * PAD
    cx = cy = canvas // 2
    img = Image.new("RGBA", (canvas, canvas), (0, 0, 0, 0))
    _draw_arc(img, cx, cy, radius, text, font, bottom=bottom, tracking=tracking)
    p = OUT / f"{name}.png"
    autocrop(img).save(p)
    return p


def render_ring(top_text: str, bottom_text: str, font_key: str, size: int,
                radius: int, *, tracking: float = 1.18, name: str = "ring") -> Path:
    """Full halo ring: top + bottom text drawn on one shared circle, open center."""
    font = load(font_key, size)
    canvas = 2 * (radius + size) + 4 * PAD
    cx = cy = canvas // 2
    img = Image.new("RGBA", (canvas, canvas), (0, 0, 0, 0))
    _draw_arc(img, cx, cy, radius, top_text, font, bottom=False, tracking=tracking)
    _draw_arc(img, cx, cy, radius, bottom_text, font, bottom=True, tracking=tracking)
    p = OUT / f"{name}.png"
    autocrop(img).save(p)
    return p


def main() -> None:
    made = []

    # --- straight display strings ---
    made.append(render_line("DOMINVS", "herc", 320, tracking=24, name="word_DOMINVS_herc"))
    made.append(render_line("DOMINVS", "copper", 300, tracking=40, name="word_DOMINVS_copper"))
    made.append(render_line("FIAT", "bodoni", 520, tracking=10, name="word_FIAT_bodoni"))
    made.append(render_line("FIAT", "herc", 460, tracking=30, name="word_FIAT_herc"))
    made.append(render_line("VS", "arialblack", 600, tracking=0, name="word_VS_arialblack"))
    made.append(render_line("VS", "bodoni", 620, tracking=0, name="word_VS_bodoni"))
    made.append(render_line("SANCTVS", "herc", 300, tracking=24, name="word_SANCTVS_herc"))
    made.append(render_line("ECCE", "herc", 360, tracking=28, name="word_ECCE_herc"))
    made.append(render_line("REX", "herc", 460, tracking=30, name="word_REX_herc"))

    # --- captions / banners ---
    made.append(render_line("REX · ET · REGINA", "copper", 150, tracking=14,
                            name="caption_REX_ET_REGINA"))
    made.append(render_line("ORA · PRO · NOBIS", "copper", 150, tracking=14,
                            name="caption_ORA_PRO_NOBIS"))
    made.append(render_line("MEMENTO · MORI", "copper", 150, tracking=14,
                            name="caption_MEMENTO_MORI"))

    # --- plate labels (contact-sheet) ---
    labels = [
        ("PL · I · REX", "label_01_REX"),
        ("PL · II · SANCTVS", "label_02_SANCTVS"),
        ("PL · III · ORA PRO NOBIS", "label_03_ORA"),
        ("PL · IV · MEMENTO MORI", "label_04_MEMENTO"),
        ("PL · V · CRVX SACRA", "label_05_CRVX"),
        ("PL · VI · LVX", "label_06_LVX"),
        ("PL · VII · DOMINVS", "label_07_DOMINVS"),
        ("PL · VIII · IN HOC", "label_08_INHOC"),
        ("PL · IX · SIGNO", "label_09_SIGNO"),
    ]
    for txt, nm in labels:
        made.append(render_line(txt, "copper", 90, tracking=8, name=nm))

    # --- halo rings ---
    made.append(render_arc("REX · REGVM", "herc", 150, 620, bottom=False,
                           name="halo_top_REX_REGVM"))
    made.append(render_arc("DOMINVS", "herc", 150, 620, bottom=True,
                           name="halo_bottom_DOMINVS"))
    made.append(render_arc("ORA PRO NOBIS", "herc", 130, 620, bottom=True,
                           name="halo_bottom_ORA_PRO_NOBIS"))
    # combined full ring (top + bottom) on one shared circle
    made.append(render_ring("REX · REGVM", "DOMINVS", "herc", 150, 620,
                            name="halo_ring_REX_REGVM_DOMINVS"))
    made.append(render_ring("SANCTVS", "DOMINVS", "herc", 150, 620,
                            name="halo_ring_SANCTVS_DOMINVS"))

    print(f"wrote {len(made)} assets to {OUT}")
    for p in made:
        im = Image.open(p)
        print(f"  {p.name:38s} {im.width}x{im.height}")


if __name__ == "__main__":
    main()
