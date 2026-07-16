# Opening tests — register probes (for codex → GPT Image 2)

**Goal of this first batch:** not the finished book — a *proof of the conceit.* Test whether the
model can render the two opposed registers and, hardest, the **form-as-content** trick (gold
rigid grid = control; white flooding the gutters = dissolution). Do not run from the riff-mcp
side; codex gens. These are full comic **pages** → expect lettering-density + character-
consistency risk; verify on review, gen in halves and composite if a page garbles.

**Aspect:** comic pages → **2:3 portrait**, high resolution. **Vane's face must stay the same
man across panels** — that consistency IS the "self-image" idea, so it's load-bearing, not
cosmetic.

---

## TEST 1 — PAGE 1: the CLARION register (control / gold monument)

*Establishes the protagonist, the voice, and the "total control of the page" look. If this
doesn't read as rigid, gilded, airless control, the contrast later won't land.*

```
A graphic-novel PAGE, vertical 2:3 portrait. STYLE: cold maximalist control — a rigid, ruler-
straight grid of equal panels with gleaming GOLD borders and gutters, flat planar color and
clinical symmetry (Chris Ware precision) crossed with illuminated-manuscript gold leaf (J.H.
Williams III), obsessive uniform thin ink line, hyperdetailed, almost no negative space. Opulent,
airless, monumental.

Subject: PRESIDENT AUGUST VANE — a powerful, imperious mogul-president in his late 60s, silver-
gold hair, heavy expensive suit, a face built for monuments (archetype, not a real person). He
sits enthroned at the center of a vast throne-room-office whose every wall is covered in screens,
and his own face repeats on every screen — the same face, dozens of times, all composed and
identical.

Panels (rigid grid, his face recurring identically):
- Wide establishing panel: the throne room, faces on every surface, Vane centered and total.
- Three tight identical-format panels: his composed face, a gilded hand, the room reflected in
  his eye.
- Final panel, lower right: a single gold lozenge (a pill) held between two fingers, glinting —
  the ritual dose. The linework in this last panel is the sharpest and most precise on the page.

Caption boxes in a cold, over-articulate first-person voice, gold-bordered: "THERE IS A VERSION
OF ME ON EVERY SURFACE IN THIS ROOM." / "I HAD IT BUILT THAT WAY." / "REDUNDANCY IS THE ONLY
HONEST FORM OF LOVE."

High resolution; every border ruler-straight and gold; all lettering legible and correctly
spelled.
```

**Watch:** is it *airless* enough? The failure mode is "nice gold comic" instead of "a man who
has imprisoned the whole page inside himself." More repetition of the identical face = better.

---

## TEST 2 — the solvent register (dissolution / white eating inward)

*Distilled from PAGE 5 — the first real appearance of the form-as-content war. Tests whether the
model can render a* breaking *grid: gold borders failing, white gutter widening and leaking, a
plain figure occupying the white. This is the make-or-break visual of the entire book.*

```
A graphic-novel PAGE, vertical 2:3 portrait. STYLE: the same cold gold-grid control as before —
BUT it is coming apart. Most panels still hold: rigid gold borders, AUGUST VANE's hyperdetailed
composed face, opulent and precise. The horror is structural: one GUTTER between panels has
widened far too much into a flooding field of blank WHITE that is eating inward, dissolving the
gold borders at its edges into ink-wash bleed and smear (Sienkiewicz/McKean dissolution texture)
where it meets the white.

In the single WHITE panel sitting inside that widening gutter stands THE WITNESS: the same man
as Vane but plain, younger, unadorned — no gold, no suit, calm, watching, occupying the white,
completely unbothered. He is drawn in a simpler, softer line than the rigid Vane panels.

Action across the page: Vane, in the intact gold panels, is visibly forcing the grid back
together — borders re-gilding, a cracked reflection of his face redrawing itself clean, panels
snapping square. It is mostly working. But the one white gutter stays open and leaking, and the
Witness is still standing in it.

Caption boxes (Vane's cold gold voice, but strained): "I BUILT ALL OF THIS." / a second caption
in a calmer, different cadence, not gold-bordered: "and none of it is load-bearing."

High resolution; the contrast between rigid gold control and the flooding white must be
unmistakable; all lettering legible and correctly spelled.
```

**Watch:** the white must read as *the page's own structure failing*, not as "a white
background." The leaking gutter + dissolving borders are the whole point. The Witness in simpler
linework vs. Vane in rigid hyperdetail is the host-vs-alter "two drawing systems" idea — keep
them visibly different hands.

---

## TEST 3 (optional, ambitious) — the war page

*Only if 1 and 2 read well. The two registers at maximum tension on one page: CLARION redrawing,
the solvent flooding, neither winning — the koan made visual ("the self can't use itself to save
itself"). Spec this after we see whether the model holds the gutter trick at all.*

---

## After the batch

If the two registers render and the gutter-failure reads, the conceit is proven and we build the
full opening 6 in sequence. If the gutter trick won't render in one shot, fallback: build each
page as separate panels with deliberately-controlled white space and composite — which also
matches how a real comic page is assembled.

---

## Run log - 2026-05-31 Codex register probes

Output folder:
`the-solvent/outputs/opening-tests/2026-05-31-register-probes/`

| Test | Output | Verdict |
|------|--------|---------|
| TEST 1 - PAGE 1: CLARION register | `test-1-page-1-clarion-register.png` | Strong gold monument look, repeated self-image, readable captions. Grid is controlled but not perfectly equal-panel. |
| TEST 2 - solvent register | `test-2-solvent-register.png` | Strong central white gutter, gold borders failing, Witness reads as a different drawing system. |
| TEST 3 - war page | `test-3-war-page.png` | Strong left/right register split, Vane repairing gold structure, Witness in the white, captions survived cleanly. |

Original Codex generated-image folder:
`$HOME/.codex/generated_images/019e7ce1-0fa7-7cc3-979f-9589144b4eb8/`
