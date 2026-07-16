"""media_probe.py — mixed-media (video + image) Gemini analysis driver.

The video-capable counterpart to ``style_probe.py`` (which is image-only). Sends
any combination of ``--videos`` (uploaded via Gemini's Files API) and ``--images``
in a single ``contents`` list, labeled "Video 1..N" / "Image 1..N" so the question
can reference them. Cleans up uploaded videos afterward (Files API resources
persist ~48h otherwise). Imports riff-mcp's ``media_analysis_mcp`` plumbing
directly, same as style_probe.

    uv run --with google-genai --with pillow --with python-dotenv \\
        python scripts/media_probe.py \\
        --videos "/abs/a.mp4,/abs/b.mp4" --images "/abs/c.png" \\
        --question "Video 1 is ... ; Image 1 is context ..." \\
        --model gemini-3.5-flash [--system "..."]
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
    ap.add_argument("--videos", default="", help="comma-separated absolute video paths")
    ap.add_argument("--images", default="", help="comma-separated absolute image paths")
    ap.add_argument("--question", required=True)
    ap.add_argument("--model", default="gemini-3.5-flash")
    ap.add_argument("--temperature", type=float, default=0.3)
    ap.add_argument("--system", default="", help="override system instruction (default: analyze_video)")
    args = ap.parse_args()

    vids = [p.strip() for p in args.videos.split(",") if p.strip()]
    imgs = [p.strip() for p in args.images.split(",") if p.strip()]
    if not vids and not imgs:
        print("NO_MEDIA: pass --videos and/or --images", file=sys.stderr)
        return 2

    client, gtypes = gemini_media.init_client()
    image_module = gemini_media.require_pillow()

    uploaded: list = []
    try:
        contents: list = [prompts.context_block(question=args.question)]
        for i, v in enumerate(vids, start=1):
            print(f"uploading video {i}: {v} …", file=sys.stderr)
            f = gemini_media.upload_and_poll_video(client, v)
            uploaded.append(f)
            contents.append(f"Video {i}:")
            contents.append(f)
        for i, im in enumerate(imgs, start=1):
            contents.append(f"Image {i}:")
            contents.append(gemini_media.load_image(im, image_module=image_module))

        system = args.system.strip() or prompts.analyze_video_system_prompt()
        out = gemini_media.call_unstructured(
            client=client,
            gtypes=gtypes,
            model=args.model,
            system_instruction=system,
            contents=contents,
            temperature=args.temperature,
        )
        print(f"[model={args.model}  videos={len(vids)}  images={len(imgs)}]\n")
        print(out)
    finally:
        for f in uploaded:
            gemini_media.cleanup_uploaded(client, f)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
