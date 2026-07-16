"""Extract the transition-reference frames identified by the 24 fps Gemini pass."""

from __future__ import annotations

import json
import sys
from pathlib import Path


RIFF_SRC = Path("/Users/daviddickinson/Projects/Lora/riff-mcp/src")
sys.path.insert(0, str(RIFF_SRC))

from media_analysis_mcp.server import extract_video_frames  # noqa: E402


HERE = Path(__file__).resolve().parent

TIMESTAMPS = [
    17.958,
    18.042,
    20.458,
    20.500,
    20.583,
    29.958,
    30.042,
    41.125,
    41.208,
    46.958,
    47.042,
    49.708,
    49.792,
    52.958,
    53.042,
    55.667,
    55.750,
]


def main() -> None:
    result = extract_video_frames(
        video_path=str(HERE / "reference.mp4"),
        timestamps=TIMESTAMPS,
        out_dir=str(HERE / "frames-24fps"),
        title_prefix="CZI5V2VRc7s",
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
