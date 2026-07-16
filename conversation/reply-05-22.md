## Context — Ben's model-test messages (precede the reply below)

**5/21, 6:03 PM — model comparison, prompt ≈ "Ahab on a boat" in storyboard/comic style:**
- `gpt-image-2-edit` (2m 34s): delivered. Ahab in long coat with cane on a storm-lashed ship deck, B&W ink/crosshatch.
- `nano-banana-2-edit` (19.6s): delivered. Captain figure on deck, lightning + rigging, same comic register. Fast.
- `fal-flux-2-edit` (6.5s): failed. Ben's note: "flux didn't give me Ahab on a boat OR the style." Output was unrelated 1950s figures at a columned building — wrong subject and off-style.

**5/22, 12:38 PM — Seedream observation + LoRA re-ask:**
- On Seedream (5.0 Lite, *closed-source*): "INCREDIBLY style coherent / consistent, but terrible at understanding what you wanted the scene to be."
- Re-asked: "$50 to train a LoRA so I can round out the test I'm running."
- Attached a golden-age "rip Kirby" style test image: B&W vintage-comic illustration, period 1950s figures (man waving, man in suit with briefcase, two women in dresses) before a columned building. Style-coherent, generic/unspecified scene — illustrates the Seedream point.

**Net pattern:** style-coherent generators (Flux, open / Seedream, closed) hold the look but miss the requested scene; the reasoning models (Nano Banana, GPT Image) hold scene control. Control is a property of instruction-following, not style quality, training, or licensing. → reply below.


Actual Discord Precding two messages
<discord>
David D — 12:22 AM
yeah that sums up where I'd also say things stand - need to use NB2 or GPT Image-2 for controllability - and NB2 is much faster to iterate with, open source models aren't nearly controllable enough
And NB2 is in the sweet spot time-wise. 
I'm not clear how much better GPT Image 2 is for controllability or style yet but rn assuming that all that thinking is producing something extra that could be drawn upon 
Ben Hansford — 12:38 PM
weirdly -- seadream is INCREDIBLY style coherent / consistent -- but terrible at understanding what you wanted the scene to be
se above.  any chance I could kick you some dinner money (50$) to train a LoRA so I can round out the test I'm running?
testing this golden age rip kirby artwork
</discord>

---

## Claude suggestion for Reply

<v1>
ha, that tracks. seedream and flux are the same story: gorgeous style, can't hold the scene you asked for. 
that's the whole style-coherent open-model category, and it's exactly why a trained LoRA won't round out the test the way you're hoping. it'll come out the same, great style, weak scene control, just a third point on that curve. it tells you what Flux and Seedream already did. the one model that holds both style and scene control is Nano Banana, which is why it's the controllability answer. I'd honestly save the $50 and just lean on NB for that. I'm buried with my own deadlines plus jury duty next week so I can't take training on right now regardless, but happy to keep trading notes.
</v1>

<v2>
ha, that tracks. funny part is seadream's closed and flux is open, but they land the exact same way: gorgeous style, can't hold the scene you asked for. so it's not an open-vs-closed thing. the models that actually nail scene control are the reasoning ones, Nano Banana and GPT Image, because the control comes from the instruction-following, not from style quality or training. which is why a style LoRA won't round out the test the way you want: it'd come out like seadream and flux, great look, weak control, telling you what you already know. NB's the only one holding both, so I'd save the $50 and just lean on it. I'm buried with my own deadlines plus jury duty next week anyway, but happy to keep trading notes.
</v2>

<!-- v3 rationale: drops the open/closed framing entirely. It's not anything Ben raised, and David's
     own 12:22 msg already said "open source models aren't controllable enough" -- so leaning on
     "it's not open-vs-closed" would walk back his own prior framing for no gain. Also avoids
     asserting Seedream's architecture (unknown). Rests on Ben's observed behavior + the one claim
     that holds regardless of any model's internals: a style LoRA buys the look, not scene control.
     (The closed-≠-controllable nuance is a real refinement to David's own model -> keep it in repo
     FINDINGS notes, not in the reply.) -->
<v3>
ha, that tracks - that seems to be the pattern at the moment with the style-first models: they nail the look but can't hold the scene you asked for. 

which is exactly why a trained LoRA won't round out the test the way you're hoping. training a style only buys you the look, it doesn't touch scene control - and scene control is the part that's actually failing. 

so it'd come out like seadream and flux: great style, weak on holding the scene. just a third point on the same curve. Nano Banana's the one that holds both, which is why it's the controllability answer. I'd save the $50 and lean on NB. buried with my own deadlines + jury duty next week anyway, but happy to keep trading notes.
</v3>

<!-- RESERVE — do not send unless Ben opens the door. v3 is the clean close; these are answers held
     in reserve for the two counters he might raise. Spending them pre-emptively turns the close into
     a debate-invite. If he raises one, firing the matching line is a one-shot answer, not a thread. -->

<!-- Counter 1: "but couldn't captioning the training data add control?" -->
<v3-followup-captioning>
captioning helps the LoRA invoke the style and bind concepts it actually saw in training - but it can't raise the base model's compositional ceiling, and a board is all novel scenes, which is exactly what captioning can't generalize to. the control you can borrow is whatever the base already has; you can't caption compositionality into it. that's why it keeps landing back on NB.
</v3-followup-captioning>

<!-- Counter 2: "so build a big enough captioned dataset that covers the range." -->
<!-- The dataset is the real blocker, and it's blocked from BOTH sides:
       (a) Real data: can't find enough comic art in ONE consistent target style that ALSO spans the
           compositional range (angles, blocking, multi-char staging). Style-consistency and
           compositional-coverage pull against each other in found data - that corpus doesn't exist.
       (b) Synthetic data from NB: circular. If NB can already generate the on-style, correctly-composed
           images you'd caption and train on, you've just proven you don't need the LoRA. And distilling
           into a weaker base captures the specific OUTPUTS (those scenes), not the CAPABILITY (arbitrary
           novel scenes). The snake eats its tail: the only way to assemble a compositionally-rich style
           set is to already have the model that does composition - the one you'd then not be replacing. -->
<v3-followup-dataset>
yeah, and that's the actual blocker - to get the full range you'd need every composition present and captioned in the training set, and that corpus doesn't exist: you can't find enough comic art in one consistent style that also covers all the staging you'd need. the only way to manufacture it is synthetic from NB itself, at which point you've proven you don't need the LoRA - you'd just be copying NB's specific outputs into a weaker base, not its ability to compose new ones. so it routes back to NB either way.
</v3-followup-dataset>
