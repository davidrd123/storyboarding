"""Standalone Seedance 2.0 (Replicate) generation helper — video counterpart to
gen_openai.py / the gemini image CLI. Drives riff-mcp's own Seedance adapter
(gemini_video_prompts_mcp.seedance + replicate_min) directly, so the validation
+ Replicate plumbing match what the MCP tool would ship.

Needs REPLICATE_API_TOKEN in env (or .env). Run with ephemeral deps:

    uv run --with replicate --with python-dotenv python scripts/gen_seedance.py \
        --prompt "..." \
        --image refs/first_frame.png \
        --duration 5 --resolution 720p --aspect-ratio 16:9 \
        --title sisyphus-board-anim --out-root style-control-probe/outputs

Modes derive from inputs (seedance.derive_mode): --image -> first_last_frames
(optionally --last-frame-image); --reference-images -> omni_reference; neither
-> text_to_video. Output layout mirrors the image scripts:
<out-root>/<YYYY-MM-DD>/seedance-2.0/01_<title>_<hash>/<title>_NN.mp4 + job.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

RIFF_SRC = "/Users/daviddickinson/Projects/Lora/riff-mcp/src"
if RIFF_SRC not in sys.path:
    sys.path.insert(0, RIFF_SRC)

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:
    pass

from gemini_video_prompts_mcp import seedance  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--image", help="first-frame image path")
    ap.add_argument("--last-frame-image", help="last-frame image path (requires --image)")
    ap.add_argument("--reference-images", help="comma-separated ingredient image paths (omni_reference)")
    ap.add_argument("--duration", type=int, default=5, help="-1 (intelligent) or 4..15")
    ap.add_argument("--resolution", default="720p", choices=["480p", "720p", "1080p", "4k"])
    ap.add_argument("--aspect-ratio", default="16:9")
    ap.add_argument("--generate-audio", action="store_true")
    ap.add_argument("--seed", type=int)
    ap.add_argument("--title", default="seedance")
    ap.add_argument("--out-root", required=True)
    ap.add_argument("--timeout", type=int, default=600)
    args = ap.parse_args()

    ref_images = (
        [p.strip() for p in args.reference_images.split(",") if p.strip()]
        if args.reference_images
        else None
    )

    params = seedance.build_seedance_video_params(
        prompt=args.prompt,
        image=args.image,
        last_frame_image=args.last_frame_image,
        reference_images=ref_images,
        duration=args.duration,
        resolution=args.resolution,
        aspect_ratio=args.aspect_ratio,
        generate_audio=args.generate_audio,
        seed=args.seed,
    )

    mode = seedance.derive_mode(image=args.image, reference_images=ref_images)
    job_hash = seedance.build_seedance_job_hash(params)
    date = dt.date.today().isoformat()
    job_dir = Path(args.out_root).expanduser().resolve() / date / "seedance-2.0" / f"01_{args.title}_{job_hash}"

    print(f"[seedance] {args.title}  mode={mode}  dur={args.duration}s  {args.resolution} {args.aspect_ratio}")
    sidecar = seedance.run_seedance_job(
        api_params=params,
        return_params=params,
        out_dir=job_dir,
        base_name=args.title,
        timeout_s=args.timeout,
    )
    (job_dir / "job.json").write_text(json.dumps(sidecar, indent=2, default=str))

    if sidecar.get("success"):
        for o in sidecar.get("outputs", []):
            print(f"saved -> {o['path']}  ({o.get('bytes', 0)} bytes)")
        m = sidecar.get("metrics", {})
        print(f"predict_time_s={m.get('predict_time_s')}  elapsed_s={m.get('elapsed_s')}")
    else:
        print(f"FAILED: {sidecar.get('error')}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
