"""Analyze the Doctor Strange universe-jump reference with Gemini at 24 fps.

Prints JSON to stdout. The caller is responsible for preserving the result.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


RIFF_SRC = Path("/Users/daviddickinson/Projects/Lora/riff-mcp/src")
sys.path.insert(0, str(RIFF_SRC))

from media_analysis_mcp import gemini_media  # noqa: E402


HERE = Path(__file__).resolve().parent
SOURCE_URL = "https://www.youtube.com/watch?v=CZI5V2VRc7s"

SYSTEM = """You are performing source-reference analysis for a film director.
Observe the supplied video precisely and do not brainstorm, recommend adaptations,
or infer an advertising brief. Separate visible and audible evidence from any
uncertainty. Use timestamps at frame-level precision where the sampling supports
it. Focus on formal construction rather than plot summary."""

QUESTION = """Produce a source-faithful analysis of this reference clip.

1. Give a chronological shot/beat table with precise start and end timestamps.
2. For every universe transition, describe:
   - the outgoing visual state;
   - the exact transition operation;
   - the incoming visual state;
   - what remains spatially or compositionally anchored across the change;
   - camera movement, subject movement, duration, and sound cue.
3. Distinguish hard cuts, continuous transformations, wipes/occlusions, match
   transitions, and changes of rendering medium or physical law.
4. Explain how subject legibility and screen direction are preserved or broken
   during rapid transformations.
5. Identify repeated formal rules without converting them into creative advice.
6. End with a list of the most informative individual-frame timestamps for a
   reference packet. Include frames immediately before and after important
   transitions, using 24 fps precision where possible.

Do not discuss Peelerz or propose new concepts. This pass is evidence collection."""


def main() -> None:
    client, gtypes = gemini_media.init_client()
    video_part = gtypes.Part(
        file_data=gtypes.FileData(file_uri=SOURCE_URL, mime_type="video/mp4"),
        video_metadata=gtypes.VideoMetadata(
            fps=24,
            start_offset="10s",
            end_offset="56s",
        ),
    )
    answer = gemini_media.call_unstructured(
        client=client,
        gtypes=gtypes,
        model="gemini-3.5-flash",
        system_instruction=SYSTEM,
        contents=[video_part, QUESTION],
        temperature=0.1,
    )
    result = {
        "model": "gemini-3.5-flash",
        "source_url": SOURCE_URL,
        "local_video": str(HERE / "reference.mp4"),
        "fps": 24,
        "start_offset": "10s",
        "end_offset": "56s",
        "question": QUESTION,
        "answer": answer,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
