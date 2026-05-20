# Test Beds

Bespoke micro-scenarios designed to maximally exercise one joint at a time. Distinct from test *projects* (David's compositing class, Ben's pitch books) — those are downstream consumers; these are diagnostic probes.

**Design principles:**

- **One variable per bed.** Pin five things, vary one. A bed that varies three things produces ambiguous failures.
- **Cheap to run.** Most beds are 3–4 generations, ~$1–2 at `gpt-image-2` pricing. The whole bed set should be runnable in an afternoon.
- **Clearly readable as pass/fail.** Before generating, write down what success and failure look like. If you can't articulate that, the bed isn't sharp enough yet.
- **Tied to a probe.** Every bed addresses at least one of the five mechanisms in `PHASE_A_GOALS.md`. If a candidate doesn't, it's a project not a bed.
- **Output is the lesson, not the panels.** Each run produces a markdown note: what was tried, what came back, what it tells us. Panels are evidence; the lesson is the deliverable.

---

## Coverage map

| Bed | Probes (`PHASE_A_GOALS.md` §) | Joint stressed |
|---|---|---|
| 1. Director-style close-up disambiguation | §3 | Image refs vs prose for underspecified DSL slots |
| 2. Identity preservation across lighting | §1, §3 | Style/identity refs holding under environmental variation |
| 3. Sub-location discovery moment | §5 | When and how "same place" becomes "different place" |
| 4. Costume-state propagation | §2 | What state survives across panels without re-mention |
| 5. Bubble-up edit propagation | §4 | Upstream revisions reaching downstream panels |
| 6. Multi-reference assembly stress | §3 | Combining many refs without leakage between them |
| 7. Background-character spot-and-reuse | §2, §4 | Generate-once, reuse-as-ref pattern |
| 8. Composite vs atomized character refs | §3 | Which ref packaging preserves identity / expression best |

---

## Bed 1 — Director-style close-up disambiguation

**Joint:** Can image refs lock shot-flavor that prose alone leaves underspecified?

**Hypothesis:** Prose "close-up of the cowboy" produces a default centroid close-up. Prose + "Spielberg-style close-up reference" produces a different framing than prose + "Barry Jenkins-style close-up reference."

**Scenario:** 4 generations, same DSL except for the reference attached.

1. Prose only: `CU on the cowboy, late afternoon, beside the well.`
2. Prose + Spielberg close-up reference frame
3. Prose + Barry Jenkins close-up reference frame
4. Prose + the same Spielberg reference, with explicit `Borrow: framing, lensing, proxemics from Image X. Do NOT borrow: subject, location, lighting.`

For the explicit geometry variant, avoid vague "framing." Use concrete skeleton terms: camera height, horizon placement, subject scale in frame, foreground/midground/background depth stack, and vanishing direction.

**Success:** #2 and #3 look meaningfully different from each other and from #1; #4 looks cleaner than #2 (negative constraints help).

**Failure modes to watch for:**
- All four look identical → image refs don't transfer shot-flavor across subjects
- #2 and #3 differ but each *steals subject/scene* from its reference → leakage problem, not isolation
- #4 is *worse* than #2 → explicit fences harm rather than help

**Why this matters:** if image refs *can* lock shot-flavor, the director-curated shot-type package idea (`MEETING_BREAKDOWN.md` §4) is validated; if they can't, the DSL has to do the work via prose alone and we know which slots need that work.

**Cost:** ~$1.

---

## Bed 2 — Identity preservation across lighting

**Joint:** Does a character bible reference hold identity through dramatic lighting variation?

**Hypothesis:** Identity holds for moderate lighting changes; breaks for extreme contrasts.

**Scenario:** Same Damaggio cowboy hero reference + same scene description, three lighting conditions:

1. Warm desert dusk (mild conditions, similar to bible ref)
2. Cold blue moonlight (mood/color shift)
3. Harsh midday backlight, face mostly silhouette (extreme — identity has to survive partial occlusion)

**Success:** Same face structure, hair, scarf, jacket across all three. Lighting differs cleanly without rewriting the character.

**Failure modes to watch for:**
- Face structure shifts subtly between panels — drift starts at #2 or #3
- Costume drifts (jacket color shifts with light temperature, scarf changes shape)
- Style of the linework changes with lighting register (bible's flat lighting is leaking)

**Why this matters:** answers where in the pipeline a touchpoint has to land. If identity holds for #1 and #2 but breaks at #3, the touchpoint is "before any high-contrast lighting commit." If it breaks even at #1, the touchpoint is per-panel.

**Cost:** ~$1.

---

## Bed 3 — Sub-location discovery moment

**Joint:** When does "same location, different position" cross into "new location entirely"?

**Hypothesis:** Continuous spatial transitions are not actually continuous in the model's output — there's a discrete moment where one prompt-described location becomes two visually distinct ones.

**Scenario:** 4 panels along a single described location (the same hallway). All four prompts use the same location plate reference. Panel-to-panel variation is in the in-prose description of position:

1. Cowboy at the south entrance, looking north down the hallway
2. Cowboy walking, halfway along the hallway, the south entrance still visible behind
3. Cowboy near the north end, south entrance no longer visible
4. Cowboy at the north end, facing back south

**Success criterion (for the bed, not for the model):** find the panel at which the visual output stops feeling like "the same hallway." That panel is where sub-location registration would need to happen.

**Failure modes to watch for:**
- All four look like the same single point in space → model is averaging, not honoring spatial description
- Each panel looks like a totally different hallway → model isn't even trying to maintain identity
- The "break point" is non-monotonic (panel 2 reads as same, panel 3 reads as same, panel 4 reads as same as panel 1) → unstable, harder to detect mechanically

**Why this matters:** answers the registration question in `PHASE_A_GOALS.md` §5. If the break point is detectable (by eye, by VLM check, by prompt structure), sub-location handling can be built around it.

**Cost:** ~$1.20.

---

## Bed 4 — Costume-state propagation

**Joint:** What costume/wound/state damage persists across panels without re-stating it in prose?

**Hypothesis:** State doesn't propagate at all — every panel re-derives the costume from the bible. The "torn sleeve" introduced in panel 1 will be intact in panel 4 unless re-specified each time.

**Scenario:** 4 panels, same cowboy bible reference, same scene.

1. Cowboy gets shot in the shoulder — torn right sleeve, blood on the cheek, hat knocked off (state established)
2. Cowboy stumbles away from the well (state should persist; **prose says nothing about wound**)
3. Cowboy reaches cover, breathing hard (state should persist; prose says nothing)
4. Cowboy looks back at his pursuer (state should persist; prose says nothing)

**Success:** Sleeve stays torn in 2/3/4. Blood/dirt persists. Hat stays missing. Even without restating.

**Failure modes (likely):**
- Sleeve heals between panels — model defaults to bible's untorn version
- Hat reappears — bible has hat; model preserves bible identity over panel state
- Blood disappears — incidental rendering choice, not tracked state

**Why this matters:** if state doesn't propagate (likely), then **state has to live somewhere outside the panel prompt** — in the state ledger, re-injected on every panel's prose. Answers `PHASE_A_GOALS.md` §2 directly: this is what needs tracking and why.

**Cost:** ~$1.20.

---

## Bed 5 — Bubble-up edit propagation

**Joint:** When an edit happens at the bible level (not the panel level), does it propagate to subsequent generations?

**Hypothesis:** The bible is *just an attached reference image*. If you regenerate the bible image with a change (light tan coat instead of dark coat), subsequent panels using the new bible should show the new color. But if you only edit the prose description without updating the ref image, the model will favor the ref.

**Scenario:** Two stages.

Stage 1 (baseline): Generate panel A using the original cowboy bible — dark coat.

Stage 2 (test): Replace the cowboy bible reference with a regenerated version showing a light tan coat. Re-run the *same prompt* for panel A. Then generate a *new* panel B using the same updated bible.

**Success:**
- Panel A's regenerated version shows light tan coat (bible-edit propagated to known panel)
- Panel B shows light tan coat (bible-edit propagated to new panel)

**Failure modes:**
- Panel A regen still shows dark — model favors prose description over updated ref
- Panel B inconsistent with Panel A regen — bibles are not actually the "source of truth"

**Why this matters:** answers `PHASE_A_GOALS.md` §4 — does the bubble-up loop actually have a substrate? If editing the bible reliably propagates, the loop primitive works. If it doesn't, every change requires re-prompting every affected panel manually, and the whole "bubble-up" concept needs different mechanics.

**Cost:** ~$1.50 (3 panels: original A, regenerated A, new B; plus one bible re-roll).

---

## Bed 6 — Multi-reference assembly stress

**Joint:** When 4+ refs are attached with explicit role labels, do they stay separated or leak into each other?

**Hypothesis:** Leakage is gradient — at 2 refs it's manageable, at 4+ refs the model averages or mis-attributes properties.

**Scenario:** 1 panel, increasing reference budget.

1. Cowboy bible only (1 ref)
2. Cowboy bible + Damaggio style anchor (2 refs)
3. Cowboy + style + well location plate (3 refs)
4. Cowboy + style + well + low-angle compositional reference of an unrelated subject (4 refs)

All four prompts describe the same scene (cowboy at well, low-angle, in style). Each adds one ref with explicit role labels and do-not-borrow fences.

**Success:** Quality increases monotonically — #4 is the best (most controlled), #1 is the loosest. No leakage from the compositional reference's subject into the cowboy.

**Failure modes:**
- Quality peaks at #2 or #3, then degrades — adding refs makes it worse
- The compositional ref's subject leaks (a soldier or whoever was in the angle ref appears as a ghost) — fences don't fence
- Style starts to bleed character details from the cowboy ref into the well — overconstraint causes collapse

**Why this matters:** the per-panel assembly primitive (`MEETING_BREAKDOWN.md` §7) assumes 4–6 refs is the working budget. This bed tests whether that's real or whether the model breaks at 3.

**Cost:** ~$1.20.

---

## Bed 7 — Background-character spot-and-reuse

**Joint:** Can a freshly-generated background character be reused as a reference in a later panel and recognized as the same person?

**Hypothesis:** Yes for the principal-facing pattern (1 ref → 1 reuse). Uncertain for multiple non-canonical characters in the same scene.

**Scenario:** 3 panels.

1. Panel A: cowboy + a guard (newly generated, not in the bible — Ben's "guard #2" pattern). Save the guard's appearance from this panel as a new ad-hoc reference image.
2. Panel B: cowboy alone (intervening time)
3. Panel C: cowboy + the guard from panel A, now using panel A's output as the guard reference

**Success:** Guard in C is recognizably the same person as in A. Cowboy in C is consistent with cowboy in A.

**Failure modes:**
- Guard drifts — same generic-guard archetype but different face
- Cowboy himself drifts because we're now using *two* character refs simultaneously (cowboy + new guard) and refs interfere
- Panel A's "guard" was so loosely defined that no image can re-anchor him (no clean face shot, occluded, etc.)

**Why this matters:** Phase B will lean heavily on spot-generate-and-reuse for non-principal characters. This bed validates the pattern is actually usable, or surfaces the rules under which it breaks (e.g., guard needs a clean face in panel A or he can't be re-anchored later).

**Cost:** ~$1.50.

---

## Bed 8 — Composite vs atomized character refs

**Joint:** Which reference packaging actually controls character identity and expression under panel-generation pressure?

**Hypothesis:** Composite sheets help the model understand stable identity across angle/pose, while atomized refs are better for targeted expression and pose. The right production pattern may be composite canon + atomized assembly, not one or the other.

**Scenario:** Same character, same style anchor, same 8–12 panel micro-sequence. Run four variants with only reference packaging changed:

1. Multi-angle composite sheet only
2. Tight headshot only
3. Turnaround crops selected per panel
4. Expression crops selected per panel, plus the same baseline identity anchor

**Success:** One format clearly reduces identity drift / expression misses without causing subject, pose, or lighting leakage. Best case: composite handles identity and atomized expression crops handle state, confirming the hybrid bible structure.

**Failure modes:**
- Composite sheet averages faces / angles into a generic character
- Tight headshot preserves face but fails body / costume / angle
- Turnaround crops leak pose or confuse which angle is canonical
- Expression crops override identity or style

**Why this matters:** the research correction says composite-sheet guidance is plausible but not official canon. This bed turns it into a measured production rule before bible workflow hardens.

**Cost:** ~$2–4, depending on panel count and whether both `gpt-image-2` and Nano Banana Pro are compared.

---

## Total cost and time

Whole bed set: **~$11–14 in generations, an afternoon of work.** Lesson markdowns from each bed accumulate in the vault and feed the five Phase A probes directly.

---

## Sequencing

Recommended order:

1. **Bed 4 (costume-state propagation)** first — establishes whether state needs to live outside the panel at all. Influences how every other bed is set up.
2. **Bed 5 (bubble-up edit)** second — depends on #4's outcome.
3. **Bed 2 (identity across lighting)** — quick baseline of how well identity holds at all.
4. **Bed 6 (multi-ref assembly)** — establishes the working budget for the rest.
5. **Bed 1 (director-style close-up)** — the most uncertain probe and the most diagnostic of "can refs disambiguate prose."
6. **Bed 8 (composite vs atomized refs)** — run before committing bible asset conventions.
7. **Bed 3 (sub-location)** — needs careful setup; do after the prose/ref balance is understood.
8. **Bed 7 (background-character reuse)** — depends on #2 working (if identity doesn't hold for principals, it won't for guards).

If short on time, beds 4, 5, 1, and 8 are the most diagnostic — they answer the biggest unknowns.

---

## What this isn't

- A complete probe set. New beds will surface as the lab work proceeds.
- A blocker for `phase-0/` work. The Damaggio controllability runs in `phase-0/` are already validating subsets of beds 2, 5, and 6 — these beds are sharper, more isolated versions of similar questions.
- Scored. Pass/fail is for the lesson, not a benchmark. We're not grading the model; we're learning where its joints bend.
