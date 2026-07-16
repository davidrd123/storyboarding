# Style Tests

Prompt and output log for reference-driven style probes. Per `CLAUDE.md` / `RECIPE.md`, this
file is the breadcrumb record: reference authority, prompt, output filename, and verdict.

---

## 2026-05-31 - Filth issue 02 reference probe

**Goal:** Rework the TEST 2 solvent breach with broad visual traits sampled from two local
reference pages from *The Filth* issue 02, while keeping all story content original to
`the-solvent`.

**Reference authority:**

| Ref | Path | Borrow | Do not borrow |
|-----|------|--------|---------------|
| Image 1 | `the-solvent/refs/style/filth-issue-02/filth-002-006-reference.jpg` | clean surreal sci-fi space, stacked page rhythm, saturated teal/cyan environment, hard black contouring | characters, dialogue, panel contents, vehicles, exact layout |
| Image 2 | `the-solvent/refs/style/filth-issue-02/filth-002-017-reference.jpg` | bold orange gutters/page field, grotesque bodily anxiety, dense wrinkles/hands, flat saturated mature-reader finish | characters, dialogue, panel contents, exact layout |

**Preassigned output:**
`the-solvent/outputs/style-tests/2026-05-31-filth-refs/filth-ref-solvent-breach-test-1.png`

**Prompt fired:**

```text
Use case: illustration-story
Asset type: full graphic-novel page style probe, vertical 2:3 portrait
Primary request: Generate a Solvent style test by reworking TEST 2, the first visible solvent breach, using the two comic-page reference images visible in this conversation only as broad visual references for line behavior, color logic, page rhythm, and sci-fi grotesque mood. Do not copy their panel compositions, characters, costumes, vehicles, dialogue, logos, or any exact image content.

Reference-image style traits to adapt, not copy: hard black comic contours; clean controlled inking with dense wrinkle/hand/fabric detail; saturated flat colors; bold acid-orange/cyan/magenta/teal palette; high-contrast figure modeling with heavy shadow shapes; sharp rectangular panels; thick gutters that become an active graphic color; surreal bureaucratic sci-fi interiors; uncanny body anxiety; confident early-2000s mature-reader comic-page finish; white speech balloons and caption boxes with black hand-lettered feel.

Scene and story: President August Vane, a fictional archetypal mogul-president, has taken CLARION. His hypercontrolled page-grid is being breached by the solvent. The page is a war between a rigid controlled comic layout and a widening blank white gutter that reveals the Witness.

Copyright/identity constraints: August Vane and the Witness are fictional. Do not depict or resemble any real politician, celebrity, existing comics character, or public figure.

Composition: one full vertical comic page with 5 to 7 hard-edged panels. Use bold black panel borders and a sickly orange page field/gutter system, but the central solvent breach is a vertical blank white rupture cutting through the page. The white rupture should feel like the page itself has been erased, not like background scenery.

Controlled panels: Vane appears in a synthetic executive control room, dark suit, silver-gold hair, stern monumental face, drawn with crisp black contour lines, dense facial wrinkles, heavy hand detail, flat saturated colors, teal screens, orange warning light, magenta/cyan accents. He is trying to physically repair the panel borders with a gold mechanical pen and both hands.

Solvent breach: at the center, a white gutter widens and eats into adjacent panels. Panel edges near the white dissolve into black speckle, dry-brush smear, and flat-color fragments. The orange gutters buckle and become jagged around the breach.

The Witness: inside the white rupture stands the same man as Vane but younger, plain, unadorned, calm, in simple pale clothing. Draw him with softer lighter linework and much less color, almost paper-pale, so he reads as a different visual system.

Required image language: make the page feel less gold-illuminated and more toxic, pop-surreal, bureaucratic sci-fi. Preserve the Solvent conceit: the host owns the panels, the Witness owns the gutter.

Lettering: include only two caption boxes, legible and correctly spelled:
Vane caption in a hard black-bordered box: "I BUILT ALL OF THIS."
Witness caption in a plain white box: "and none of it is load-bearing."

Quality checks: high resolution, clear full comic page, no copied characters or scenes from the references, no extra text, no watermark, Vane face consistent across panels, Witness visibly related but simpler, the white gutter breach unmistakable.
```

**Output landed:**
`the-solvent/outputs/style-tests/2026-05-31-filth-refs/filth-ref-solvent-breach-test-1.png`

**Verdict:** Useful style direction. Strong toxic pop-sci-fi palette, orange gutters, teal/magenta
control-room panels, harder black contouring, and central white rupture still reads. Caption
text survived. It drifts away from the gold CLARION monument register, which is acceptable for
a style probe but should be deliberately mixed back if used for Page 5 continuity.
