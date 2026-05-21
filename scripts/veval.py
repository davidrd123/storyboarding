"""veval — rubric-free visual evaluation.

The 6-dimension score_image rubric was inherited from a different project and
proved noisy here (same model's "style lock" swung 76->88 across two panels).
This tool drops the numeric rubric entirely and does what actually works with a
strong vision model: put the reference image(s) and the candidate(s) in one
context, label each honestly, and ask the model to reason in prose —
comparatively, grounded in specific visible evidence.

Principle: vision models are reliable at "A is closer to the reference than B,
and here is the specific difference" and unreliable at "this is an 82." So
prefer comparison with the reference in-frame over absolute scoring.

Usage (run with riff-mcp's env so google-genai + key resolve):

    uv run --project /Users/daviddickinson/Projects/Lora/riff-mcp \\
        python scripts/veval.py \\
        --image "Damaggio style reference:phase-0/refs/style/damaggio_01_establishing.jpg" \\
        --image "Candidate A — gpt-image-2 mesa:phase-0/outputs/.../t02...png" \\
        --image "Candidate B — gpt-image-2 canyon:phase-0/outputs/.../t04...png" \\
        --question "Which candidate more faithfully reproduces the reference's linework and rendering, and what specifically differs?"

Each --image is "LABEL:PATH" (split on the first colon). Images are sent in the
order given; put references first, candidates after. The model sees every image
with its label, then the question.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from media_analysis_mcp import gemini_media

DEFAULT_MODEL = "gemini-3.1-pro-preview"

SYSTEM = (
    "You are a senior storyboard artist and art director with an exacting eye. "
    "You are shown one or more REFERENCE images and one or more CANDIDATE images, "
    "each labeled. Judge the candidates against the references and the question.\n\n"
    "Rules:\n"
    "- Ground every claim in specific visible evidence — name the region, the "
    "line treatment, the value, the feature. No vague praise.\n"
    "- When there are multiple candidates, RANK them and explain the basis for "
    "the ranking. Comparative judgment is more reliable than absolute judgment, "
    "so prefer 'A is closer than B because X'.\n"
    "- Do NOT assign numeric scores. Describe what you actually see.\n"
    "- Separate the axes that matter for a storyboard panel: character identity "
    "vs the identity reference; style/linework/palette vs the style reference; "
    "staging and readability of the beat; anything a director or editor would "
    "object to.\n"
    "- Call out failure modes explicitly, even small ones. Be the critic who "
    "catches drift early.\n"
    "- Be concise and specific. No preamble."
)


def parse_labeled(items: list[str]) -> list[tuple[str, Path]]:
    out: list[tuple[str, Path]] = []
    for it in items:
        if ":" not in it:
            print(f"--image must be LABEL:PATH, got: {it}", file=sys.stderr)
            raise SystemExit(2)
        label, path = it.split(":", 1)
        p = Path(path).expanduser().resolve()
        if not p.is_file():
            print(f"IMAGE_NOT_FOUND: {p}", file=sys.stderr)
            raise SystemExit(2)
        out.append((label.strip(), p))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--image", action="append", required=True,
                    help="LABEL:PATH — repeatable; references first, candidates after")
    ap.add_argument("--question", required=True)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--temperature", type=float, default=0.3)
    ap.add_argument("--system", default=SYSTEM)
    args = ap.parse_args()

    labeled = parse_labeled(args.image)
    image_module = gemini_media.require_pillow()
    client, gtypes = gemini_media.init_client()

    contents: list = ["Images for evaluation (each labeled):"]
    for label, path in labeled:
        contents.append(f"\n[{label}]:")
        contents.append(gemini_media.load_image(str(path), image_module=image_module))
    contents.append(f"\nQUESTION: {args.question}")

    answer = gemini_media.call_unstructured(
        client=client,
        gtypes=gtypes,
        model=args.model,
        system_instruction=args.system,
        contents=contents,
        temperature=args.temperature,
    )

    print(f"--- veval ({args.model}) ---")
    for label, path in labeled:
        print(f"  [{label}] {path.name}")
    print(f"\nQ: {args.question}\n")
    print(answer)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
