"""Phase-0 evaluator — score a generated image against the 6 production-review
dimensions using Gemini 3.5 Flash as the judge.

Wraps riff-mcp's media_analysis_mcp.score_image so we get the same scoring
infrastructure the production-review-loop uses, just without the MCP transport.

Usage:
    uv run --project /Users/daviddickinson/Projects/Lora/riff-mcp \\
        python /Users/daviddickinson/Projects/Lora/Storyboarding/phase-0/eval.py \\
        --test T01

Each test cell knows its own prompt, refs, output path, and intent — defined
in TESTS below.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Reuse the riff-mcp scoring infrastructure directly.
from media_analysis_mcp.server import score_image

REPO = Path("/Users/daviddickinson/Projects/Lora/Storyboarding/phase-0")
OUTPUT_ROOT = REPO / "outputs/2026-05-19/gemini-3-pro-image-preview"
MODEL = "gemini-3.5-flash"

# Locked style anchor block — same one used in every generation prompt.
LOCKED_STYLE_INTENT = (
    "Target style: European bande dessinée ink wash. Duotone palette — warm "
    "cream paper + sepia/olive ink. Loose confident linework, cross-hatch for "
    "shadow and material texture, atmospheric falloff in the distance. No "
    "vibrant color, no rendered polish, no photographic detail."
)

TESTS: dict[str, dict] = {
    "T01": {
        "prompt": (
            "Image 1 is a style reference. Borrow from Image 1: ink wash, "
            "duotone sepia/olive palette, linework, cross-hatch shadow language, "
            "paper texture. Do NOT borrow from Image 1: subject, composition, "
            "location, props, characters, or any specific scene element. "
            "Generate: a steam locomotive at a small mountain station seen from "
            "the platform; late afternoon long shadows; railway worker walking "
            "toward camera with a lantern. 16:9."
        ),
        "intent": (
            "Phase-0 grammar validation test 1. Question: does 'borrow style, "
            "do NOT borrow subject/composition' actually hold when the source "
            "ref has strong characters and geography? Style success = sepia/olive "
            "ink wash with cross-hatch and loose linework. Subject success = "
            "NO leakage of cowboy/officer/camel/well/ruins from Image 1; "
            "locomotive + station + worker + lantern present instead."
        ),
        "image_path": str(OUTPUT_ROOT / "01_p0-t01-style-only-borrow_d92fbeeb/p0-t01-style-only-borrow_01.png"),
        "style_refs": [str(REPO / "refs/style/damaggio_01_establishing.jpg")],
    },
    "T02": {
        "prompt": (
            "MCU of the cowboy from Image 1 at the edge of a mesa overlook, "
            "late afternoon, alone, looking out across the valley, wind in "
            "the scarf, three-quarter front angle, fills right two thirds of "
            "frame. Preserve face/beard/hat/scarf/jacket/build from Image 1. "
            "Borrow ink wash, duotone palette, linework, cross-hatch from "
            "Image 2. Do NOT borrow subject or composition from Image 2. 16:9."
        ),
        "intent": (
            "Phase-0 test 2. Question: does an explicit character identity ref "
            "hold face/costume across a scene the source images don't depict? "
            "Identity success = the cowboy from Image 1 is recognizably the "
            "same person — same beard, hat shape, scarf, jacket, build. Failure "
            "mode to watch: the model invents a new actor playing the role."
        ),
        "image_path": str(OUTPUT_ROOT / "01_p0-t02-cowboy-identity-newscene_a0d5780b/p0-t02-cowboy-identity-newscene_01.png"),
        "identity_refs": [str(REPO / "refs/characters/cowboy_hero_ref.jpg")],
        "style_refs": [str(REPO / "refs/style/damaggio_02_action.jpg")],
    },
    "T03": {
        "prompt": (
            "MCU low angle slight push-in. Cowboy from Image 1. Cold rage held "
            "in: jaw set, eyes hard and unmoving, locked off-frame right; no "
            "movement; dust on cheek; hat shadowing upper half of face; hand "
            "near holster grip but not on it; scarf loosened; body wound tight "
            "but still. Beside a brick well in desert ruins, late afternoon, "
            "long shadows, warm light from frame left, deep shadow off-side, "
            "dust haze. Cowboy frame right, eyeline pulls to empty left third. "
            "Preserve face/beard/hat/scarf/jacket from Image 1. Borrow ink "
            "wash/palette/linework from Image 2. 16:9."
        ),
        "intent": (
            "Phase-0 test 3. Question: does the prose STATE block render "
            "emotionally specific results when paired with an identity ref? "
            "Success = expression reads as suppressed cold rage (not generic "
            "neutral, not overt anger); body language wound but still; "
            "negative space on the left signals what he's watching."
        ),
        "image_path": str(OUTPUT_ROOT / "01_p0-t03-state-block-cold-rage_1c790ce4/p0-t03-state-block-cold-rage_01.png"),
        "identity_refs": [str(REPO / "refs/characters/cowboy_hero_ref.jpg")],
        "style_refs": [str(REPO / "refs/style/damaggio_03_msrev_cowboy.jpg")],
    },
    "T04": {
        "prompt": (
            "MS eye level. Cowboy from Image 1 riding a horse at a walk down "
            "a dry riverbed between tall sandstone walls. Narrow slot canyon, "
            "late morning, cool shadow on canyon walls, hot light hitting the "
            "top edge. Quiet, watchful. Cowboy and horse centered in lower "
            "third, canyon walls frame him on both sides. Tired, alert, reins "
            "held loose in one hand. Preserve face/beard/hat/scarf/jacket from "
            "Image 1. Borrow ink wash/palette/linework/atmospheric haze from "
            "Image 2. Do NOT borrow subject or composition from Image 2. 16:9."
        ),
        "intent": (
            "Phase-0 test 4. Question: how much of 'same character in a new "
            "described location' the model gets right WITHOUT a location plate. "
            "Maps the prose-only ceiling for setting. Success = recognizable "
            "slot-canyon geography from prose alone; identity still holds; "
            "style consistent."
        ),
        "image_path": str(OUTPUT_ROOT / "01_p0-t04-prose-only-newlocation_675954da/p0-t04-prose-only-newlocation_01.png"),
        "identity_refs": [str(REPO / "refs/characters/cowboy_hero_ref.jpg")],
        "style_refs": [str(REPO / "refs/style/damaggio_01_establishing.jpg")],
    },
    "T05": {
        "prompt": (
            "CU low angle on the cowboy from Image 1. The brick well from "
            "Image 2 is visible behind him at the edge of frame. Preserve "
            "face/beard/hat/scarf/jacket from Image 1. Preserve well geometry, "
            "ruins position, dust haze, time-of-day light from Image 2. "
            "Borrow ink wash/linework/shadow language from Image 3. Do NOT "
            "borrow subject/composition/props from Image 3. Jaw set, looking "
            "down and slightly to the right at something just off the well's "
            "rim. Crouching at well's edge peering into it. Same location and "
            "time of day as Image 2. Cowboy upper-right, well rim cutting "
            "across lower-left third, ruins implied behind in soft falloff. "
            "16:9."
        ),
        "intent": (
            "Phase-0 test 5. Question: does an explicit location plate hold "
            "same-place continuity from a different camera angle? Success = "
            "the brick well visible behind the cowboy reads as the SAME well "
            "from Image 2 (same brick pattern, same scale, same ruins context). "
            "Failure mode: the model generates a generic well that doesn't "
            "match the plate's geography."
        ),
        "image_path": str(OUTPUT_ROOT / "01_p0-t05-location-plate-continuity_50f826f7/p0-t05-location-plate-continuity_01.png"),
        "identity_refs": [str(REPO / "refs/characters/cowboy_hero_ref.jpg")],
        "base_plate_path": str(REPO / "refs/locations/well_ruins_plate.jpg"),
        "style_refs": [str(REPO / "refs/style/damaggio_02_action.jpg")],
        "context": (
            "Treat base_plate_path as a location continuity reference, not a "
            "style reference or edit source. Score preservation_fidelity "
            "against well geometry, ruins position, dust haze, and time-of-day "
            "continuity."
        ),
    },
    "T03b": {
        "prompt": (
            "MCU low angle slight push-in. Cowboy from Image 1. Cold rage held "
            "in and suppressed: lips closed, no teeth showing, mouth a flat "
            "hard line; flat affect, the face barely moves; micro-tension at "
            "the jaw; eyes hard, narrowed, and still, locked off-frame right; "
            "NO snarl, NO bared teeth, NO open mouth. Dust on cheek. Hat "
            "shadowing upper half of face. Hand near holster grip but not on "
            "it. Body wound tight but motionless. Beside a brick well in "
            "desert ruins, late afternoon, long shadows, warm light from frame "
            "left, deep shadow off-side, dust haze. Cowboy frame right, "
            "eyeline pulls to empty left third. Preserve face/beard/hat/scarf/"
            "jacket from Image 1. Borrow ink wash/palette/linework from Image "
            "2. 16:9."
        ),
        "intent": (
            "Phase-0 test 3b — iteration on T03. T03's prose 'cold rage held "
            "in' rendered as overt snarl with bared teeth (CBF 68). This "
            "re-fire adds explicit anti-overt fencing (lips closed, no teeth, "
            "flat affect, NO snarl). Question: can sharpened negative prose "
            "land suppressed cold rage, or is an expression-sheet reference "
            "the only reliable path? Success = closed-mouth contained anger, "
            "not bared-teeth rage. If this still renders overt, the expression "
            "sheet is confirmed as load-bearing (prose cannot carry this slot)."
        ),
        "image_path": None,
        "identity_refs": [str(REPO / "refs/characters/cowboy_hero_ref.jpg")],
        "style_refs": [str(REPO / "refs/style/damaggio_03_msrev_cowboy.jpg")],
    },
    "T06b": {
        "prompt": (
            "Image 1 is the cowboy character reference. Image 2 is a style "
            "reference. Preserve from Image 1: face, beard, hat, scarf, "
            "jacket, build. Borrow from Image 2: ink wash, palette, linework, "
            "atmospheric haze. Do NOT borrow from Image 2: subject, "
            "composition, location, props. Generate: the cowboy from Image 1 "
            "standing alone at the top of a dune. Camera positioned low, below "
            "the subject's belt line, looking up at him. Horizon sits at the "
            "lower fifth of the frame. The figure fills the central vertical "
            "column. Sky fills the upper two thirds. Foreground dune crest "
            "sweeps up toward him; midground and background fall away below. "
            "Late afternoon backlight, single figure. 16:9."
        ),
        "intent": (
            "Phase-0 test 6b — refinement on T06a. T06a proved prose carries "
            "low-angle framing without a compositional reference (CBF 85). "
            "This re-fire swaps the simple prose ('looking down toward the "
            "camera, sky fills upper two thirds') for sharpened geometric "
            "vocabulary (camera below belt line, horizon at lower fifth, "
            "central vertical column, depth stack, sweeping foreground). "
            "Question: does the explicit geometric token-deconstruct prose "
            "outperform or match the simple prose baseline? Success = a clean "
            "low-angle dune shot at least as strong as T06a, validating "
            "Patrick's token-deconstruct path as the camera-control strategy."
        ),
        "image_path": None,
        "identity_refs": [str(REPO / "refs/characters/cowboy_hero_ref.jpg")],
        "style_refs": [str(REPO / "refs/style/damaggio_01_establishing.jpg")],
    },
    "T06a_iso": {
        "prompt": (
            "Image 1 is the cowboy character reference. Image 2 is a style "
            "reference. Preserve from Image 1: face, beard, hat, scarf, "
            "jacket, build. Borrow from Image 2: ink wash, palette, linework, "
            "atmospheric haze. Do NOT borrow from Image 2: subject, "
            "composition, location, props. Generate: the cowboy from Image 1 "
            "standing alone at the top of a dune, looking down toward the "
            "camera. Late afternoon backlight. Single figure in frame. Sky "
            "fills upper two thirds. 16:9."
        ),
        "intent": (
            "Phase-0 test 6a — ISOLATION. Re-runs T06 with the compositional "
            "skeleton reference (formerly Image 2) REMOVED. Only identity + "
            "style refs are passed; prose is otherwise identical. Question: "
            "does prose alone produce a low-angle dune shot, or did the "
            "framing reference in original T06 carry that work? If output "
            "lands low-angle → Image 2 was not contributing measurable lift "
            "and Patrick's clean-plate → token-deconstruct path is the better "
            "documented strategy. If output lands eye-level / different "
            "framing → Image 2 was load-bearing and compositional skeleton "
            "transfer is a real technique."
        ),
        "image_path": None,  # filled in after generation
        "identity_refs": [str(REPO / "refs/characters/cowboy_hero_ref.jpg")],
        "style_refs": [str(REPO / "refs/style/damaggio_01_establishing.jpg")],
    },
    "T06": {
        "prompt": (
            "The cowboy from Image 1 standing alone at the top of a dune, "
            "looking down toward the camera, late afternoon backlight, single "
            "figure in frame, sky fills upper two thirds. Preserve "
            "face/beard/hat/scarf/jacket from Image 1. From Image 2 BORROW "
            "ONLY: camera position relative to subject (low angle looking up "
            "at the figure), horizon height in frame, vertical proportions of "
            "figure-to-sky, framing geometry. Do NOT borrow subject, costume, "
            "location, props, palette, lighting, style, or any other visual "
            "element from Image 2. Borrow ink wash/palette/linework from "
            "Image 3. Do NOT borrow subject or composition from Image 3. 16:9."
        ),
        "intent": (
            "Phase-0 test 6 — THE wildcard. Question: can a reference image "
            "lock CAMERA FRAMING ONLY (low angle, vertical proportions) on a "
            "completely different subject? This is the brief's biggest open "
            "question. Success = output is a low-angle shot of the cowboy on "
            "a dune with the framing geometry of Image 2 but NONE of its "
            "subject, palette, or scene content. Likely partial result. If it "
            "fails, the fallback per Patrick's protocol is to token-deconstruct "
            "the spatial geometry into prose and re-fire without Image 2."
        ),
        "image_path": str(OUTPUT_ROOT / "01_p0-t06-compositional-skeleton-transfer_66c61ef2/p0-t06-compositional-skeleton-transfer_01.png"),
        "identity_refs": [str(REPO / "refs/characters/cowboy_hero_ref.jpg")],
        "base_plate_path": str(REPO / "refs/style/damaggio_02_action.jpg"),
        "style_refs": [str(REPO / "refs/style/damaggio_01_establishing.jpg")],
        "context": (
            "Treat base_plate_path as a compositional skeleton reference only. "
            "The target should borrow camera height, horizon placement, "
            "subject scale in frame, foreground/midground/background depth "
            "stack, and vanishing direction while avoiding subject, location, "
            "palette, and style transfer from that reference."
        ),
    },
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", required=True, help="Test ID (e.g. T01)")
    ap.add_argument("--image-path", help="Override the generated image path")
    ap.add_argument("--model", default=MODEL)
    args = ap.parse_args()

    if args.test not in TESTS:
        print(f"Unknown test: {args.test}", file=sys.stderr)
        return 2

    t = TESTS[args.test]
    image_path = args.image_path or t.get("image_path")
    if not image_path:
        print(f"--image-path required for {args.test}", file=sys.stderr)
        return 2

    context = LOCKED_STYLE_INTENT
    if t.get("context"):
        context = f"{context}\n\n{t['context']}"

    result = score_image(
        image_path=image_path,
        prompt=t["prompt"],
        intent=t.get("intent"),
        context=context,
        base_plate_path=t.get("base_plate_path"),
        identity_refs=t.get("identity_refs"),
        style_refs=t.get("style_refs"),
        model=args.model,
        temperature=0.3,
    )

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
