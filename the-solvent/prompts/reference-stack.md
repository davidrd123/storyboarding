# Reference Stack Assets

Prompt and output log for project reference assets: character sheets, layout locks, and other
inputs used to control later page generations.

---

## 2026-05-31 - Vane, Witness, Page 5 Layout Lock

**Goal:** Build the first three control assets recommended by `RECIPE.md`: Vane identity sheet,
Witness identity sheet, and Page 5 Image A layout lock.

**Reference authority:**

| Ref | Path | Borrow | Do not borrow |
|-----|------|--------|---------------|
| CLARION register probe | `the-solvent/outputs/opening-tests/2026-05-31-register-probes/test-1-page-1-clarion-register.png` | Vane's mature face, silver-gold hair, dark suit, gold-control finish, V emblem language | exact page layout, captions, throne-room composition |
| Solvent register probe | `the-solvent/outputs/opening-tests/2026-05-31-register-probes/test-2-solvent-register.png` | Witness relation to Vane, white gutter figure, border-failure grammar | exact page layout, captions |
| Filth-style solvent probe | `the-solvent/outputs/style-tests/2026-05-31-filth-refs/filth-ref-solvent-breach-test-1.png` | toxic orange/teal pop-sci-fi option, hard black contouring, white rupture behavior | exact page layout, captions |

### ASSET 1 - Vane character sheet v1

**Preassigned output:**
`the-solvent/refs/characters/vane-sheet-v1.png`

**Prompt fired:**

```text
Use case: illustration-story
Asset type: labeled comic character model sheet / production reference, landscape format
Primary request: Create a labeled character sheet for PRESIDENT AUGUST VANE, the fictional protagonist of The Solvent. This is a production reference for consistent future comic pages.

Reference authority: Use the visible Solvent register-probe images as broad continuity references for Vane's face, hair, suit, and gold-control visual language. Do not copy any exact panel layout or captions from them.

Copyright/identity constraints: August Vane is fictional. Do not depict or resemble any real politician, celebrity, existing comics character, or public figure.

Character bible: PRESIDENT AUGUST VANE. Male, late 60s. Powerful imperious mogul-president. Silver-gold swept-back hair, heavy brow, severe eyes, square monumental jaw, deep wrinkles, expensive dark suit, white shirt, black-and-gold patterned tie, gold ring, V lapel pin or cuff detail. He should read as a face built for monuments: controlled, proprietary, humorless, dominant.

Sheet layout: clean production model sheet on an off-white background, black comic ink line with controlled color. Include labeled sections with legible uppercase labels:
TITLE: PRESIDENT AUGUST VANE
ROW 1: FRONT / THREE-QUARTER / PROFILE / BACK
ROW 2: ACTION POSES
ROW 3: EXPRESSIONS
CALLOUTS: SILVER-GOLD HAIR / V LAPEL PIN / GOLD RING / MONUMENT FACE

Required drawings:
- Four standing turnaround views: front, three-quarter front, side profile, back.
- Four action poses: seated at command desk, holding a gold lozenge pill, repairing a panel border with a gold pen, both hands gripping a straight border.
- Five expression heads: controlled neutral, cold smile, wounded rage, suspicious calculation, CLARION focus.
- Small accessory drawings: gold lozenge pill, V lapel pin, gold ring, gold mechanical pen.

Style: mature-reader graphic novel production art, crisp black contour, dense controlled facial wrinkles and hand detail, flat colors, restrained gold accents, clean labels, no decorative finished-page background. Keep the same face across every pose.

Quality checks: high resolution, labels legible, no extra characters, no watermark, all views clearly the same fictional man, no resemblance to real public figures.
```

**Output landed:**
`the-solvent/refs/characters/vane-sheet-v1.png`

**Verdict:** Strong production sheet. Labels are clean; turnaround, action poses, expressions,
and accessories are all usable. Good identity anchor for Vane's repeated self-image.

### ASSET 2B - Witness character sheet v2 correction

**Reason:** First Witness sheet landed with a useful upper model-sheet section, but also picked
up an unwanted partial page-layout/template band at the bottom. Correction pass keeps labels but
explicitly forbids page templates, color keys, panels, and Image A language.

**Preassigned output:**
`the-solvent/refs/characters/witness-sheet-v2.png`

**Prompt fired:**

```text
Use case: illustration-story
Asset type: labeled comic character model sheet / production reference, landscape format
Primary request: Create ONLY a clean labeled character model sheet for THE WITNESS, the buried alter / younger plain self of August Vane in The Solvent. This is a production reference for consistent future comic pages, not a story page and not a layout template.

Hard exclusions: Do not include PAGE 5, IMAGE A, color keys, comic-page panels, page thumbnails, red silhouettes, gold panel layouts, desk scenes, screen diagrams, central gutter diagrams, story captions, dialogue balloons, or any finished comic-page composition. This must be one landscape character sheet only.

Copyright/identity constraints: The Witness is fictional. Do not depict or resemble any real politician, celebrity, existing comics character, or public figure.

Character bible: THE WITNESS. Male, looks 25-35. Same underlying face architecture as August Vane before the brand-self hardened: similar brow, nose, jaw, and eye shape, but younger and less armored. Plain pale loose clothing, barefoot, no suit, no gold, no insignia. Calm, unadorned, watchful, almost paper-pale. He belongs to the white gutter, not the panels.

Sheet layout: clean production model sheet on a white-paper background, with simple ruled compartments like an animation turnaround sheet. Include labeled sections with legible uppercase labels:
TITLE: THE WITNESS
TURNAROUND: FRONT / THREE-QUARTER / PROFILE / BACK
GUTTER POSES
EXPRESSIONS
ACCESSORIES / OBJECTS
CALLOUTS: SAME FACE UNDERNEATH / PLAIN CLOTHES / NO GOLD / SOFTER LINE

Required drawings:
- Four standing turnaround views: front, three-quarter front, side profile, back.
- Four gutter poses: standing calmly in blank white space, looking out at the reader, placing a vial just outside an invisible edge, one hand touching a dissolving border fragment.
- Five expression heads: calm neutral, compassion without sentiment, lucid sadness, unreadable stillness, quiet refusal.
- Small accessory/object drawings: plain vial labeled SOLVENT, bare hand emerging from blank white, dissolving border fragment.

Style: soft graphite-and-ink comic production art, minimal pale color, sparse shadows, white space, light contour, subtle ink wash only around the small dissolving-border accessory. Much softer and simpler than Vane's sheet. Make him visibly the same man underneath but not the same social identity.

Quality checks: high resolution, labels legible, no page template, no Image A, no color key, no comic panels, no extra characters, no watermark.
```

**Output landed:**
`the-solvent/refs/characters/witness-sheet-v2.png`

**Verdict:** Preferred Witness sheet. Clean character-reference-only layout with no Image A
contamination. Labels are legible; the softer line and no-gold distinction read clearly.

### ASSET 2 - Witness character sheet v1

**Preassigned output:**
`the-solvent/refs/characters/witness-sheet-v1.png`

**Prompt fired:**

```text
Use case: illustration-story
Asset type: labeled comic character model sheet / production reference, landscape format
Primary request: Create a labeled character sheet for THE WITNESS, the buried alter / younger plain self of August Vane in The Solvent. This is a production reference for consistent future comic pages.

Reference authority: Use the visible Solvent register-probe images as broad continuity references. The Witness should be recognizably related to Vane, but younger, simpler, paler, softer, and drawn in a different visual system. Do not copy any exact page layout or captions.

Copyright/identity constraints: The Witness is fictional. Do not depict or resemble any real politician, celebrity, existing comics character, or public figure.

Character bible: THE WITNESS. Male, looks 25-35. The same underlying face architecture as Vane before the brand-self hardened: similar brow, nose, jaw, and eye shape, but younger and less armored. Plain pale loose clothing, barefoot, no suit, no gold, no insignia. Calm, unadorned, watchful, almost paper-pale. He belongs to the white gutter, not the panels.

Sheet layout: clean production model sheet on a white-paper background, soft graphite-and-ink comic line with minimal pale color. Include labeled sections with legible uppercase labels:
TITLE: THE WITNESS
ROW 1: FRONT / THREE-QUARTER / PROFILE / BACK
ROW 2: GUTTER POSES
ROW 3: EXPRESSIONS
CALLOUTS: SAME FACE UNDERNEATH / PLAIN CLOTHES / NO GOLD / SOFTER LINE

Required drawings:
- Four standing turnaround views: front, three-quarter front, side profile, back.
- Four gutter poses: standing in a vertical white rupture, looking out at the reader, placing a vial just outside a panel, one hand touching a dissolving border.
- Five expression heads: calm neutral, compassion without sentiment, lucid sadness, unreadable stillness, quiet refusal.
- Small accessory/object drawings: plain vial labeled SOLVENT, bare hand emerging from gutter, dissolving border fragment.

Style: production reference sheet, softer and simpler than Vane's sheet, pale paper tones, light graphite contour, sparse shadows, subtle ink wash at edges, plenty of white space. Make him visibly the same man underneath but not the same social identity.

Quality checks: high resolution, labels legible, no extra characters, no watermark, all views clearly the same fictional man and clearly related to Vane.
```

**Output landed:**
`the-solvent/refs/characters/witness-sheet-v1.png`

**Verdict:** Useful but superseded by v2. Upper sheet content is good, but it picked up an
unwanted partial page-layout/template band, so do not use it as the primary reference.

### ASSET 3 - Page 5 gutter breach Image A v1

**Preassigned output:**
`the-solvent/refs/layout/page-05-gutter-breach-image-a-v1.png`

**Prompt fired:**

```text
Use case: illustration-story
Asset type: labeled comic page layout lock / flat colorblock Image A, vertical 2:3 portrait
Primary request: Create a labeled flat-color layout template for Page 5 of The Solvent. This is not a finished comic page. It is Image A: a composition lock for later generations.

Reference authority: Use the visible solvent-register pages only for the structural idea: Vane panels around a widened central white gutter with the Witness in the white. Do not render finished art, faces, shading, captions, or detailed environments.

Purpose: The later image model should be able to copy this panel layout exactly. Make the panel geometry, gutter sizes, character positions, and action zones unambiguous.

Format: vertical 2:3 portrait comic page template. Flat color blocks only. Thick clean black outer page border. Hard panel borders. No detailed drawing. No realistic rendering.

Color key:
- BLACK = outer border and panel borders
- DARK GOLD = intact CLARION/Vane panels
- BRIGHT GOLD = repair lines / panel-border action
- WHITE = solvent gutter / not-self space
- PALE BLUE = Witness figure zone
- RED = Vane figure/action zones
- GRAY = desk/screen/background zones
- ORANGE = unstable edge / dissolving border zones

Layout: central vertical WHITE gutter rupture runs from near top to bottom, slightly irregular and too wide. It divides the page into left and right stacks of rigid panels. Around it are 8 intact or partly damaged panels:
Top left: Vane front view gripping a gold border.
Top right: Vane profile pressing a border shut.
Middle left: Vane from behind facing screens.
Middle center inside white gutter: Witness standing full-body in pale blue.
Middle right: Vane hand drawing a rectilinear repair line.
Lower left: cracked Vane face reflection panel.
Lower right: hand placing tomorrow's dose near a panel edge.
Bottom wide panel: Vane at command desk, tiny against rigid architecture.

Labels: include clear uppercase diagram labels, not story dialogue:
PAGE 5 IMAGE A
WHITE GUTTER / WITNESS ZONE
VANE PANELS
DISSOLVING BORDER
REPAIR LINE
DOSE OBJECT
SCREEN FACE

Quality checks: flat template, legible labels, exact page-layout utility, no finished rendering, no comic dialogue, no decorative detail, no watermark.
```

**Output landed:**
`the-solvent/refs/layout/page-05-gutter-breach-image-a-v1.png`

**Verdict:** Strong Image A. Flat colorblock structure, central white gutter, Vane/Witness zones,
repair lines, dose object, and labels are all legible. Suitable as the Page 5 layout lock.
