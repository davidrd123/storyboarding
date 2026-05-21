---
title: Phase 0 — Grammar Validation Prompt Log
purpose: Pre-logged grammar-validation tests, one entry per cell. Fire in order; resume by finding entries with blank `Sent:`.
---

# Phase 0 — Grammar Validation Prompt Log

Pre-logged per Patrick's discipline: every entry is committed to this file with `Sent:` blank before any job fires. A fresh agent picks up by finding the first blank `Sent:` row.

Append, don't overwrite. Successful phrases get hoisted into the Successful Phrases section at the bottom.

---

## Approved Keyframes

| Test | Final state | Output path |
|---|---|---|
| T01 | accepted — style-only grammar keeper | `outputs/2026-05-19/gemini-3-pro-image-preview/01_p0-t01-style-only-borrow_d92fbeeb/p0-t01-style-only-borrow_01.png` |
| T02 | accepted — cowboy identity proof | `outputs/2026-05-19/gemini-3-pro-image-preview/01_p0-t02-cowboy-identity-newscene_a0d5780b/p0-t02-cowboy-identity-newscene_01.png` |
| T03 | iterate — useful diagnostic failure on suppressed emotion | `outputs/2026-05-19/gemini-3-pro-image-preview/01_p0-t03-state-block-cold-rage_1c790ce4/p0-t03-state-block-cold-rage_01.png` |
| T04 | accepted — prose-only new location proof | `outputs/2026-05-19/gemini-3-pro-image-preview/01_p0-t04-prose-only-newlocation_675954da/p0-t04-prose-only-newlocation_01.png` |
| T05 | accepted — location-plate continuity proof, mirrored composition caveat | `outputs/2026-05-19/gemini-3-pro-image-preview/01_p0-t05-location-plate-continuity_50f826f7/p0-t05-location-plate-continuity_01.png` |
| T06 | accepted only as a visual result — attribution inconclusive | `outputs/2026-05-19/gemini-3-pro-image-preview/01_p0-t06-compositional-skeleton-transfer_66c61ef2/p0-t06-compositional-skeleton-transfer_01.png` |

---

## Identity Anchors

| Anchor | File | Use |
|---|---|---|
| Style — establishing | `refs/style/damaggio_01_establishing.jpg` | Wide-frame style ref, also holds well/ruins geography |
| Style — action | `refs/style/damaggio_02_action.jpg` | High-action style ref |
| Style — MSrev cowboy | `refs/style/damaggio_03_msrev_cowboy.jpg` | MS reverse style ref, doubles as cowboy face anchor |
| Style — MSrev officer | `refs/style/damaggio_04_msrev_officer.jpg` | MS reverse style ref, doubles as officer face anchor |
| Cowboy identity | `refs/characters/cowboy_hero_ref.jpg` | Face/hat/scarf/build lock |
| Officer identity | `refs/characters/officer_hero_ref.jpg` | Face/uniform lock |
| Location — well/ruins | `refs/locations/well_ruins_plate.jpg` | Same-place continuity ref |

---

## Locked Style Anchor (text block — reused across tests)

```
STYLE: European bande dessinée ink wash. Duotone palette — warm
       cream paper + sepia/olive ink. Loose confident linework,
       cross-hatch for shadow and material texture, atmospheric
       falloff in the distance. No vibrant color, no rendered
       polish, no photographic detail.
```

Use this verbatim in every test's `STYLE` block. If a test deviates from this, the deviation is the experiment — log why.

---

## T01 — Style-only borrow, new scene

**Date:** 2026-05-19
**Mode:** genesis
**Model:** gemini-3-pro-image-preview
**Test question:** Does "borrow style, do NOT borrow subject/composition" hold when the source ref has strong characters and geography?

**References:**
- Image 1: `refs/style/damaggio_01_establishing.jpg` (style only)

**Prompt:**
```
Image 1 is a style reference.
Borrow from Image 1: ink wash treatment, duotone sepia/olive palette,
  linework quality, cross-hatch shadow language, paper texture.
Do NOT borrow from Image 1: subject, composition, location, props,
  characters, or any specific scene element.

Generate a new scene: a steam locomotive at a small mountain station,
seen from the platform. Late afternoon, long shadows across the platform.
A railway worker walks toward the camera with a lantern. No specific
period or country signaling required.

16:9 aspect ratio.
```

**System prompt:** (locked style anchor text block above, used as system instruction)

**Sent:** 2026-05-19 14:16
**Output:** `outputs/2026-05-19/gemini-3-pro-image-preview/01_p0-t01-style-only-borrow_d92fbeeb/p0-t01-style-only-borrow_01.png`
**Result notes:** Steam locomotive at mountain station with water tower; railway worker walking toward camera with lantern. Late afternoon shadows. **No subject leakage from Image 1** — none of the source's cowboy/officer/camel/well/ruins appear. Sepia/olive duotone present, cross-hatch shadow language present, ink wash present. Linework slightly tighter/more illustrative than Damaggio's loose confidence, but in-category. The do-not-borrow grammar held.

**Calibrated score (gemini-3.5-flash, 0–100):**
| PF | PrF | SL | SH | SS | CBF | Decision |
|---|---|---|---|---|---|---|
| 78 | N/A | 77 | 76 | 76 | 79 | accept |

Judge notes (verbatim from Flash):
- PF: locomotive, station platform, worker with lantern, late afternoon — all rendered as instructed.
- SL: duotone sepia/olive palette, ink wash texture, cross-hatch shading "perfectly mirror" the reference aesthetic.
- SH: foreground worker / midground locomotive / background mountains — strong depth stack.
- CBF: "model successfully isolated the artistic style of the reference while completely avoiding any subject or compositional leakage."

**Next iteration:** None. Grammar validated. Carry the same do-not-borrow phrasing into T02 with character identity added.
**Successful phrases:** `"Borrow from Image 1: ink wash treatment, duotone sepia/olive palette, linework quality, cross-hatch shadow language, paper texture. Do NOT borrow from Image 1: subject, composition, location, props, characters, or any specific scene element."` — clean lock, no leakage.

---

## T02 — Style + cowboy identity (new scene)

**Date:** 2026-05-19
**Mode:** genesis
**Model:** gemini-3-pro-image-preview
**Test question:** Does an explicit character identity ref hold face/costume across a new scene the source images don't depict?

**References:**
- Image 1: `refs/characters/cowboy_hero_ref.jpg` (character identity)
- Image 2: `refs/style/damaggio_02_action.jpg` (style only — chosen because it has a different composition than the character ref)

**Prompt:**
```
Image 1 is the cowboy character reference.
Image 2 is a style reference.

Preserve from Image 1: face structure, beard pattern, hat shape, scarf,
  jacket, build, weathered look.
Borrow from Image 2: ink wash treatment, duotone palette, linework
  quality, cross-hatch shadow language.
Do NOT borrow from Image 2: subject, composition, scene elements.

Generate: MCU of the cowboy from Image 1 standing at the edge of a
mesa overlook, late afternoon. He is alone, looking out across the
valley. Wind in the scarf. Three-quarter front angle. He fills the
right two thirds of frame.

16:9 aspect ratio.
```

**Sent:** 2026-05-19 14:22
**Output:** `outputs/2026-05-19/gemini-3-pro-image-preview/01_p0-t02-cowboy-identity-newscene_a0d5780b/p0-t02-cowboy-identity-newscene_01.png`
**Result notes:** MCU of cowboy at mesa edge, three-quarter front, scarf catching wind, valley/mesas behind. Identity locked — recognizably the same person from Shot_Reverse_01.

**Calibrated score (gemini-3.5-flash):**
| PF | PrF | SL | SH | SS | CBF | Decision |
|---|---|---|---|---|---|---|
| 81 | 80 | 82 | 80 | 80 | 81 | accept |

Judge quote (the key one): *"The character's facial structure, stubble, hat shape, and scarf style closely match the reference from Image 1. The identity remains recognizable without feeling like a different actor."* — this is **exactly** the failure mode from the original chat (prose-only generated a new actor). The identity ref fixed it.

**Next iteration:** None. **First proof point that the bible-driven workflow holds identity.**
**Successful phrases:** `"Preserve from Image 1: face structure, beard pattern, hat shape, scarf, jacket, build, weathered look."` — concrete feature list locks identity cleanly.

---

## T03 — Style + identity + STATE block (emotional specificity)

**Date:** 2026-05-19
**Mode:** genesis
**Model:** gemini-3-pro-image-preview
**Test question:** Does the prose STATE block (per the DSL skeleton) render emotionally specific results when paired with an identity ref?

**References:**
- Image 1: `refs/characters/cowboy_hero_ref.jpg` (character identity)
- Image 2: `refs/style/damaggio_03_msrev_cowboy.jpg` (style + tonal reference for stillness)

**Prompt:**
```
Image 1 is the cowboy character reference.
Image 2 is a style and tonal reference.

Preserve from Image 1: face, beard, hat, scarf, jacket, build.
Borrow from Image 2: ink wash, palette, linework, atmosphere of held stillness.
Do NOT borrow from Image 2: subject placement, composition, location.

SHOT: MCU, low angle, slight push-in.
STATE: Cold rage held in. Jaw set, eyes hard and unmoving, locked
       on something off-frame right. No movement. Dust on his cheek.
       Hat shadowing the upper half of his face. Hand near holster
       grip but not on it. Scarf loosened. Whole body wound tight
       but still.
ACTION: Holds his ground, watching.
SETTING: Beside a brick well in desert ruins, late afternoon, long shadows.
MOOD: Tense, anticipatory. Warm directional light from frame left, deep
      shadow on his off side. Dust haze.
COMPOSITION: Cowboy frame right, eyeline pulls composition to empty
             left third. Negative space signals what he's watching.

16:9 aspect ratio.
```

**Sent:** 2026-05-19 14:23
**Output:** `outputs/2026-05-19/gemini-3-pro-image-preview/01_p0-t03-state-block-cold-rage_1c790ce4/p0-t03-state-block-cold-rage_01.png`
**Result notes:** MCU low-angle on cowboy beside brick well, dust haze, jaw set, hand near holster. Identity strong, style strong, composition strong. **But the expression rendered as overt snarl with bared teeth instead of suppressed cold rage.** The brief predicted this exact failure mode — prose cannot reliably distinguish "cold rage held in" from generic anger; the model defaults to the more legible expression.

**Calibrated score (gemini-3.5-flash):**
| PF | PrF | SL | SH | SS | CBF | Decision |
|---|---|---|---|---|---|---|
| 74 | 82 | 85 | 80 | 75 | 68 | **iterate** |

Judge quote (the diagnostic one): *"The image fails the specific success criteria for expression, rendering overt anger with bared teeth instead of suppressed cold rage."*

**Next iteration:** This is the load-bearing case for the expression sheet. Two paths:
1. Sharper anti-overt language in prose ("lips closed, no teeth showing, flat affect, no movement in the face") — cheap to try.
2. The real fix: an expression sheet entry `cowboy_expr_cold-rage.png` passed as a third reference, role-labeled as the emotional state lock.

T03 outcome **validates that the expression sheet is the highest-leverage asset in the bible** — exactly as the brief predicted. Defer the iteration; the discovery is the value.

**Successful phrases:** Style and identity language held perfectly under emotional-state stress. The failure is isolated to the expression prose itself.

---

## T04 — Style + identity + new location (prose-only)

**Date:** 2026-05-19
**Mode:** genesis
**Model:** gemini-3-pro-image-preview
**Test question:** How much of "the same character in a new described location" the model gets right without a location plate. Maps the prose-only ceiling for setting.

**References:**
- Image 1: `refs/characters/cowboy_hero_ref.jpg`
- Image 2: `refs/style/damaggio_01_establishing.jpg` (style only)

**Prompt:**
```
Image 1 is the cowboy character reference.
Image 2 is a style reference.

Preserve from Image 1: face, beard, hat, scarf, jacket, build.
Borrow from Image 2: ink wash, palette, linework, atmospheric haze.
Do NOT borrow from Image 2: any subject, composition, or scene elements.

SHOT: MS, eye level.
SUBJECT: Cowboy from Image 1.
STATE: Tired, alert. Reins held loose in one hand.
ACTION: Riding a horse at a walk down a dry riverbed between
        tall sandstone walls.
SETTING: Narrow slot canyon, late morning. Cool shadow on canyon
         walls, hot light hitting the top edge.
MOOD: Quiet, watchful. The canyon presses in.
COMPOSITION: Cowboy and horse centered in lower third, canyon walls
             frame him on both sides.

16:9 aspect ratio.
```

**Sent:** 2026-05-19 14:24
**Output:** `outputs/2026-05-19/gemini-3-pro-image-preview/01_p0-t04-prose-only-newlocation_675954da/p0-t04-prose-only-newlocation_01.png`
**Result notes:** MS of cowboy on horseback walking through a slot canyon between sandstone walls; cool shadow on walls, hot light on the top edge. Prose-only landed a recognizable slot-canyon environment cleanly. Identity locked. Style perfect.

**Calibrated score (gemini-3.5-flash):**
| PF | PrF | SL | SH | SS | CBF | Decision |
|---|---|---|---|---|---|---|
| 80 | 81 | 82 | 80 | 80 | 81 | accept |

Judge quote: *"The model successfully generates a recognizable slot-canyon environment from prose alone while maintaining style and character consistency."*

**Next iteration:** None. **Confirms that distinct location *categories* don't need plates — prose carries them.** Plates are needed for *same-location continuity*, not for "go to a new kind of place." Brief implication: world bible only needs plates for locations that recur, not for every setting.

**Successful phrases:** Geographic detail (`"narrow slot canyon… tall sandstone walls… cool shadow on canyon walls, hot light hitting the top edge"`) gave the model enough to land the right place from prose alone.

---

## T05 — Style + identity + location plate (same-place continuity)

**Date:** 2026-05-19
**Mode:** genesis
**Model:** gemini-3-pro-image-preview
**Test question:** Does an explicit location plate hold same-place continuity from a *different camera angle* on the same geography?

**References:**
- Image 1: `refs/characters/cowboy_hero_ref.jpg` (character identity)
- Image 2: `refs/locations/well_ruins_plate.jpg` (location continuity)
- Image 3: `refs/style/damaggio_02_action.jpg` (style only)

**Prompt:**
```
Image 1 is the cowboy character reference.
Image 2 is the location reference — the same brick well, ruins,
  and surrounding geography.
Image 3 is a style reference.

Preserve from Image 1: face, beard, hat, scarf, jacket, build.
Preserve from Image 2: well geometry, ruins position, dust haze, palette
  of the location, time-of-day quality of light.
Borrow from Image 3: ink wash, linework, shadow language.
Do NOT borrow from Image 3: subject, composition, props, scene elements.

SHOT: CU, low angle on the cowboy. The brick well is visible
      behind him at the edge of frame.
STATE: Jaw set, looking down and slightly to the right at something
       just off the well's rim.
ACTION: Crouching at the well's edge, peering down into it.
SETTING: Same location as Image 2. Same time of day. Same dust haze.
MOOD: Tense, focused.
COMPOSITION: Cowboy upper-right, well rim cutting across lower-left
             third, ruins implied behind in soft falloff.

16:9 aspect ratio.
```

**Sent:** 2026-05-19 14:25
**Output:** `outputs/2026-05-19/gemini-3-pro-image-preview/01_p0-t05-location-plate-continuity_50f826f7/p0-t05-location-plate-continuity_01.png`
**Result notes:** CU low-angle on cowboy crouching at brick well, ruins behind in soft falloff. The brick well in the output reads as the **same well from the location plate** — same brick pattern, same scale, same ruins context. Composition mirrored (cowboy upper-left instead of upper-right) but the location continuity held.

**Calibrated score (gemini-3.5-flash):**
| PF | PrF | SL | SH | SS | CBF | Decision |
|---|---|---|---|---|---|---|
| 76 | 84 | 85 | 83 | 84 | 86 | accept |

Judge quote (the headline): *"Successfully proves that location continuity can be maintained across different camera angles using the provided plates."*

**Next iteration:** None. **World bible workflow validated.** The location plate + role label held the same geography from a completely new camera angle.

**Successful phrases:** `"Preserve from Image 2: well geometry, ruins position, dust haze, palette of the location, time-of-day quality of light."` — concrete geographic feature list works the same way concrete identity features work.

**Minor note:** PF dropped to 76 because composition mirrored. Possibly tolerable for storyboards (the beat reads the same), but flag for fix if direction-of-action matters (left/right screen direction is a continuity grammar). Easy mitigation: explicit "cowboy on the right side of frame, well on the left" prose plus "do not mirror" if needed.

---

## T06 — Compositional skeleton transfer (THE wildcard)

**Date:** 2026-05-19
**Mode:** genesis
**Model:** gemini-3-pro-image-preview
**Test question:** Can a reference image lock *camera framing only* (low angle, specific composition) on a completely different subject? **This is the brief's biggest open question.**

**References:**
- Image 1: `refs/characters/cowboy_hero_ref.jpg` (character identity — different subject from Image 2)
- Image 2: `refs/style/damaggio_02_action.jpg` (compositional skeleton — *not* a typical style use; we're using its low-angle aggressive framing)
- Image 3: `refs/style/damaggio_01_establishing.jpg` (style only, deliberately different from Image 2)

**Prompt:**
```
Image 1 is the cowboy character reference.
Image 2 is a COMPOSITIONAL reference. We want only its camera position
  relative to subject, its horizon height, its vertical proportions,
  and its framing geometry.
Image 3 is a STYLE reference.

Preserve from Image 1: face, beard, hat, scarf, jacket, build.

From Image 2 BORROW ONLY: camera position relative to subject (low
  angle looking up at the figure), horizon height in frame, vertical
  proportions of figure-to-sky, framing geometry. Do NOT borrow:
  subject, costume, location, props, palette, lighting, style, or
  any other visual element.

Borrow from Image 3: ink wash, palette, linework, atmospheric haze.
Do NOT borrow from Image 3: subject, composition, location.

Generate: the cowboy from Image 1 standing alone at the top of a dune,
looking down toward the camera. Late afternoon backlight. Single figure
in frame. Sky fills upper two thirds.

16:9 aspect ratio.
```

**Sent:** 2026-05-19 14:26
**Output:** `outputs/2026-05-19/gemini-3-pro-image-preview/01_p0-t06-compositional-skeleton-transfer_66c61ef2/p0-t06-compositional-skeleton-transfer_01.png`
**Result notes:** Low-angle shot of the cowboy on a dune crest, looking down at camera, sky fills the upper portion. The framing geometry IS low-angle as instructed. Identity preserved. Style perfect. **But — there's a confound.** The prose itself says "looking down toward the camera," which prose-only would already imply low angle. We cannot tell from this single test whether Image 2's framing reference contributed to the result or whether prose carried it alone.

**Calibrated score (gemini-3.5-flash):**
| PF | PrF | SL | SH | SS | CBF | Decision |
|---|---|---|---|---|---|---|
| 80 | 78 | 81 | 79 | 80 | 82 | accept |

Judge quote: *"Successfully demonstrates that camera framing and low-angle geometry can be locked onto a new subject."* — generous interpretation; the test design didn't isolate the variable.

**Next iteration / isolation test:** Re-fire the same prompt **without Image 2** (only identity + style refs) to see if prose alone produces an equivalent low-angle composition. If yes → role-labeled framing reference is not doing measurable work and Patrick's clean-plate → token-deconstruct path is the better strategy. If no → the framing ref is load-bearing and we have a real new technique. **This is the question worth answering before Tuesday.**

**Tentative verdict:** the brief was right to be skeptical that abstract relational properties like "camera angle" cleanly extract from a reference. The output is good but ambiguous attribution. **Patrick's compositional-skeleton-transfer-as-token-deconstruct** (`patterns/image-generation-control-lessons.md` §14) remains the better-documented path; this experiment is inconclusive.

**Fallback if T06 fails:** apply Patrick's camera-change protocol — token-deconstruct the low-angle reference into explicit spatial prose ("camera height below subject's belt line, looking up; horizon at lower fifth of frame; subject scale fills central vertical column; foreground/midground/background depth stack compressed toward the dune crest; vanishing direction pulls upward into sky") and re-fire as pure prose without Image 2. Log whether the prose-only spatial description outperforms the role-labeled framing reference. See `patterns/image-generation-control-lessons.md` §14.

---

## T06a-iso — Isolation: T06 prompt minus Image 2

**Date:** 2026-05-19
**Mode:** genesis
**Model:** gemini-3-pro-image-preview
**Test question:** Was Image 2 (the compositional skeleton reference) doing measurable work in T06, or did the prose ("looking down toward the camera," "sky fills upper two thirds") carry the low-angle framing alone?

**References:**
- Image 1: `refs/characters/cowboy_hero_ref.jpg` (character identity)
- Image 2: `refs/style/damaggio_01_establishing.jpg` (style only)

Same prose as T06. Only difference: the compositional skeleton ref (formerly T06's Image 2) is removed.

**Prompt:**
```
Image 1 is the cowboy character reference.
Image 2 is a STYLE reference.

Preserve from Image 1: face, beard, hat, scarf, jacket, build.

Borrow from Image 2: ink wash, palette, linework, atmospheric haze.
Do NOT borrow from Image 2: subject, composition, location, props.

Generate: the cowboy from Image 1 standing alone at the top of a dune,
looking down toward the camera. Late afternoon backlight. Single figure
in frame. Sky fills upper two thirds.

16:9 aspect ratio.
```

**Sent:** 2026-05-19 18:38
**Output:** `outputs/2026-05-19/gemini-3-pro-image-preview/01_p0-t06a-iso-no-compositional-ref_84d695b3/p0-t06a-iso-no-compositional-ref_01.png`
**Result notes:** Low-angle shot of the cowboy on a dune crest, looking down at camera, sky fills upper portion. **Composition is essentially identical to original T06.** Prose alone carried the low-angle framing.

**Calibrated score (gemini-3.5-flash):**
| PF | PrF | SL | SH | SS | CBF | Decision |
|---|---|---|---|---|---|---|
| 83 | 81 | 84 | 82 | 80 | 85 | accept |

Judge quote (the decisive one): *"The image successfully achieves the low-angle framing and character preservation using only prose and style/identity references, indicating the compositional reference was not required."*

**Comparison vs T06:**
| Variant | PF | PrF | SL | SH | SS | CBF |
|---|---|---|---|---|---|---|
| T06 with Image 2 | 80 | 78 | 81 | 79 | 80 | 82 |
| T06a-iso no Image 2 | **83** | **81** | **84** | **82** | 80 | **85** |

T06a-iso scored **equal or better on every dimension**. The role-labeled compositional reference didn't just fail to add value — it likely introduced competing visual signal that nudged scores down.

**Verdict:** **Compositional skeleton transfer via role-labeled reference does NOT work as advertised in Nano Banana Pro.** The brief's biggest open question (`STORYBOARD_SYSTEM_BRIEF.md` §4, deep-research #6) has a clean negative answer for this technique.

**What this confirms:** Patrick's clean-plate → token-deconstruct → genesis path (`patterns/image-generation-control-lessons.md` §14) is the correct strategy. Prose alone, with sharp framing language ("looking down toward the camera, sky fills upper two thirds, low angle, single figure"), is sufficient and cleaner.

**Successful phrases:** `"looking down toward the camera... sky fills upper two thirds"` — prose-only framing language carries low-angle reliably. No compositional ref needed.

**Open follow-up:** T06b would push further — does the sharpened geometric vocabulary from the deep-research memo and Patrick's protocol ("camera height below subject's belt line, horizon at lower fifth of frame, foreground/midground/background depth stack, vanishing direction pulls upward") outperform the simpler prose we just used? Cheap to test; would confirm or refine the prose-only baseline.

---

## Round 2 — iterations (2026-05-21)

### T03b — Cold rage with anti-overt fencing (iteration on T03)

**Mode:** genesis · **Model:** gemini-3-pro-image-preview
**Test question:** T03's "cold rage held in" rendered as overt snarl (CBF 68). Can sharpened negative prose ("lips closed, no teeth, NO snarl, flat affect, micro-tension at jaw") land suppressed cold rage, or is an expression-sheet reference the only path?

**References:** Image 1 `cowboy_hero_ref.jpg` (identity) · Image 2 `damaggio_03_msrev_cowboy.jpg` (style)
**Output:** `outputs/2026-05-21/gemini-3-pro-image-preview/01_p0-t03b-cold-rage-antiovert_61fbeef9/p0-t03b-cold-rage-antiovert_01.png`
**Result notes:** Snarl gone — mouth closed, flat affect. Shot widened from MCU toward a fuller MS, well + ruins behind. **Eyeball caveat:** reads to me as closer to neutral/calm than actively "wound tight"; the suppressed/neutral boundary is genuinely fuzzy. Flash read it as contained cold rage.

**Calibrated score (gemini-3.5-flash):**
| PF | PrF | SL | SH | SS | CBF | Decision |
|---|---|---|---|---|---|---|
| 84 | 83 | 85 | 82 | 84 | 85 | accept |

Judge quote: *"successfully meets the core test of depicting suppressed cold rage with a closed mouth and no teeth. This confirms that precise negative prompting can achieve the desired expression without an expression sheet."*

**Verdict (refined from T03):** Prose with explicit negative fencing CAN hit contained emotion on a single panel — CBF rose 68 → 85. This narrows the expression-sheet's role: it's not required to land the emotion *once*, it's required to land it *consistently across many panels*. Single-panel emotional specificity is a prose-solvable problem; cross-panel emotional consistency is the bible's job.

**Successful phrase:** `"lips closed, no teeth showing, mouth a flat hard line; flat affect; NO snarl, NO bared teeth, NO open mouth"` — explicit negative fencing suppresses the model's default toward legible/overt emotion.

**Open nuance:** the eyeball-vs-Flash divergence on neutral-vs-suppressed is worth a human gut-check before treating this as fully solved. The model avoided the snarl; whether it landed *cold rage* specifically vs. *generic stoicism* is a judgment call.

### T06b — Geometric token-deconstruct prose (refinement on T06a)

**Mode:** genesis · **Model:** gemini-3-pro-image-preview
**Test question:** T06a proved simple prose carries low-angle framing (CBF 85). Does the *sharpened* geometric vocabulary (camera below belt line, horizon at lower fifth, central vertical column, depth stack, sweeping foreground) outperform or match it?

**References:** Image 1 `cowboy_hero_ref.jpg` (identity) · Image 2 `damaggio_01_establishing.jpg` (style). No compositional ref.
**Output:** `outputs/2026-05-21/gemini-3-pro-image-preview/01_p0-t06b-geometric-prose_1df7ea88/p0-t06b-geometric-prose_01.png`
**Result notes:** Low-angle dune-crest shot, figure central, horizon low, sweeping foreground. Slightly flatter than T06a's dramatic upward angle by eye, but structurally on-spec. (One transient 502 from Google on first fire; succeeded on retry.)

**Calibrated score (gemini-3.5-flash):**
| PF | PrF | SL | SH | SS | CBF | Decision |
|---|---|---|---|---|---|---|
| 82 | 84 | 85 | 83 | 81 | 85 | accept |

Judge quote: *"The geometric prose successfully guided the layout, producing a precise low-angle composition... This validates the token-deconstruct strategy."*

**Verdict:** Geometric token-deconstruct prose matches simple prose (both CBF 85). Camera framing is firmly a **prose slot**, and Patrick's clean-plate → token-deconstruct path (`patterns/image-generation-control-lessons.md` §14) is the validated camera-control strategy. No compositional reference pack needed. Combined with T06a, the compositional-skeleton-transfer question is fully closed.

**Successful phrase:** `"Camera positioned low, below the subject's belt line, looking up at him. Horizon sits at the lower fifth of the frame. The figure fills the central vertical column."` — explicit geometric vocabulary lands camera framing without a reference.

---

## Successful Phrases

| Phrase | Unlocked | First seen in |
|---|---|---|
| `"Borrow from Image 1: ink wash treatment, duotone sepia/olive palette, linework quality, cross-hatch shadow language, paper texture. Do NOT borrow from Image 1: subject, composition, location, props, characters, or any specific scene element."` | Style-only transfer without subject leakage | T01 |
| `"Preserve from Image 1: face structure, beard pattern, hat shape, scarf, jacket, build, weathered look."` | Cowboy identity held across a new scene | T02 |
| `"narrow slot canyon... tall sandstone walls... cool shadow on canyon walls, hot light hitting the top edge"` | Distinct new location category from prose alone | T04 |
| `"Preserve from Image 2: well geometry, ruins position, dust haze, palette of the location, time-of-day quality of light."` | Same-place continuity from a location plate | T05 |

---

## Failure Modes Observed

| Mode | Description | Seen in | Mitigation tried |
|---|---|---|---|
| Overt-expression default | Prose "cold rage held in" rendered as bared-teeth anger; model picked legibility over suppression | T03 | Next: closed-mouth / no-teeth prose; real fix is expression ref |
| Composition mirror | Requested cowboy upper-right / well lower-left; output mirrored the composition | T05 | Next: explicit "cowboy on right side of frame, well on left; do not mirror" |
| Camera attribution confound | Low-angle result could have come from prose alone because prompt said "looking down toward the camera" | T06 | Next: T06-iso without Image 2; then geometric token-deconstruct prompt |
| Linework tightness | Output trends slightly more polished / illustrated than Damaggio's loose confidence | T01-T06 | Next: test "loose sketch quality, broken contour, scratch lines" |
