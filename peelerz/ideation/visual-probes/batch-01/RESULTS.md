# Peelerz Visual Probes - Batch 01

Exploratory Nano Banana 2 renders for reaction and visual-legibility testing. These are generated probes, not source material, approved concepts, or presentation frames.

- Model: `gemini-3.1-flash-image-preview` (Nano Banana 2)
- Date: 2026-07-11
- Format: one 1K, 16:9 render per seed
- Shared reference: Tina/car/Peelerz frame extracted from Ben Hansford's treatment
- Prompt source: [prompts.yaml](prompts.yaml)
- Contact sheet: [contact-sheet.png](contact-sheet.png)

## s001 - Continuous peel tether

![s001 visual probe](outputs/2026-07-11/gemini-31-flash-image-preview/01_s001-continuous-peel-tether_921d8a93/s001-continuous-peel-tether_01.png)

**Visible result:** Tina levitates above the street holding a pink ribbon; a narrow strip of roadway lifts below her.

**What survived:** Tina, Peelerz, flight, ribbon, lifted road, neighborhood scale.

**What did not survive:** The ribbon does not visibly remain one material continuum from upholstery through car, road, and skyline. Levitation, ribbon, peeled road, and Uber compete as separate events.

**Blind Gemini caption:** A levitating woman holds a floating pink ribbon extending from an Uber while the road peels upward. The causal connection among ribbon, levitation, Uber, candy, and asphalt is unclear.

**Use:** Preserve the continuous-operation rule but simplify the frame drastically before rerendering.

## s034 - Sky-inhale orbit

![s034 visual probe](outputs/2026-07-11/gemini-31-flash-image-preview/02_s034-sky-inhale-orbit_b624ca04/s034-sky-inhale-orbit_01.png)

**Visible result:** Tina eats a pink gummy at the window while light street objects orbit her in a localized spiral.

**What survived:** Localized physical event, clear protagonist, grounded neighborhood, product action, curved object path.

**What did not survive:** The sky itself does not read as inhaling, and Tina's exhale/steering cannot be conveyed in the still.

**Blind Gemini caption:** A localized vortex circulates a chair, cups, mail, and receipts around the window. Eating the Peelerz is paired with the event, though strict causality remains uncertain.

**Use:** Strongest faithful probe. Advance the physical orbit; decide whether `sky inhales` is necessary or whether it was poetic scaffolding.

## s035 - Stopped-feed baseline

![s035 visual probe](outputs/2026-07-11/gemini-31-flash-image-preview/03_s035-stopped-feed-baseline_6cb2f0af/s035-stopped-feed-baseline_01.png)

**Visible result:** A central house is isolated inside a glowing pause/ripple interface while surrounding houses streak past.

**What survived:** Paused central house, moving background, candy aligned with a pause indicator.

**What did not survive:** The physical window-as-feed metaphor became a generic holographic smart-home interface. The pause target and consequence are ambiguous.

**Blind Gemini caption:** A gummy appears aligned with a holographic smart-home pause button; the physical meaning of the pause state is unexplained.

**Use:** Valuable baseline failure. The prose was judged most communicative, but the render was judged least communicative. Do not mistake a recognizable metaphor in text for a reliable visual result.

## s036 - Wrapper paperweight restage

![s036 visual probe](outputs/2026-07-11/gemini-31-flash-image-preview/04_s036-wrapper-paperweight-restage_7d71e832/s036-wrapper-paperweight-restage_01.png)

**Visible result:** A Peelerz package sits in a road depression while a large strip of asphalt peels upward carrying an SUV.

**What survived:** Low-angle scale contrast, package foreground, raised neighborhood surface, documentary realism.

**What did not survive:** Houses do not float independently and the wrapper does not read as a paperweight. NB2 transformed the requested mechanism into a simpler literal `Peelerz peels the road` gag.

**Blind Gemini caption:** The Peelerz bag appears directly related to a giant strip of road peeling upward. This was ranked the clearest single-frame gag.

**Use:** Preserve as an accidental generated seed with lineage from s036; do not mislabel it as a successful render of s036. Separately decide whether to repair the paperweight concept.

## Blind single-frame ranking

Gemini 3.5 Flash received the four images without seed descriptions and ranked their communication:

1. s036 render - direct package/peeled-road relationship, although it changed the idea
2. s034 render - clear localized vortex paired with candy eating
3. s001 render - striking but contains too many competing events
4. s035 render - abstract holographic interface, unclear physical consequence

## Batch lesson

Text-level and rendered-image legibility are not interchangeable. Before rendering, Gemini ranked s035 first and s036 last. After rendering, it ranked the s036 artifact first and s035 artifact last. Render tests therefore reveal both whether an idea survives visualization and whether the image model invents a different, more legible idea.

Generated artifacts belong in the probe archive with their lineage. They do not enter the external reference store as independent source material.
