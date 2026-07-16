"""Style-analysis driver — calls riff-mcp's (media-analysis-mcp) own Gemini
plumbing to characterize the *illustration style* of mood-board frames.

This is the calibration harness for the Phase-0 style work: send candidate
style frames to Gemini, compare its read against David's ground-truth labels,
and tune the system prompt until the analysis is reliable. It imports
``media_analysis_mcp.prompts`` + ``gemini_media`` directly rather than going
through the MCP tool layer, so the system prompt we're tuning is the same one
the tool will ship.

Run (deps come from the riff-mcp project venv):

    uv run --with google-genai --with pillow --with pydantic --with python-dotenv \\
        python scripts/style_probe.py \\
        --images "/abs/a.png,/abs/b.png" \\
        --question "Classify the illustration style ..." \\
        --model gemini-3.5-flash

Multiple --images are labeled "Image 1..N" so the question can compare them.
A single image is labeled "Image 1" too (harmless, keeps the prompt uniform).
"""
from __future__ import annotations

import argparse
import sys

RIFF_SRC = "/Users/daviddickinson/Projects/Lora/riff-mcp/src"
if RIFF_SRC not in sys.path:
    sys.path.insert(0, RIFF_SRC)

from media_analysis_mcp import gemini_media, prompts  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", required=True, help="comma-separated absolute image paths")
    ap.add_argument("--question", required=True, help="what to ask Gemini about the image(s)")
    ap.add_argument("--model", default="gemini-3.5-flash", help="Gemini model id")
    ap.add_argument("--temperature", type=float, default=0.3)
    ap.add_argument("--system", default="", help="override system instruction (default: analyze_image)")
    args = ap.parse_args()

    paths = [p.strip() for p in args.images.split(",") if p.strip()]
    client, gtypes = gemini_media.init_client()
    image_module = gemini_media.require_pillow()

    contents: list = [prompts.context_block(question=args.question)]
    for idx, p in enumerate(paths, start=1):
        contents.append(f"Image {idx}:")
        contents.append(gemini_media.load_image(p, image_module=image_module))

    system = args.system.strip() or prompts.analyze_image_system_prompt()

    out = gemini_media.call_unstructured(
        client=client,
        gtypes=gtypes,
        model=args.model,
        system_instruction=system,
        contents=contents,
        temperature=args.temperature,
    )
    print(f"[model={args.model}  images={len(paths)}]\n")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
