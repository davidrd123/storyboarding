"""litho_post.py — add stone-lithograph facture to a clean NB2 litho render.

NB2 nails the litho *category* (palette, layout, print-object) fast but cannot
*generate* the crayon facture: paper grain sits passively on top instead of
breaking the ink (style-control-probe finding, 2026-05-23). This pass does in
compositing what the model structurally won't:

  1. ink-starvation — knock cream-paper speckle THROUGH the dark fills, denser
     where ink is heaviest (prob ~ darkness**1.5 * starve, gated by a noise
     field). This is the hardest-to-fake signature per Gemini.
  2. paper tooth — multiply a fine grain over everything for matte texture.
  3. loose registration — small per-channel horizontal offsets to mimic
     multi-stone misregistration / color fringe.

Deterministic given --seed, so the SAME grain applies identically across an
entire storyboard — the consistency win over per-frame GPT-Image-2 facture.

    uv run --with pillow --with numpy python scripts/litho_post.py \
        --in  path/to/clean.png --out path/to/textured.png \
        [--paper 235,223,198] [--starve 0.40] [--tooth 0.12] [--reg 2] [--seed 7]
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image


def _octave(rng: np.random.Generator, h: int, w: int, factor: int) -> np.ndarray:
    """One octave of value noise at 1/factor resolution, bilinear-upsampled."""
    small = rng.random((max(1, h // factor), max(1, w // factor))).astype(np.float32)
    up = Image.fromarray((small * 255).astype(np.uint8)).resize((w, h), Image.BILINEAR)
    return np.asarray(up).astype(np.float32) / 255.0


def _clumpy(rng: np.random.Generator, h: int, w: int) -> np.ndarray:
    """Multi-octave noise weighted toward LOW frequency, so it clumps into
    organic paper-fiber blotches rather than reading as uniform digital static
    (the failure of the first pass: 'uniform flat digital noise overlay')."""
    f = 0.55 * _octave(rng, h, w, 16) + 0.30 * _octave(rng, h, w, 6) + 0.15 * _octave(rng, h, w, 2)
    f -= f.min()
    f /= max(f.max(), 1e-6)
    return f


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--paper", default="235,223,198", help="cream paper RGB")
    ap.add_argument("--starve", type=float, default=0.55, help="ink-starvation strength 0..1")
    ap.add_argument("--tooth", type=float, default=0.10, help="paper-tooth grain depth 0..1")
    ap.add_argument("--reg", type=int, default=0, help="registration offset in px (0 = off; channel-split reads as digital aberration)")
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()

    paper = np.array([int(x) for x in args.paper.split(",")], dtype=np.float32) / 255.0
    rng = np.random.default_rng(args.seed)

    arr = np.asarray(Image.open(args.inp).convert("RGB")).astype(np.float32) / 255.0
    h, w, _ = arr.shape
    lum = arr @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    darkness = 1.0 - lum  # high where ink is heavy

    # 1. ink-starvation: SOFT, clumpy lift toward paper in the darks. Continuous
    #    (not binary) blend driven by a low-frequency field gamma'd to 0/1 ends,
    #    so heavy ink breaks into organic blotches, not per-pixel static.
    field = _clumpy(rng, h, w)
    field = field ** 2.2  # push toward 0 so only field-peaks knock through
    m = (args.starve * (darkness ** 1.5) * field)[..., None]
    arr = arr * (1.0 - m) + paper * m

    # 2. paper tooth: subtle multiplicative grain, also clumped (not fine static)
    grain = 1.0 - args.tooth * _clumpy(rng, h, w)
    arr = arr * grain[..., None]

    # 3. loose registration: nudge R right, B left -> plate-misregistration fringe
    if args.reg:
        arr[..., 0] = np.roll(arr[..., 0], args.reg, axis=1)
        arr[..., 2] = np.roll(arr[..., 2], -args.reg, axis=1)

    out = np.clip(arr, 0.0, 1.0)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray((out * 255).astype(np.uint8)).save(args.out)
    print(f"saved -> {args.out}  (starve={args.starve} tooth={args.tooth} reg={args.reg} seed={args.seed})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
