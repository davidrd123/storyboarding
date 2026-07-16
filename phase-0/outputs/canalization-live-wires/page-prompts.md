# Canalization Live Wires — Full Prompts (single panel + full-page variants)

**Handoff spec for codex → GPT Image 2.** Do not generate from the riff-mcp side; this file is the prompt source. codex gens these (GPT Image 2 is free).

## How to use this file

- Each concept has **two variants to A/B**:
  - **A — Single dense panel:** the whole gag crammed into one editorial-cartoon frame (un-simplified, on purpose).
  - **B — Full page:** the same idea spread across a multi-panel comics page in the reference aesthetic (yellow caption boxes + speech balloons, recurring motif, closing aphorism banner). The grid carries the density so each cell stays clean — this is the render-safe variant for the busy ones.
- Prompts are self-contained (the style clause is pasted into each) — fire one at a time.
- **"forget simplifying first":** these are the full, un-trimmed versions. If a page garbles, fall back to fewer panels or gen panels separately and composite.

## GPT Image 2 notes / caveats

- **Aspect:** GPT Image 2 is happiest at 1:1, 3:2 landscape, or 2:3 portrait. Single panels → **3:2 landscape**; full pages → **2:3 portrait**; "4-panel strips" → **3:2 landscape** (true ultra-wide 3:1 isn't native — approximate, or stack two rows of two).
- **Lettering:** GPT Image 2 renders text well but long strings across many panels still slip — **verify spelling on review.** Underlined emphasis words are cosmetic; don't expect perfect underlines.
- **Character consistency across panels** is the main risk on the full-page variants — the same face must recur. Where the joke *is* a repeated face (Autogen), that's called out in-prompt; watch it on review.
- **Per-concept watch flags** are noted under each.

## Shared house-style clause (already pasted into every prompt below)

> Style: a weathered vintage graphic-novel / underground-comix look in a warm sepia-and-amber palette, heavy ink crosshatching over soft painterly washes, aged and lightly foxed paper texture, thin dark-brown panel borders with visible gutters; narration in cream rectangular caption boxes set in black all-caps lettering with key words underlined, dialogue in classic white speech balloons; grimy, melancholy, lit like dusk.

---

## 1. REPAVE IT, DOC? — *hysteresis / the scar*

*Top keeper. The single panel is dense-but-doable; the page variant gets the delayed strata-reveal a single frame can't.*

### 1A — Single dense panel

```
A single richly detailed editorial-cartoon panel. Style: a weathered vintage graphic-novel
look in a warm sepia-and-amber palette, heavy ink crosshatching over soft painterly washes,
aged foxed paper texture, thin dark-brown panel border; narration in cream caption boxes in
black all-caps lettering with key words underlined, dialogue in white speech balloons;
melancholy, lit like dusk.

Scene: a middle-aged man in shirtsleeves reclines on a classic tufted-leather analyst's
couch — but the couch sits right at the lip of a sheer cliff. The cliff face plunging away
beneath him is a geological cross-section of the man himself: his own face and body strata
exposed in the rock layers. A bespectacled therapist in a cardigan stands at the very edge
with a long wooden pointer, reading the layers like a field geologist, notepad in hand.

The exposed strata are labeled in small caption-box fine print down the cliff: a thin top
band "THIS WEEK'S MOOD — TOPSOIL, WON'T SURVIVE"; below it "CANALIZED 2019-23 — THICKENED
BY USE"; a thick dark band "ASSIMILATED"; a jagged glowing-red FAULT LINE cutting through
everything "THE YEAR IT ALL CHANGED — CANNOT BE UN-LAID"; basement bedrock "THE FIRST
DESCENT. STILL DOWN THERE."

Caption box top-left: "THERE'S A LOT OF HISTORY IN THAT CLIFF." The man, sheepish,
half-raising a hand, speech balloon: "CAN'T WE JUST... REPAVE IT?" The therapist, deadpan,
tapping the red fault line with the pointer, speech balloon: "FORMATION IS IRREVERSIBLE.
THE VALLEY YOU DUG STAYS DUG." Wide landscape 3:2, high resolution; ensure all lettering is
legible and correctly spelled.
```

### 1B — Full page

```
A full vintage graphic-novel PAGE, vertical portrait format. Style: a weathered vintage
graphic-novel look in a warm sepia-and-amber palette, heavy ink crosshatching over soft
painterly washes, aged foxed paper texture, thin dark-brown panel borders with visible
gutters; narration in cream caption boxes in black all-caps lettering with key words
underlined, dialogue in white speech balloons; melancholy, lit like dusk.

Top establishing panel, wide, spanning the page: a man reclining on a tufted-leather
analyst's couch perched at the lip of a sheer cliff at dusk; the cliff below is a
cross-section of the man's own body in the rock; a bespectacled therapist stands at the
edge with a long pointer. Caption boxes: "THERE'S A LOT OF HISTORY IN THAT CLIFF." /
"BUT YOU CAN'T REPAVE A SCAR." Man's balloon: "CAN'T WE JUST... REPAVE IT?"

Below, a vertical stack of four narrow close-up cells descending the cliff, each showing one
rock stratum with the therapist's pointer touching it and a cream caption box:
Cell 1 (topsoil): "THIS WEEK'S MOOD. TOPSOIL — WON'T SURVIVE THE SEASON."
Cell 2 (pale layered band): "2019-23: SAID IT YEARLY, CANALIZED, THE MUSCLE THICKENED BY USE."
Cell 3 (thick dark band): "ASSIMILATED — NO LONGER NEEDS THE OCCASION THAT EVOKED IT."
Cell 4 (glowing-red jagged fault line cutting the rock): "THE YEAR IT ALL CHANGED. CANNOT BE
UN-LAID."

Bottom banner strip with a small trowel icon at the left and a jagged fault-line icon at the
right, flanking black all-caps text: "FORMATION IS IRREVERSIBLE. THE VALLEY YOU DUG STAYS
DUG." Recurring motif: the therapist's wooden pointer appears in every cell. Vertical
portrait page 2:3, high resolution; all lettering legible and correctly spelled.
```

**Watch:** keep the same man's face on the couch and in the cross-section consistent.

---

## 2. THE METAPHYSICAL REPO MAN — *teleology on credit*

### 2A — Single dense panel

```
A single editorial-cartoon panel. Style: a weathered vintage graphic-novel look in a warm
sepia-and-amber palette, heavy ink crosshatching over soft painterly washes, aged foxed
paper texture, thin dark-brown panel border; narration in cream caption boxes in black
all-caps lettering with key words underlined, dialogue in white speech balloons; grimy,
melancholy, lit like dawn.

Scene: dawn on a suburban front stoop. A schlubby man in a striped bathrobe stands frozen in
his open doorway, coffee mug halfway to his open mouth, horror dawning on his face. Facing
him on the stoop is a stern bailiff dressed in a classical white toga worn over a hi-vis
safety vest (Aristotle moonlighting as a debt collector), clipboard in hand. Beside the
bailiff a hand-truck is already stacked with cardboard moving boxes labeled in marker:
"THE VALLEY DRAWS THE BALL", "IT WANTS EQUILIBRIUM", "IT'S TRYING TO PERSIST (x400)". A
"FINAL NOTICE" is taped to the door, its fine print readable: "RE: OUTSTANDING TELEOLOGICAL
BALANCE. AMOUNT DUE: ONE (1) ACCOUNT OF HOW ABSENCE CAUSES ANYTHING."

Bailiff, flat, reading the clipboard, balloon: "SAYS HERE YOU'VE BEEN RUNNING
END-DIRECTEDNESS ON CREDIT SINCE TUESDAY." Schlub, flustered, balloon: "BUT THE ATTRACTOR
PULLS — EVERYONE SAYS THE VALLEY PULLS—" Bailiff, deadpan, balloon: "A TELOS WITH THE
METAPHYSICS FILED OFF. WE'RE REPOSSESSING THE LOT." Caption box top-left: "THEY CAME FOR THE
CAUSES AT DAWN." Wide landscape 3:2, high resolution; all lettering legible and correctly
spelled.
```

### 2B — Full page (4-panel strip)

```
A vintage graphic-novel four-panel comic strip, aged sepia paper, heavy ink. Style: warm
sepia-and-amber palette, heavy ink crosshatching over painterly washes, foxed paper texture,
thin dark-brown panel borders with visible gutters; cream caption boxes in black all-caps
lettering with key words underlined, white speech balloons; grimy, dawn light. Four equal
panels left to right.

Panel 1 — establishing: a schlub in a striped bathrobe frozen in his open doorway at dawn,
coffee mug halfway up, facing a stern bailiff in a toga over a hi-vis vest holding a
clipboard. Caption box: "THEY CAME FOR THE CAUSES AT DAWN." Bailiff balloon: "YOU'VE BEEN
RUNNING END-DIRECTEDNESS ON CREDIT."

Panel 2 — the loaded hand-truck of cardboard boxes labeled "THE VALLEY DRAWS THE BALL",
"IT WANTS EQUILIBRIUM", "IT'S TRYING TO PERSIST (x400)". Caption box: 'EVERY "IT TENDS
TOWARD" — BORROWED.'

Panel 3 — close-up of the "FINAL NOTICE" taped to the door: "AMOUNT DUE: ONE (1) ACCOUNT OF
HOW ABSENCE CAUSES ANYTHING." Schlub balloon from off-panel: "BUT THE ATTRACTOR PULLS—"

Panel 4 — the bailiff wheeling the hand-truck away down the path, the schlub small in the
doorway behind. Bailiff balloon: "A TELOS WITH THE METAPHYSICS FILED OFF. PAY UP." Caption
box bottom: "PAY THE TAB OR LOSE THE PURPOSE." Wide landscape 3:2 (or two rows of two if the
strip is too thin). High resolution; all lettering legible and correctly spelled.
```

**Watch:** keep the same bailiff and same schlub across all four panels.

---

## 3. AUTOGEN, INC. — EMPLOYEE OF THE MONTH — *teleodynamics / the self that maintains itself*

*The gag IS a repeated face. That's the make-or-break — call it out hard in the prompt.*

### 3A — Single dense panel

```
A single editorial-cartoon panel. Style: a weathered vintage graphic-novel look in a warm
sepia-and-amber palette, heavy ink crosshatching over soft painterly washes, aged foxed
paper texture, thin dark-brown panel border; narration in cream caption boxes in black
all-caps lettering, dialogue in white speech balloons; fluorescent-lit, beige, weary.

Scene: a cramped beige office cubicle under flat fluorescent light. A weary office drone with
a loosened tie slumps in his chair beside a single dying desk plant. A sticky note on his
monitor reads, fully legible: "MAINTAIN THE CONDITIONS OF YOUR OWN EMPLOYMENT." On the
cubicle's back wall a whiteboard shows a looping flowchart whose arrows curve all the way
back on themselves: "AUTOCATALYSIS -> SELF-ASSEMBLY -> RECIPROCAL MAKING ->" (the last arrow
curving back to the first). To the right hangs an "EMPLOYEE OF THE MONTH" wall of framed
portraits — every single frame is the SAME man's face. A manager leans in over the cubicle
wall to congratulate him, and the manager has the EXACT SAME FACE as the drone.

CRITICAL: the drone, the manager, and every employee-of-the-month portrait are all the same
identical person — the same face repeated everywhere in the frame.

Manager-him, thumbs up, balloon: "OUTSTANDING WORK STAYING EMPLOYED. THAT IS THE JOB."
Drone-him, hollow, balloon: "...I KNOW." A small wall plaque: "OUR ONLY PRODUCT IS CONTINUING
TO EXIST. EST. ~3.8 BILLION YEARS AGO." Caption box top-left: "I HAVE ONE JOB. AND ONE BOSS.
AND ONE EMPLOYEE." Wide landscape 3:2, high resolution; all lettering legible and correctly
spelled.
```

### 3B — Full page (4-panel strip)

```
A vintage four-panel comic strip, aged sepia paper, heavy ink. Style: warm sepia-and-amber
palette, heavy ink crosshatching, foxed paper texture, thin dark-brown panel borders with
gutters; cream caption boxes in black all-caps lettering, white speech balloons; weary,
fluorescent. CRITICAL: the worker and the manager are the SAME identical man — the same face
recurs in every panel.

Panel 1 — establishing: a weary office drone slumped in a beige cubicle, dying desk plant; a
whiteboard behind him with a looping flowchart "AUTOCATALYSIS -> SELF-ASSEMBLY -> RECIPROCAL
MAKING ->" curving back on itself; a monitor sticky note: "MAINTAIN THE CONDITIONS OF YOUR
OWN EMPLOYMENT." Caption box: "MY JOB HAS ONE TASK."

Panel 2 — a manager with the same face as the drone leans over the cubicle wall, thumbs up.
Caption box: "AND ONE BOSS." Manager balloon: "OUTSTANDING WORK STAYING EMPLOYED. THAT IS
THE JOB."

Panel 3 — the "EMPLOYEE OF THE MONTH" wall: a row of framed portraits, every one the same
man's face. Caption box: "AND ONE EMPLOYEE." A plaque visible: "OUR ONLY PRODUCT IS
CONTINUING TO EXIST."

Panel 4 — tight close-up of the drone's hollow, tired face. Balloon: "...I KNOW." Caption box
bottom: "THE SELF IS A COMPANY THAT MAKES ONLY ITSELF. EST. ~3.8 BILLION YEARS AGO." Wide
landscape 3:2 (or two rows of two). High resolution; the same face must recur in all four
panels; all lettering legible and correctly spelled.
```

**Watch:** the same-face repetition is the entire joke — if GPT Image 2 drifts the faces apart, reroll; the wall of identical portraits is the backup that sells it even on slight drift.

---

## 4. THE TUG-OF-WAR OVER A SELF — *near-criticality*

### 4A — Single dense panel

```
A single editorial-cartoon panel. Style: a weathered vintage graphic-novel look in a warm
sepia-and-amber palette, heavy ink crosshatching over soft painterly washes, aged foxed
paper texture, thin dark-brown panel border; narration in cream caption boxes in black
all-caps lettering, dialogue in white speech balloons; dramatic, lit like dusk.

Scene: a huge wall-mounted industrial gauge dominates the frame, its big needle quivering.
The dial face is labeled: far-left zone "OVER-CANALIZED — RIGID, FIXED, TECHNICALLY DEAD";
far-right zone "TOTAL EROSION — FORMLESS, NO SELF AT ALL"; and a razor-thin green wedge in
the dead center "NEAR-CRITICAL — ENOUGH SHAPE TO ACT, ENOUGH GIVE TO CHANGE YOUR MIND." A
sweat-drenched everyperson in the center grips the gauge's lever with both hands, legs
braced, straining to hold the needle on the green sliver. On the left, a rigid man in a
starched collar and suit HEAVES the lever leftward; on the right, a loose tie-dyed hippie
drags it rightward. The needle is losing, pegged hard left and shuddering.

Rigid suit, balloon: "STAY THE COURSE! DISCIPLINE!" Tie-dye hippie, balloon: "JUST GOOO WITH
THE FLOWWW, MAN." Center everyperson, gritted teeth, balloon: "I'M TRYING TO HOLD THE GREEN—"
A riveted warning plate bolted to the machine, fine print readable: "CAUTION: DO NOT
OVER-TIGHTEN. NEGATIVE CAPABILITY SOLD SEPARATELY. THIS IS THE ONLY HEALTHY SETTING AND IT
WILL NOT HOLD STILL." Caption box top-left: "THERE IS EXACTLY ONE HEALTHY SETTING." Wide
landscape 3:2, high resolution; all lettering legible and correctly spelled.
```

### 4B — Full page

```
A vintage graphic-novel PAGE, vertical portrait format. Style: warm sepia-and-amber palette,
heavy ink crosshatching over painterly washes, foxed paper texture, thin dark-brown panel
borders with gutters; cream caption boxes in black all-caps lettering, white speech balloons;
dramatic, dusk.

Top hero panel, large: a huge wall-mounted industrial gauge, needle pegged hard left and
shuddering; the dial labeled left "OVER-CANALIZED — RIGID, TECHNICALLY DEAD", a thin green
wedge in the center "NEAR-CRITICAL", right "TOTAL EROSION — NO SELF AT ALL". A sweat-drenched
everyperson grips the lever in the center, legs braced. Caption box: "THERE IS EXACTLY ONE
HEALTHY SETTING."

A row of three close-up cells beneath:
Cell 1 — a rigid suited man in a starched collar heaving the lever left. Balloon: "STAY THE
COURSE! DISCIPLINE!"
Cell 2 — the everyperson's straining, sweating face. Balloon: "I'M TRYING TO HOLD THE GREEN—"
Cell 3 — a loose tie-dyed hippie dragging the lever right. Balloon: "JUST GOOO WITH THE
FLOWWW, MAN."

Bottom banner strip with a clenched-fist icon at the left and an open-hand icon at the right,
flanking black all-caps text: "POISED BETWEEN RIGID AND FORMLESS — AND IT WILL NOT HOLD
STILL." A small riveted warning plate in the corner: "NEGATIVE CAPABILITY SOLD SEPARATELY."
Vertical portrait page 2:3, high resolution; all lettering legible and correctly spelled.
```

---

## 5. THE BASIN SAFARI — *the full attractor typology* (FULL, not simplified)

*This is the clearest A/B in the set: 5A is the render-risk version (four individuated figures in one frame — the De-Canalizers clutter trap); 5B is the rescue (one specimen per cell). Gen both, compare.*

### 5A — Single dense panel (full 4 specimens)

```
A single richly detailed editorial-cartoon panel. Style: a weathered vintage graphic-novel
look in a warm sepia-and-amber palette, heavy ink crosshatching over soft painterly washes,
aged foxed paper texture, thin dark-brown panel border; narration in cream caption boxes in
black all-caps lettering, dialogue in white speech balloons; dusk, melancholy.

Scene: a khaki-clad nature guide in a pith helmet leads a small tour group along a raised
wooden boardwalk through a rolling dusk landscape dotted with people, each stuck in their own
labeled valley, with small staked placards beside each one. The guide points; the tourists
peer and whisper.

The four specimens, each in their own dip with a readable placard:
- a comfortable old man settled in a smooth, deeply worn groove; placard: 'THE SELF-DEEPENING
  ATTRACTOR. DOMESTICATES EASILY. KNOWN LOCALLY AS "CHARACTER."'
- a man at the bottom of a deep pit lined with glowing phone screens; placard: "THE TRAP. DO
  NOT APPROACH. FROM DOWN THERE, NO OTHER VALLEY IS VISIBLE."
- a woman jogging an endless loop between two hollows, never landing; placard: "THE LIMIT
  CYCLE (THE AMBIVALENCE). NOT INDECISION — A STABLE ORBIT."
- a faint, half-transparent fading figure in a flattening dip; placard: "THE EROSION. YOU
  WON'T NOTICE IT LEAVE."

A tourist, whispering, balloon: "DO THEY KNOW WE'RE HERE?" The guide, warm, balloon: "FROM
THE BOTTOM, NO OTHER VALLEY IS VISIBLE. MIND THE BOARDWALK — IT'S HOW THE REST OF US AVOID
BECOMING EXHIBITS." Caption box top-left: "THERE'S A LOT OF PEOPLE DOWN IN THOSE VALLEYS.
THEY CALL IT CHARACTER." Wide landscape 3:2, high resolution; all lettering legible and
correctly spelled.
```

### 5B — Full page (rescue: one specimen per cell)

```
A vintage graphic-novel PAGE styled like a nature-documentary field guide, vertical portrait
format. Style: warm sepia-and-amber palette, heavy ink crosshatching over painterly washes,
foxed paper texture, thin dark-brown panel borders with gutters; cream caption boxes in black
all-caps lettering, white speech balloons; dusk, melancholy.

Top establishing panel, wide: a khaki-clad guide in a pith helmet leads a small tour group
along a raised wooden boardwalk receding into a rolling dusk landscape dotted with distant
stuck figures. Caption boxes: "THERE'S A LOT OF PEOPLE DOWN IN THOSE VALLEYS." / "THEY CALL
IT CHARACTER." A tourist balloon: "DO THEY KNOW WE'RE HERE?"

A strip of four specimen close-up cells, each one person in their own valley with a staked
placard, the guide's pointing hand recurring at the edge of each:
Cell 1 — a comfortable old man in a smooth worn groove; placard: "THE SELF-DEEPENING
ATTRACTOR. DOMESTICATES EASILY."
Cell 2 — a man in a deep pit lined with glowing phone screens; placard: "THE TRAP. FROM DOWN
THERE, NO OTHER VALLEY IS VISIBLE."
Cell 3 — a woman jogging an endless loop between two hollows; placard: "THE LIMIT CYCLE. NOT
INDECISION — A STABLE ORBIT."
Cell 4 — a faint, half-transparent fading figure in a flattening dip; placard: "THE EROSION.
YOU WON'T NOTICE IT LEAVE."

Bottom banner strip with a topographic contour-line icon at the left and a small
boardwalk-plank icon at the right, flanking black all-caps text: "FROM THE BOTTOM, NO OTHER
VALLEY IS VISIBLE. MIND THE BOARDWALK." Recurring motif: the raised wooden boardwalk runs
through every panel. Vertical portrait page 2:3, high resolution; all lettering legible and
correctly spelled.
```

**Watch:** 5A is expected to clutter (it's the test); 5B is the safe bet. The four specimens must each read as visually distinct states.

---

## 6. THE UNIVERSE PROVIDES™ — LIVE SEMINAR — *survivorship bias*

*Flagged off-core-theme (this is a stats/survivorship point, more tangential to the canalization thread than 1-5). Kept because the writing is sharp. The whole gag rests on the translucent ghost-crowd reading as "the deleted misses" — lean on the fine-print banner to anchor it.*

### 6A — Single dense panel

```
A single editorial-cartoon panel. Style: a weathered vintage graphic-novel look in a warm
sepia-and-amber palette, heavy ink crosshatching over soft painterly washes, aged foxed paper
texture, thin dark-brown panel border; narration in cream caption boxes in black all-caps
lettering, dialogue in white speech balloons; stage-lit gold fading into darkness.

Scene: a slick manifestation guru in a headset mic stands on a TED-style stage, arms flung
wide, presenting a giant glowing testimonial wall. The front rows of the audience are lit
warm gold, hopeful, nodding and scribbling notes. The testimonial wall shows three beaming
spotlit faces with five-star ratings and quotes: "I PICTURED THE HOUSE AND IT APPEARED!
*****", "I JUST KNEW IT'D WORK OUT — AND IT DID! *****", "THE UNIVERSE HEARD ME! *****".

The reveal (the gag): the back rows and everything beyond the stage lights are packed with a
vast grey crowd of TRANSLUCENT GHOST attendees — everyone who did exactly the same thing and
got nothing — un-spotlit, no quote bubbles, fading off the edges into darkness. A stage banner
along the bottom in tiny print: "SURVIVORS PICTURED. NON-SURVIVORS NOT AVAILABLE FOR COMMENT.
TESTIMONIALS REFLECT BASE RATES WITH THE MISSES DELETED."

Guru, beaming, balloon: "IT WORKS FOR EVERYONE WHO TRULY BELIEVES!" Caption box top-left:
"THE UNIVERSE PROVIDES — LIVE SEMINAR." Wide landscape 3:2, high resolution; the translucent
grey ghost-crowd must clearly read as faded, deleted non-survivors behind the gold believers;
all lettering legible and correctly spelled.
```

### 6B — Full page (4-panel strip)

```
A vintage four-panel comic strip, aged sepia paper, heavy ink. Style: warm sepia-and-amber
palette, heavy ink crosshatching, foxed paper texture, thin dark-brown panel borders with
gutters; cream caption boxes in black all-caps lettering, white speech balloons; stage-lit
gold fading into darkness.

Panel 1 — establishing: a slick manifestation guru in a headset mic on a TED-style stage,
arms flung wide, front rows lit warm gold and adoring. Caption box: "THE UNIVERSE PROVIDES."
Guru balloon: "IT WORKS FOR EVERYONE WHO TRULY BELIEVES!"

Panel 2 — the glowing testimonial wall, three beaming spotlit faces with quotes: "I PICTURED
IT AND IT APPEARED! *****", "I JUST KNEW IT'D WORK! *****", "THE UNIVERSE HEARD ME! *****".
Caption box: "THE WINNERS GET A MICROPHONE."

Panel 3 — a wide pull-back to behind the stage lights, revealing a vast grey crowd of
translucent ghost-attendees fading into darkness, no spotlights, no quotes. Caption box:
"THE REST DON'T."

Panel 4 — close-up of the stage banner's fine print: "SURVIVORS PICTURED. NON-SURVIVORS NOT
AVAILABLE FOR COMMENT. RESULTS MAY BE REGRESSION TO THE MEAN." Caption box bottom:
"TESTIMONIALS REFLECT BASE RATES WITH THE MISSES DELETED." Wide landscape 3:2 (or two rows of
two). High resolution; the ghost crowd in panel 3 must read as faded deleted non-survivors;
all lettering legible and correctly spelled.
```

**Watch:** ghost-crowd readability (panel 3 / the reveal) and the fine-print spelling.

---

## 7. THE REDACTION — *the apophatic self / via negativa (the absential, defined by what it is not)*

*New spec. Two-figure scene → low render risk. Text-heavy (redaction bars + legible negations) → verify spelling. Black bars are easy to render (solid rectangles); the joke is that the legible parts are all negations.*

### 7A — Single dense panel

```
A single editorial-cartoon panel. Style: a weathered vintage graphic-novel look in a warm
sepia-and-amber palette, heavy ink crosshatching over soft painterly washes, aged foxed paper
texture, thin dark-brown panel border; narration in cream caption boxes in black all-caps
lettering, dialogue in white speech balloons; dim, lamplit, scholarly.

Scene: a dim archive reading room lit by a single green-shaded lamp. Two scholars hunch over
a massive open document on a library table: a young, eager scholar with a magnifying glass and
an old, weary scholar in spectacles. The document is titled "THE TRUE SELF — COMPLETE &
UNABRIDGED", but nearly every line is a solid black REDACTION bar. Only fragments of negation
remain legible between the bars: "IT IS NOT [REDACTED]", "NOR THE [REDACTED] EITHER",
"DEFINITELY NOT [REDACTED]", and at the foot "[REMAINDER CLASSIFIED]". A purple ink stamp
across the corner: "APOPHATIC — DECLASSIFICATION DENIED."

Young scholar, eager, tapping a black bar, balloon: "BUT WHAT'S UNDER THE BLACK BARS?" Old
scholar, deadpan, balloon: "THAT'S THE ONLY PART THAT'S REAL. YOU READ IT BY SUBTRACTION."
Caption box top-left: "WE HAVE THE COMPLETE WORKS OF THE SELF. MOSTLY IN BLACK BARS." Wide
landscape 3:2, high resolution; all lettering legible and correctly spelled.
```

### 7B — Full page

```
A vintage graphic-novel PAGE, vertical portrait format. Style: warm sepia-and-amber palette,
heavy ink crosshatching over painterly washes, foxed paper texture, thin dark-brown panel
borders with gutters; cream caption boxes in black all-caps lettering, white speech balloons;
dim, lamplit, scholarly.

Top establishing panel, wide: a dim archive reading room with a green-shaded lamp; two
scholars — a young eager one with a magnifying glass, an old weary one in spectacles — hunch
over a massive open tome titled "THE TRUE SELF — COMPLETE & UNABRIDGED", nearly every line a
solid black redaction bar. Caption boxes: "WE HAVE THE COMPLETE WORKS OF THE SELF." / "MOSTLY
IN BLACK BARS."

A strip of four close-up cells:
Cell 1 — a redacted passage, only the negation legible: "IT IS NOT [REDACTED]." Caption:
"EVERY POSITIVE CLAIM — STRUCK OUT."
Cell 2 — the magnifying glass over another line: "NOR THE [REDACTED] EITHER." Caption: "WHAT
REMAINS IS ONLY WHAT IT ISN'T."
Cell 3 — the young scholar peeling up a black bar with tweezers, finding only ANOTHER black
bar beneath it. Balloon: "BUT WHAT'S UNDER THE BARS?"
Cell 4 — the old scholar's deadpan face. Balloon: "THAT'S THE ONLY PART THAT'S REAL. YOU GET
IT BY SUBTRACTION."

Bottom banner strip with a black redaction-bar icon at the left and a magnifying-glass icon at
the right, flanking black all-caps text: "EVERYTHING TRUE ABOUT YOU IS UNDER A BLACK BAR. YOU
READ IT BY WHAT IT REFUSES TO SAY." A purple stamp in the corner: "DECLASSIFICATION DENIED."
Vertical portrait page 2:3, high resolution; all lettering legible and correctly spelled.
```

---

# Full-page re-cuts of the five already-rendered panels

*These five were already rendered by codex as single panels (the `.png` files in this folder = their "A" variant). Below is a **full-page "B" variant** for each, applying the comics-page structure (caption boxes, sequential cells, recurring motif, closing banner).*

*Register note: each re-cut **keeps that panel's native art look** (what made the original work) rather than the sepia house style — so this is a fair test of "does the page format help THIS concept." If you'd rather unify the whole canalization set in the sepia comics look, swap in the house-style clause from the top of the file.*

*Two of these bake in fixes for problems flagged in codex's renders: **Lost** (the face must be the ground he's on, not beside him) and **De-Canalizers** (one "HI, GREG", deeper individuated grooves — the clutter rescue).*

## 8. LOST: MY TRUE WILL — *the will is the landscape* — full page

*Fix baked in: a final pull-back reveal makes the terrain-IS-his-face explicit (codex's single panel read as "face beside him").*

```
A graphic-novel PAGE, vertical portrait format, night scene in a heavy-ink editorial-cartoon
register — moody nocturne, warm flashlight glow against cool blue-black dark; cream caption
boxes in black all-caps lettering, white speech balloons.

Top establishing panel, wide: a man in plaid pajamas crawls on hands and knees with a
flashlight across a yard at night — scattered rocks, a mailbox, a welcome mat; a telephone
pole bears a flyer "LOST: MY TRUE WILL" with sad untaken tear-off tabs; a crescent moon and a
lit house far off. Caption boxes: "I'VE LOOKED EVERYWHERE." / "UNDER THE MAT. IN THE MAILBOX.
NOTHING." Balloon: "WHERE DID I PUT IT?"

A strip of small search-beat cells: 1) the flashlight under a lifted rock, empty; 2) peering
into the open mailbox, empty; 3) lifting the welcome mat, empty; 4) the flyer's untaken
tear-tabs fluttering in the dark.

Bottom reveal panel, wide: a pull-back showing that the rolling hills he has been crawling on
ARE his own giant sleeping FACE — the flashlight beam falls directly across his own cheekbone,
his crawling body small on the slope of his own brow. Caption box: "HE WAS CRAWLING ON IT THE
WHOLE TIME."

A thin closing banner with a flashlight icon at the left and a contour-line-face icon at the
right, flanking black all-caps text: "THE WILL ISN'T LOST. IT'S THE GROUND YOU'RE STANDING
ON." Recurring motif: the flashlight beam in every cell. Vertical portrait page 2:3, high
resolution; all lettering legible and correctly spelled.
```

## 9. THE HABIT IN THE WILD — *the self-deepening trap* — full page

```
A nature-documentary field-guide PAGE, vertical portrait format, in a painterly illustrated
cross-section style — lush naturalistic color above ground, warm earthy strata below;
parchment caption boxes in black all-caps serif; no speech balloons (documentary captions
only).

Top establishing panel, wide: a lush green valley surface at golden hour, the small mouth of
a narrow well, and other green valleys glowing temptingly in the distance. Caption: "THE
COMMON HABIT BEGINS AT THE SURFACE, LIKE EVERYTHING ELSE."

A vertical stack of cells descending the shaft:
Cell 1 — a shallow scuff in the soil: "FIRST DESCENT — BARELY A DENT."
Cell 2 — a deeper worn groove: "REPEATED DAILY."
Cell 3 — a narrow shaft, the upper ladder rungs rotted away: "THE LADDER ROTS FROM DISUSE."
Cell 4 — the bottom: a soft, big-eyed doughy creature, a small "YOU ARE HERE" arrow pointing
down at it, the daylight above now a tiny distant dot. Captions: "IT DEEPENED THE BASIN WITH
EVERY DESCENT." / "FROM HERE, NO OTHER VALLEY IS VISIBLE." / "IT BELIEVES THIS IS THE WORLD."

A thin closing banner with a small spade icon at the left and a topographic-contour icon at
the right, flanking black all-caps text: "EVERY DESCENT DUG THE WALL IT CANNOT SEE OVER."
Recurring motif: the shrinking dot of daylight at the top of each descending cell. Vertical
portrait page 2:3, high resolution; all lettering legible and correctly spelled.
```

## 10. SOME ASSEMBLY REQUIRED: A SELF — *charging vs. discharging* — full page

*Stays in flat-pack instruction register (NOT sepia), like the original render. A fuller manual: exploded view + numbered S-curve + parts legend.*

```
A full flat-pack furniture INSTRUCTION-SHEET page, vertical portrait format, clean off-white
background, simple black-and-blue line art, the deadpan wordless register of an IKEA manual
(NOT the sepia comics look). Title bar at top: "SOME ASSEMBLY REQUIRED: A SELF", with a small
person icon, a manual icon, a 3-of-5-star difficulty rating, and "TIME: LIFELONG".

Top: an exploded-view diagram of a little featureless assembly mannequin's parts floating
apart — a blue "SELF" block, a yellow "END" block, a coiled "ACT" spring, and a dashed empty
outline labeled "1 ABSENCE".

A numbered S-curve of assembly steps:
Step 1 — the mannequin holds "SELF" and "END" with a dashed "GAP" between them, a "?" above
its head.
Step 2 (green check) — the mannequin inserts the "ACT" spring to hold the gap OPEN; the pieces
vibrate with little motion marks; the mannequin smiles.
Step 3 (red X) — the mannequin squeezes a glue bottle labeled "TOO SOON" and fuses the pieces
shut; they slump, inert; the mannequin frowns with a sweat drop.
Step 4 (green check) — the finished correct figure stands with the gap still held open,
faintly glowing with potential.

Footer parts legend: "SELF x1", "END x1", "ACT (spring) x1", "1 ABSENCE (do not discard)"
drawn as an empty dashed box, and "LUST OF RESULT — discard" drawn as a lonely leftover screw.
A small boxed customer-service note: "IF SELF COLLAPSES, DO NOT RETURN. RE-OPEN THE GAP."
Vertical portrait page 2:3, high resolution; all lettering legible and correctly spelled.
```

## 11. DE-CANALIZERS ANONYMOUS — *hysteresis / drift* — full page

*This is the clutter rescue: codex's single panel had ~6 "HI, GREG" bubbles and shallow furrows. The page gives each attendee their own cell with a distinct, deep groove, and uses "HI, GREG" exactly once.*

```
A graphic-novel PAGE, vertical portrait format, in a heavy-ink editorial-cartoon register, a
drab fluorescent-lit church-basement palette; cream caption boxes in black all-caps lettering,
white speech balloons.

Top establishing panel, wide: a church-basement support-group room — a circle of metal folding
chairs, a "ONE DAY AT A TIME" banner, a sad coffee urn, and a whiteboard reading "STEP 1: THE
VALLEY STAYS DUG" with a facilitator beside it. Caption box: "WELCOME TO DE-CANALIZERS
ANONYMOUS."

A strip of cells, one attendee and their own personal groove each (so each reads cleanly):
Cell 1 — a standing man mid-share, hand half-raised. Balloons: "I HAVEN'T BEEN TO THAT VALLEY
IN YEARS..." / "...AND I STILL CAN'T LEAVE."
Cell 2 — a man whose folding chair has sunk deep into a rut that travels with him. Caption:
"THE RUT FOLLOWS HIM TO EVERY MEETING."
Cell 3 — a woman dragging a long, deep worn valley behind her across the floor like a tail.
Caption: "SHE BROUGHT IT WITH HER."
Cell 4 — a man pacing a tight circle worn into the linoleum, unable to sit. Caption: "HE CAN'T
STOP CIRCLING."

One small group-response balloon shared across the room, used exactly ONCE: "HI, GREG."

A thin closing banner with a folding-chair icon at the left and a worn-groove icon at the
right, flanking black all-caps text: "YOU CAN LEAVE THE VALLEY. THE VALLEY DOESN'T LEAVE YOU."
Recurring motif: the "STEP 1: THE VALLEY STAYS DUG" whiteboard visible behind every cell.
Vertical portrait page 2:3, high resolution; all lettering legible and correctly spelled.
```

## 12. PICK A DOOR! — *negative capability* — full page

*Fix baked in: codex's single panel had the three "half-formed lives" reading as generic vignettes. Giving each door its own cell lets the superposed life actually read.*

```
A graphic-novel PAGE, vertical portrait format, in a vivid heavy-ink editorial-cartoon
register — glitzy saturated game-show color, spotlights and confetti; cream caption boxes in
black all-caps lettering, white speech balloons.

Top establishing panel, wide: a glitzy game-show stage under a bulb-lit marquee reading
"PICK! PICK! PICK!"; a frantic studio audience on its feet pointing; a manic host in a sequin
suit center stage; a serene poet at a podium labeled "POET" with a red buzzer. Caption box:
"THE ONLY GAME WHERE WINNING MEANS CHOOSING."

A row of three door cells, each door clearly showing one flickering, half-drawn life inside:
Cell 1 — Door One glows over a ghostly, half-formed family kitchen. Caption: "A LIFE,
HALF-DRAWN."
Cell 2 — Door Two glows over a ghostly, half-formed city career. Caption: "ANOTHER, JUST AS
REAL."
Cell 3 — Door Three glows over a ghostly, half-formed quiet cabin. Caption: "ALL OF THEM,
STILL POSSIBLE."

Two close-up cells beneath: the host, sweating, balloon "JUST LOCK ONE IN!"; the poet, eyes
half-closed and calm, balloon "I'D RATHER KEEP ALL THREE ALIVE."

A thin closing banner with a game-show buzzer icon at the left and a question-mark icon at the
right, flanking black all-caps text: "PICK ONE AND THE OTHER TWO DIE. HE'D RATHER KEEP THEM
ALIVE." Recurring motif: the three glowing doors. Vertical portrait page 2:3, high resolution;
all lettering legible and correctly spelled.
```

---

## Full set, at a glance

| # | Concept | Single (A) | Page (B) | Register |
|---|---|---|---|---|
| 1 | Repave It, Doc? | ✓ | ✓ cliff-strata page | sepia comics |
| 2 | Metaphysical Repo Man | ✓ | ✓ 4-panel strip | sepia comics |
| 3 | Autogen, Inc. | ✓ | ✓ 4-panel strip | sepia comics |
| 4 | Tug-of-War | ✓ | ✓ hero-dial page | sepia comics |
| 5 | Basin Safari | ✓ | ✓ per-cell page | sepia comics |
| 6 | The Universe Provides™ | ✓ | ✓ 4-panel strip | sepia comics |
| 7 | The Redaction | ✓ | ✓ archive page | sepia comics |
| 8 | Lost: My True Will | already rendered | ✓ reveal page | night ink |
| 9 | The Habit in the Wild | already rendered | ✓ descent page | painterly nature-doc |
| 10 | Some Assembly Required | already rendered | ✓ full manual | flat-pack / IKEA |
| 11 | De-Canalizers Anonymous | already rendered | ✓ rescue page | ink editorial |
| 12 | Pick a Door! | already rendered | ✓ per-door page | glitzy ink |
