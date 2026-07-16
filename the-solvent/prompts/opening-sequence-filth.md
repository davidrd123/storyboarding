# Opening sequence — *The Filth* register system (NB2 via riff MCP)

The proven look (see `outputs/style-probes/`): the **Filth/Weston register-as-layers system**.
Vane's whole self is a surveilled, mediated construct, so the layers are:

- **self-image** = warm full-color **full-bleed** (how he sees himself)
- **reality** = cold **duotone CCTV monitor** panel, scanlines + timecode (what the camera sees)
- **dissolution** = **static/glitch corruption** that *crosses panel borders* (the mediation failing)

Border-TYPE is the register. Dissolution should violate borders, not sit in its own box.

**Model:** `gemini-3.1-flash-image-preview` (NB2) · **aspect:** `2:3` · sequential calls only.
**Consistency caveat:** NB2 won't hold Vane's exact face across separate genesis calls — for a
real run, anchor later pages with an earlier page as an img2img/identity ref, or finish on a Pro
model. These are layout/sequence proofs; lettering is approximate at NB2 (final = Pro or a
separate lettering pass).

## Reusable house `system_prompt` (paste into every page)

> Art style of Chris Weston on Grant Morrison's THE FILTH (Vertigo, 2002): dense precise fine-line
> ink, heavy feathered hatching, grotesque-realist faces pushed HARD (etched wrinkles, jowls,
> pores, unflattering), clinical mundane detail. Encode registers by panel-border type: warm
> full-color full-bleed = self-image; rounded duotone blue-grey CCTV monitor with scanlines +
> corner timecode = surveillance reality; static/glitch/macroblock corruption that crosses panel
> borders = dissolution. Bold, confident, sophisticated layout — varied panel sizes, puncturing
> insets, full-bleed, corruption violating borders. PRESIDENT AUGUST VANE: imperious silver-haired
> mogul-president, late 60s, heavy dark suit, small "V" monogram — the same man every time. THE
> WITNESS: the same face but younger, plain, pale, calm, drawn in a softer/cleaner line.

---

## PAGE 1 — THE MONUMENT *(cold-open splash — DONE: `style-probes/...page1-pushed-layout`)*

The pushed splash works as the cold open: the whole arc compressed — gilded self-image, CCTV
reality puncturing it, the eye, and the first static-tear already eating his face. Use as Page 1.
Captions: *"THERE IS A VERSION OF ME ON EVERY SURFACE IN THIS ROOM."* / *"I HAD IT BUILT THAT WAY."*

## PAGE 2 — CLARION *(control at maximum)*

```
prompt: A comic page at the tightest, most controlled register. A rigid, symmetrical grid of
crisp, PRISTINE gold panels and clean CCTV monitors — NO corruption anywhere. PRESIDENT AUGUST
VANE's composed face repeated across clean gold screens. In a central wider panel he calmly
dismantles an opponent across a boardroom table, reading him ten moves ahead, utterly in command.
Everything sharp, gilded, airless, total — the reader should feel how GOOD the control feels.
Gold caption: "I SEE EVERY MOVE BEFORE IT IS MADE." / "THIS IS NOT ARROGANCE. IT IS RESOLUTION."
ref: genesis (no image)
```

## PAGE 3 — THE FIRST TEAR

```
prompt: Control still holding — gold panels, clean monitors — BUT one monitor's gutter runs a
hair too wide, and a single thread of static and glitch leaks from it ACROSS the gold border. On
one screen a hairline crack runs across Vane's composed face. He pauses, unsettled. A caption
finishes in a calmer cadence that is NOT his voice (plain box, not gold): "and none of it is
load-bearing." Strained gold caption: "WHO— WHO THOUGHT THAT."
ref: genesis, or img2img off Filth page 5 (clean grid to corrupt)
```

## PAGE 4 — THE SOLVENT

```
prompt: A hard cut. A WIDE band of static and dead-air runs across the middle of the page — a gap
in time the reader's eye must cross. Vane comes to mid-gesture on the far side, disoriented, the
clock jumped. On his gold desk: a second small glass vial, open, that he does not remember opening
— his own fingerprints on it, a dose already gone. His jowly face dawns with dread. Gold caption,
first fear: "the solvent." He has named it inside the gap.
ref: genesis
```

## PAGE 5 — THE DEAD CHANNEL *(≈ proven probe 4)*

```
prompt: A wall of CCTV monitors, Vane's face on each, the signal now CORRUPTING across the page —
static, macroblocks, glitch-tear, timecodes failing to "ERROR". In the few intact gold panels,
Vane presses his hands to the borders, forcing the grid back together, re-gilding, redrawing his
cracked face clean — and it is mostly working. BUT one monitor, dead center, has gone to a clean
bright dead channel, and standing calmly inside it is THE WITNESS, untouched, looking out. The one
space the control cannot close. Strained gold caption: "I CAN RESTORE THE BOUNDARY." / Witness,
plain: "there was never a boundary."
ref: img2img off Filth page 5
```

## PAGE 6 — FIND THEM

```
prompt: Rattled, Vane turns his control OUTWARD: a war-room of gold monitors as he commands a hunt
— security feeds, the supply chain. Cold gold caption, regaining composure: "SOMEONE IS DOING THIS
TO ME. FIND THEM." The thriller launches: a search for an administrator who isn't external. FINAL
panel, bottom: in one last open dead-channel monitor, THE WITNESS's plain hand sets a single gold
lozenge pill where Vane's morning will find it, and the Witness looks straight OUT at the reader,
not at Vane. Plain calm caption: "YOU'LL HELP. YOU ALREADY DID. YOU FILLED IN THE PART WHERE I
MOVED."
ref: genesis
```

---

## Run log

| Page | File | Verdict |
|------|------|---------|
All under `outputs/opening-sequence/2026-05-31/gemini-31-flash-image-preview/` (P1 in `style-probes/`).

| Page | Folder | Verdict |
|------|--------|---------|
| 1 THE MONUMENT | `style-probes/...page1-pushed-layout_402fab31` | ★★ Cold-open thesis splash — self-image punctured by CCTV reality + eye, static eating his face. |
| 2 CLARION | `01_page2-clarion-control_2ce521a0` | ★ Control at max — pristine symmetrical gold grid + boardroom dismantle. Tidy grid is correct here (the control peak). |
| 3 FIRST TEAR | `01_page3-first-tear_fea6d6a0` | ★★ Crack violates borders down the left; static creeps into a monitor; NB2 improvised good denial captions ("A slight, auditory hallucination" / "I am in control"). |
| 4 THE SOLVENT | `01_page4-the-solvent_412cda15` | ★★ Wide static band bisects the page = missing time the reader crosses; second open vial; "The solvent." |
| 5 DEAD CHANNEL | `01_page5-dead-channel_b8bcca71` | ★★ Full monitor grid, Vane's hands gripping the frames to hold them, "ERROR" timecodes, Witness calm in the clean dead channel. "there was never a boundary." |
| 6 FIND THEM | `01_page6-find-them_6afdedef` | ★★ Turns control outward (thriller launches); final dead-channel: Witness sets tomorrow's dose, looks at the reader — the keystone twist. |

**Overall:** coherent 6-page opening; the register grammar sequences across pages; Vane's face held
recognizably across separate genesis calls (better than expected for NB2). Caveats: lettering is
NB2-approximate; this is animatic/draft level — finals want a Pro pass (crisp text + tighter
identity-lock) or a separate lettering pass.

## Deepening pass — LAYOUT VARIETY (2026-05-31)

First critique of the v1 sequence: too many pages were grids-of-his-face / monitor grids. *The Filth*
has far more range (suspense size-modulation pg11, psychedelic splash pg13, mixed panel-shapes pg21,
fisheye splash pg23). Fix = **assign each beat a DISTINCT layout device** so the page architecture
has rhythm and no two adjacent pages share a shape.

| Beat | Layout device | Status |
|------|---------------|--------|
| 1 MONUMENT | full-bleed splash + puncturing insets | ✓ |
| 2 CLARION | rigid control grid (thematic — the one place the grid belongs) | ✓ keep |
| 3 FIRST TEAR | **suspense size-modulation** (wide → tightening cuts → dominant dread close-up + light-burst) | ✓ re-cut → `01_page3b-first-tear-suspense_be016c2c` (supersedes the v1 face-grid) |
| 4 THE SOLVENT | bisecting static band = missing time | ✓ |
| 5 DEAD CHANNEL | corrupting monitor grid | ✓ (2nd grid — non-adjacent, distinct job) |
| 6 FIND THEM | war-room montage | ✓ |
| DEEP DISSOLUTION (later beat) | **psychedelic full-page splash** (organic rainbow ego-melt) | ✓ `01_deep-dissolution-psychedelic_3c438c04` |

**Two-stage dissolution established:** clinical signal-glitch (early cracks) → psychedelic organic
plunge (the ego-death) → pure white signal-death. Reference vein for the psychedelic register:
*Filth* #1 pg 13. More layout devices still on the shelf: mixed panel-shapes (pg21), fisheye/axial
splash (pg23), close-up-intercut-over-wide-violence (pg1).
