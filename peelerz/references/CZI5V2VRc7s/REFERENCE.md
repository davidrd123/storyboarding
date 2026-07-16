# Doctor Strange Universe-Jump Reference

Reference cited in red text in Ben Hansford's Peelerz treatment.

- Source: [YouTube - CZI5V2VRc7s](https://www.youtube.com/watch?v=CZI5V2VRc7s)
- Downloaded title: `4K HDR | Jumping through Universes - Doctor Strange in the Multiverse of Madness | Dolby 5.1`
- Local full video: [reference.mp4](reference.mp4)
- Local transformation clip, source `00:10.000–00:56.000`: [reference-universe-jump.mp4](reference-universe-jump.mp4)
- Download metadata: [reference.info.json](reference.info.json)
- Thumbnail: [reference.jpg](reference.jpg)
- Analysis model: `gemini-3.5-flash`
- Sampling: `VideoMetadata(fps=24, start_offset="10s", end_offset="56s")`
- Analysis date: 2026-07-11
- Full model answer: [gemini-3.5-flash-24fps.md](gemini-3.5-flash-24fps.md)

The Gemini pass was deliberately source-blind: it received no Peelerz brief and was asked to observe formal construction without proposing adaptations.

## High-confidence formal observations

- The universe-jump section is staged as a continuous virtual-camera plunge rather than a montage of conventionally separated shots.
- Strange and America remain close to the center of the frame while environments change around them.
- Their persistent forward/downward Z-axis trajectory provides continuity across major changes of setting, physical law, palette, and rendering medium.
- Repeated crystalline/shattering planes articulate many transitions, accompanied by impact/whoosh changes in the soundtrack.
- Strange's red cape remains a recurring identification cue across visually noisy environments.
- Some transitions alter only environment; others alter the characters' own rendering or material state, including 2D animation, voxel/cube decomposition, and liquid paint.

These are observations of the supplied reference, not instructions for the Peelerz work.

## Gemini chronology at 24 fps

Gemini divided the clip as follows. Timestamps are against the full downloaded video.

| Time | Observed state or beat |
|---|---|
| `00:10.000–00:18.000` | Kamar-Taj action culminating in Strange and America entering the star portal |
| `00:19.083–00:20.500` | Giant stone heads / orange fog |
| `00:20.583–00:21.875` | Cosmic space and planetary horizon |
| `00:22.042–00:23.250` | Purple canyon / organic caves |
| `00:23.417–00:24.625` | Crystalline or ice environment |
| `00:24.750–00:26.000` | Amber honeycomb and giant bees |
| `00:26.125–00:29.792` | Underwater coral environment |
| `00:30.042–00:33.042` | Tilted contemporary New York street |
| `00:33.708–00:35.708` | White futuristic pipe city |
| `00:35.917–00:38.875` | Dark biomechanical / skeletal environment |
| `00:39.167–00:41.000` | Prehistoric jungle and dinosaur |
| approximately `00:41.500–00:43.750` | Characters and environment transition into 2D animation |
| `00:44.000–00:46.458` | Sepia/noir city |
| approximately `00:47.000–00:49.417` | Characters deconstruct into geometric cubes |
| approximately `00:49.750–00:52.792` | Characters become liquid paint |
| approximately `00:53.000–00:53.875` | Black-and-white film rendering |
| approximately `00:54.167–00:55.542` | Dark neon city |
| from approximately `00:55.708` | Bright white futuristic city with greenery |

This chronology is model-generated and should be checked against the frames or source video before being used for frame-accurate editorial claims.

## Transition frame packet

### First portal entry

Immediately before and after the first portal boundary:

![Frame at 17.958 seconds](frames-24fps/CZI5V2VRc7s_t17.958.png)

![Frame at 18.042 seconds](frames-24fps/CZI5V2VRc7s_t18.042.png)

### Stone-head environment into cosmic space

Before, during, and after the transition:

![Frame at 20.458 seconds](frames-24fps/CZI5V2VRc7s_t20.458.png)

![Frame at 20.500 seconds](frames-24fps/CZI5V2VRc7s_t20.500.png)

![Frame at 20.583 seconds](frames-24fps/CZI5V2VRc7s_t20.583.png)

### Underwater environment into New York

![Frame at 29.958 seconds](frames-24fps/CZI5V2VRc7s_t29.958.png)

![Frame at 30.042 seconds](frames-24fps/CZI5V2VRc7s_t30.042.png)

### Prehistoric/live-action environment into 2D animation

Gemini initially proposed `41.125–41.208`; direct frame inspection shows the mixed-media transition beginning closer to `41.500`, with the 2D rendering substantially established by `42.000`.

![Frame at 41.500 seconds](frames-24fps/CZI5V2VRc7s_t41.500.png)

![Frame at 42.000 seconds](frames-24fps/CZI5V2VRc7s_t42.000.png)

### Live rendering into geometric cubes

![Frame at 46.958 seconds](frames-24fps/CZI5V2VRc7s_t46.958.png)

![Frame at 47.042 seconds](frames-24fps/CZI5V2VRc7s_t47.042.png)

### Geometric cubes into liquid paint

![Frame at 49.708 seconds](frames-24fps/CZI5V2VRc7s_t49.708.png)

![Frame at 49.792 seconds](frames-24fps/CZI5V2VRc7s_t49.792.png)

### Liquid paint into black-and-white film rendering

![Frame at 52.958 seconds](frames-24fps/CZI5V2VRc7s_t52.958.png)

![Frame at 53.042 seconds](frames-24fps/CZI5V2VRc7s_t53.042.png)

### Final transition into the bright futuristic city

![Frame at 55.667 seconds](frames-24fps/CZI5V2VRc7s_t55.667.png)

![Frame at 55.750 seconds](frames-24fps/CZI5V2VRc7s_t55.750.png)

## Contact sheets

- [Selected transition frames](transition-contact-sheet.png)
- [2D-transition timing check](transition-2d-check.png)
- [Ten-second overview of full source](overview-10s.png)
- [Two-second overview of source `00:10–00:70`](overview-10-70-2s.png)

## Reproduction scripts

- [Run Gemini analysis](analyze_reference.py)
- [Extract identified frames](extract_reference_frames.py)

The Gemini API's custom-FPS video path is documented in Google's [Generate Content video-understanding guide](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding), which accepts `VideoMetadata.fps` values in `(0, 24]`.
