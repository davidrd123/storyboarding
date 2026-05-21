"""Standalone gpt-image-2 generation helper — OpenAI counterpart to riff-mcp's
gemini-video-prompts CLI, for head-to-head model comparison.

Run with ephemeral openai dep (no install needed):

    uv run --with openai python scripts/gen_openai.py \\
        --prompt "..." \\
        --images refs/a.png,refs/b.png \\
        --system-prompt "STYLE: ..." \\
        --title idp-p3-comp-gpt \\
        --out-root identity-ref-probe/outputs

Reference-based jobs (any --image/--images given) use the images.edit endpoint,
which accepts up to 16 input images for gpt-image models. Text-only jobs use
images.generate. OpenAI image models have no system-prompt slot, so a
--system-prompt is prepended to the prompt (the only way to deliver a style
block) — keeping parity with the Gemini runs where it's a system instruction.

Output layout mirrors riff-mcp: <out-root>/<YYYY-MM-DD>/gpt-image-2/NN_<title>_<hash>/<title>_01.png
plus a job.json sidecar, so eval.py and find-based retrieval work the same way.
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import json
import secrets
import sys
import time
from pathlib import Path

from openai import OpenAI


def _resolve_paths(csv: str | None, single: str | None) -> list[Path]:
    paths: list[str] = []
    if single:
        paths.append(single)
    if csv:
        paths.extend(p.strip() for p in csv.split(",") if p.strip())
    resolved = [Path(p).expanduser().resolve() for p in paths]
    for p in resolved:
        if not p.is_file():
            print(f"IMAGE_NOT_FOUND: {p}", file=sys.stderr)
            raise SystemExit(2)
    return resolved


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--images", help="comma-separated input image paths (edit endpoint)")
    ap.add_argument("--image", help="single input image path (edit endpoint)")
    ap.add_argument("--system-prompt", default="", help="style block; prepended to prompt")
    ap.add_argument("--model", default="gpt-image-2")
    ap.add_argument("--size", default="1536x864", help="WxH, divisible by 16; default 16:9")
    ap.add_argument("--quality", default="high", choices=["high", "medium", "low", "auto"])
    ap.add_argument("--title", default="gpt-image")
    ap.add_argument("--out-root", required=True)
    args = ap.parse_args()

    prompt = args.prompt
    if args.system_prompt:
        prompt = f"{args.system_prompt}\n\n{prompt}"

    inputs = _resolve_paths(args.images, args.image)
    client = OpenAI()

    t0 = time.perf_counter()
    if inputs:
        print(f"[edit] {args.title} via {args.model} with {len(inputs)} ref(s)")
        files = [open(p, "rb") for p in inputs]
        try:
            result = client.images.edit(
                model=args.model,
                image=files,
                prompt=prompt,
                size=args.size,
                quality=args.quality,
            )
        finally:
            for f in files:
                f.close()
    else:
        print(f"[generate] {args.title} via {args.model} (text-only)")
        result = client.images.generate(
            model=args.model,
            prompt=prompt,
            size=args.size,
            quality=args.quality,
        )
    elapsed = time.perf_counter() - t0

    b64 = result.data[0].b64_json
    if not b64:
        print("NO_IMAGE_RETURNED", file=sys.stderr)
        return 1
    png = base64.b64decode(b64)

    date = dt.date.today().isoformat()
    job_hash = secrets.token_hex(4)
    job_dir = Path(args.out_root).expanduser().resolve() / date / args.model / f"01_{args.title}_{job_hash}"
    job_dir.mkdir(parents=True, exist_ok=True)
    out_png = job_dir / f"{args.title}_01.png"
    out_png.write_bytes(png)

    sidecar = {
        "title": args.title,
        "model": args.model,
        "size": args.size,
        "quality": args.quality,
        "prompt": prompt,
        "input_images": [str(p) for p in inputs],
        "endpoint": "edit" if inputs else "generate",
        "latency_seconds": round(elapsed, 2),
        "output": str(out_png),
        "usage": getattr(result, "usage", None) and result.usage.model_dump()
        if hasattr(getattr(result, "usage", None), "model_dump")
        else None,
    }
    (job_dir / "job.json").write_text(json.dumps(sidecar, indent=2))

    print(f"saved -> {out_png}  ({elapsed:.1f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
