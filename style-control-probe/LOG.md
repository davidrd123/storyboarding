---
name: style-control-probe-log
description: "Running lab log for the style-control probe — session-level decisions, cross-branch findings, methodology/rigor items, and the experiment queue. The meta-layer above the per-branch prompts-*-active breadcrumbs."
title: "Style-Control Probe — Running Log"
type: lab_log
tags: [style_probe, lab_log]
tier: reference
status: living_document
system_directive: "Append a dated entry each working session. Per-generation detail belongs in the prompts-*-active breadcrumbs; durable cross-session facts belong in agent memory. This log is the narrative thread between them."
related:
  - "CLAUDE.md"
  - "prompts-litho-active.md"
  - "prompts-goya-active.md"
  - "prompts-greek-hybrid-active.md"
---

# Style-Control Probe — Running Log

The narrative thread for the probe. **Per-generation detail** lives in the `prompts-*-active` breadcrumbs; **durable cross-session facts** live in agent memory (`project_nb2-facture-ceiling`, `feedback_style-classification-via-gemini`). This log records what we decided and why, session by session.

Probe question (from `CLAUDE.md`): how faithfully can a closed model reproduce a MidJourney style-atom on a fresh subject, via the borrow-style-only grammar?

---

## 2026-05-23 — Hard-style branches + first cross-model facture test

**Headline:** NB2 locks *category-anchored* styles richly but hits a **structural facture ceiling**; **GPT-Image-2 clears that ceiling** (first cross-model data point). New source batch `MidJourney/2026-05-23/` cataloged (~10 distinct hands; broad fan-out, not one style).

### Branches this session

| Branch | Anchor (job) | Model | Best grade* | Verdict |
|---|---|---|---|---|
| 1 · search-line ink | Hephaestus `054e808b` | NB2 | ~80–88 | (prior session) line-based style locks easily |
| 2 · Goya-dark impasto | Saturn `c42475f0` | NB2 | ~50 (v01) | **Parked** — David: "looks terrible." Palette/value transfer (~85), facture does not (~15) |
| 3 · litho-crayon duotone | Cerberus `8f5831c8` | NB2 | 78 (v01) → 75 (v02) | facture wall: full physical recipe did **not** move it |
| 3 · litho-crayon duotone | Cerberus `8f5831c8` | **GPT-Image-2** | **82 (x01)** | **facture transferred**; new miss = over-rendering (promptable) |

\*Gemini compare grades — see "Rigor items" below for the caveat on what these numbers mean.

### Findings

1. **Predictor of style-lock = category-anchored vs. facture-anchored**, not "hard vs. easy." Styles that map to a recognizable print/illustration *category* (search-line, litho) invoke a strong prior and lock; a paint-*surface* style with no category handle (Goya impasto) gets flattened to clean render. → `project_nb2-facture-ceiling`.
2. **NB2's facture miss is a model ceiling, not a prompt miss.** Two escalating litho attempts (v01 light amplifier → v02 full tusche-crayon/pressure/grain recipe) hit the identical wall: NB2 paints clean marks and lays paper texture *passively behind* them rather than building marks *out of* the grain. Grade flat (78→75).
3. **The ceiling is NB2-specific.** Same prompt+ref+fence on GPT-Image-2 graded 82 and the crayon facture actually transferred ("paper grain + toothy crayon texture highly accurate"). GPT's failure mode is the *opposite* — too tight/detailed/illustrative (over-rendered), which is promptable. → **For facture-heavy print/paint styles, GPT-Image-2 > NB2.**
4. **Open-ended `describe`-style questions yield richer reproduction recipes than the structured 5-axis question** — surfaced levers the axis cage missed (e.g. NB2's ruler-straight perspective is itself a tell). → `feedback_style-classification-via-gemini` updated.

### Decisions (David, Direction Gates)

- Branch from search-line to a hard style → **Goya-dark** chosen → fired v01 → **parked** ("looks terrible").
- Pivot anchor to **Cerberus litho** → fired v01/v02 → hit facture wall.
- Past the ceiling → **try GPT-Image-2** (chosen over accept-~78 / post-process-grain / new-anchor) → x01 fired, 82.

### Rigor items (raised by David — OPEN)

1. **Grade calibration.** All Gemini calls this session used the **`analyze_image`** system prompt (the script default; `--system` never passed) — including the "deep describe" and the three "grades." So the 75/78/82 numbers are Gemini *free-handing* a score from my question, **not** the calibrated `score_image` bands or the `compare_images` rubric. Deltas are fair (same system prompt + question + temp 0.3); absolute numbers are not anchored. **TODO:** re-grade NB2-v02 vs GPT-x01 through `compare_images_system_prompt` before trusting the cross-model gap.
2. **Cross-model delivery confound.** NB2 received the style block via the dedicated `system_prompt` channel; GPT-Image-2's `images.edit` endpoint has no system slot, so `gen_openai.py` *prepends* the block into the single user prompt. **Same text, different channel.** **TODO (clean control):** re-run NB2-v02 with the block prepended into the user prompt + no system instruction; if it still can't reach facture, the channel wasn't the cause.
3. **Grader circularity.** Gemini is both the *source* of the fix language (its grade/recipe) and the *judge* of the result. Feeding its words back in and watching its score rise = teaching to the grader. Ground truth is the anchor + David's eye, not the rising number — keep these as Direction Gates.

### External input triaged (GPT-on-the-web NB2 prompting advice)

- Aimed at NB2, which we've parked for this style → apply the good ideas to **GPT-Image-2** (our lead), whose miss is promptable.
- Already doing: scene-based prompts; the 2-step describe-then-generate.
- Worth testing (single-variable): **multi-ref crops** (show the crude mark-making vs. tell — best fit for the over-rendering gap); **artist-list trim** (consistent with our calibration memory, though x01 *had* the list and scored highest — hypothesis, not a known win); **positive framing** over the negation wall.
- Treat skeptically: its "14 refs" figure and "Google recommends" citations are unverifiable browsing artifacts.
- Methodology catch: its rewrite bundles ~5 changes at once → adopt as ordered single-variable tests, not a wholesale swap.

### Speed reframe + NB2-first push (David: NB2 is ~20s, GPT-Image-2 ~100s — wants NB2 to work)

- **Post-process abandoned.** `scripts/litho_post.py` (ink-starvation + tooth + registration): naive v1 **regressed to 65** (chromatic-aberration fringing + uniform digital-noise speckle); fixed v2 (reg off, clumpy soft starvation) **recovered to 75** = clean-NB2 baseline, no gain. **Why it can't help:** the facture is in the *line* (heavy greasy mass-based crayon marks), and post is downstream of the line — grain has no heavy ink to break through, so it sits on top as "a flat digital layer." David: forget post.
- **Show-don't-tell (v03 multi-ref crops) = 78**, +3 over v02. Crops of the anchor's heavy ink-mass + crayon line moved NB2's line heavier (what words couldn't), but NB2 still defaults to straight perspective lines + uniform hatching. Mild composition convergence noted (foreground figure).

### Full leverboard — this litho style (FINAL)

| Run | Config | Grade | Speed |
|---|---|---|---|
| v04 | text-only, no refs | 55 | 20s |
| v02 | full recipe, 1 ref | 75 | 20s |
| v02+post | post-process grain | 75 (naive 65) | 20s |
| v03 | + crops | 78 | 20s |
| v05 | + crops, positive-framed | 75 | 20s |
| **v06** | **+ crops, artists trimmed** | **82** | **20s** |
| x01 | GPT-Image-2, 1 ref | 82 | ~100s |
| **x02** | **GPT-Image-2, + crops** | **85** | ~100s |

### Outcome — the mid-session "structural ceiling" call was WRONG

**Crops (show-don't-tell, David's suggestion) were the universal unlock** — lifted both models by *showing* the heavy mass-based crayon facture that *telling* (verbose recipe) couldn't. Combined with **dropping the artist names** (which were widening the basin — confirms `feedback_style-classification-via-gemini` + GPT-web's hunch), **NB2 reached 82**, tying GPT's no-crop run. GPT+crops tops out at **85**.

- **Production recipe (NB2, 20s):** deep-recipe block (keep negations) + artists removed + full frame + 2 crops = **82**.
- **Hero-frame ceiling (GPT-Image-2, ~100s):** + crops = **85**.
- 3-pt gap, within freehand-grade noise, for 5× speed → **NB2 is viable for this facture style.** Revises the earlier "NB2 facture ceiling ~78, structural" — it was partly a *prompting* limit (describe-not-show + artist-name basin), not purely the model.
- Negation wall: **keep** (positive framing −3). Text-only: **not viable** (55; refs load-bearing). Post-process: abandoned.
- **Shared residual on both models:** lines still a touch thin/precise, perspective too structured vs. the anchor's flat graphic abstraction. The new frontier, not an NB2 wall.

### Scene coverage works on NB2 (the storyboard payoff)

Treated the v06 master as an establishing wide and generated **coverage** — alternate camera setups of the *same* scene (refs = master + facture crops; **fence flipped** to preserve world/character, change only camera). Three angles all **PASS** (`prompts-coverage-active.md`): medium front-¾ (face readable), low-angle up the escalator into the tunnel, high-reverse down at the lone figure. Same character + set + litho style; the "BROKEN / OUT OF ORDER" sign persists across all three → NB2 held the *set as a place*, not just a restyle. Character identity is storyboard-consistent (archetype, not pixel-locked face).

**Why it matters:** style-repro (proven) + coverage (now proven) = the core storyboard premise holds — establish a styled master once, cover the scene fast on NB2.

**Extended (2026-05-24):**
- **Coverage off the RAW MJ source is even stronger** (Cerberus oc01–oc03 all pass): feeding the un-modified frame alone, NB2 held world+characters+facture AND *resolved* the scene (dog-head → explicit three-headed Cerberus; deep corridor reverse; preserved the "10.2.11" plate-date). Denser source = more continuity anchors. **Workflow shortcut: pick any MJ frame → cover it, no style-repro round-trip.**
- **Coverage generalizes across style families** (Hephaestus concept-art hc01–hc03 all pass): with a **generic "match the reference style" block** (no hand-built block), coverage works on clean concept-art too — even easier (NB2's native register). Down-the-line tracking + CU-with-bokeh-background = real spatial reasoning. **The coverage method is style-agnostic.**

### Experiment queue

- [x] post (abandoned) · [x] v03 crops (78) · [x] v04 text-only (55) · [x] v05 positive (75) · [x] v06 artist-trim (82) · [x] x02 GPT+crops (85) · [x] coverage c01–c03 (all pass)
- [ ] **Calibrated `compare_images` re-grade** of v06 (82) vs x02 (85) — confirm the freehand numbers before locking the NB2-vs-GPT call
- [ ] Coverage: push harder angles (OTS, reverse-180, insert detail); test character-face drift across a longer set; try GPT-master → NB2-coverage
- [ ] Validate the v06 NB2 recipe across more myth×modern subjects (does crops+artist-trim hold beyond Sisyphus?)
- [ ] *(open)* NB2 delivery-control run (block in user prompt vs system)

---

## 2026-05-24 — Seedance: storyboard page → video

Fed the Hephaestus storyboard page (hp-sp01 `_02`) to **Seedance 2.0** (`bytedance/seedance-2.0` via Replicate; new runner `scripts/gen_seedance.py` drives riff-mcp's `gemini_video_prompts_mcp.seedance` adapter — no Replicate MCP is connected, so we call the plumbing directly). 5s / 720p / 16:9 / first_last_frames mode (page = first frame), ~156s render.

**Result — "living storyboard":** Seedance pinned the 6-panel grid as frame 0 and **animated each panel in place, simultaneously, grid + labels preserved** (not a layout morph). Panel E's automaton head lands a welder spark-burst by the end; Hephaestus + the automaton line animate in the other panels; concept-art style held. The literal "animate the storyboard" reading produces an *animated boards page*, not a single continuous shot. For a real scene shot: extrapolate one panel → full frame → img2vid that (stage-2, pending). Output: `seedance-2.0/01_hephaestus-board-anim_bea0973c/`.

### Seedance follow-up — storyboard page → continuous oner (David's hypothesis, confirmed)

Re-fired the Hephaestus page to Seedance, but as an **ingredient reference** (`omni_reference`) instead of the first-frame anchor, prompted "synthesize ONE continuous take, do NOT reproduce the grid." 8s/720p, ~244s render. **Result: a true oner** — opens wide dollying down the automata line → arrives on Hephaestus → welder spark beat → settles on his weary face. NO grid; it threaded the page's coverage beats into one developing camera move, style+character held. **The only change from the first (grid-animating) run was the reference ROLE** (first-frame anchor → ingredient) + the synthesis instruction. → storyboard page → Seedance oner/animatic is a viable pipeline step. Output: `seedance-2.0/01_hephaestus-oner-from-board_20998783/`.

### Seedance oner from the GPT-180 board (2026-05-24)
Fed the higher-fidelity GPT-Image-2 coverage board as an ingredient ref, same "one continuous take" prompt, threading the "cradles the gold face" turning beat. 8s/720p. Richest video result yet — painterly depth from the GPT source held through; coherent oner (wide dolly → arrive on Hephaestus → intimate cradle of the automaton's face → hold on maker-and-creation). Output: `seedance-2.0/01_hephaestus-oner-from-gpt-board_8804cc57/`. NOTE (per `feedback_dont-over-conclude`): single-call oners compose their own continuous interpretation rather than replaying panels in order — but external examples (`conversation/patrick/HG*.jpeg`) got good results from numbered boards, so the storyboard→video method is OPEN, not closed; replicate-and-observe their workflow before concluding.

### Storyboard → video RESOLVED — ordered-beat ingredients (2026-05-24)
Fed 5 finished GPT-kit panels as named ingredients ([Image1..5], omni_reference) prompted as ordered BEATS the camera transitions through. **Seedance sequenced them into a paced animatic in one generation** — wide establish (0s) → automaton/gaze (4s) → hands on its face (6s) → lone smith before the ranks (9.8s). Honored the beat *arc* + order with cinematic pacing (not rigid 1→N; merged/added some beats with its own timing). Best video result of the session — richer + more coherent than the grid-page oner, better-paced than uniform manual cuts. **Corrects the earlier "Seedance freelances order" over-hedge: it sequences ordered beats when prompted (Patrick-proven, now ours too).** Winning method = clean consistent panels → named ordered-beat ingredients → one-gen sequenced animatic. Output: `seedance-2.0/01_hephaestus-panels-as-ingredients_eff12bbd/`.
