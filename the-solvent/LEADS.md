# LEADS — reading + visual-reference moodboard

Tracking list pulled from the source chat. Two buckets: **(1) read** for how form-as-content
works in the space; **(2) reference** to deconstruct into generation prompts. The pipeline (the
move your friend made with the Manson/Topanga underground panel): find a panel that nails a
specific shading/texture, paste or describe it, and I reverse it into a precise prompt — line
weight, hatching type, ink behavior, palette, paper stock — for the autoregressive image model.

> Note: the underground/psychedelic vein below is the *same vein* the friend's Topanga-Manson
> panel came from — and that panel is what kicked off this whole storyboarding thread. The
> deconstruct-a-panel-into-a-prompt workflow is already proven on it.

## (1) READING — kin in the space

- [ ] **Watchmen** — Moore / Gibbons. The Dr Manhattan one. Strict **nine-panel grid** as a
      control device; ch. IV renders nonlinear consciousness purely through panel order. → this
      grid IS the CLARION register.
- [ ] **Promethea** — Moore / **J.H. Williams III**. The single best precedent for the whole
      idea: as the character ascends, Williams **rebuilds the page itself**; layouts become
      architecture, the self dissolves into structure. Form enacts content, gold and illuminated.
- [ ] **The Filth** — Morrison / Chris Weston. The alter mechanic, basically: a man who may be
      two people (a sad nobody and a deep-cover agent) who can't tell which is real. Grubbier
      sibling to *The Invisibles*.
- [ ] **Asterios Polyp** — Mazzucchelli. Characters drawn in **different visual languages**;
      page style shifts with psychological state. → host-vs-Witness as two drawing systems on
      one page.
- [ ] **Jim Woodring — the Frank books.** Wordless dreamspace; ego dissolution as a journey
      through a morphing inner world. No-self phenomenology with **zero captions**.
- [ ] *Honorable mentions:* **Enigma** (Milligan/Fegredo); **Black Hole** (Burns); **Here**
      (McGuire) for the time-strip gutter trick.

## (2) VISUAL REFERENCE — by register, with prompt-vocab to lift

### CLARION / control / gold monument
- [ ] **Chris Ware** — *flat planar color, isometric diagram, ruler-straight borders, clinical
      symmetry, ligne claire, muted limited palette, zero crosshatch.*
- [ ] **J.H. Williams III (on Promethea)** — *art nouveau ornament, illuminated-manuscript gold
      leaf, page-as-architecture, Mucha decorative borders.*
- [ ] **Geof Darrow (Hard Boiled)** — the "CLARION sees everything" look. *maximalist
      hyperdetail, every surface rendered, obsessive uniform thin ink line, no negative space.*

### the solvent / dissolution / white eating inward
- [ ] **Bill Sienkiewicz (Stray Toasters, Elektra: Assassin)** — the reference for psychic
      dissolution. *mixed-media collage, ink-wash bleed, smeared acrylic, figure dissolving into
      abstraction, expressionist distortion.*
- [ ] **Dave McKean (Cages, Arkham Asylum)** — the Witness and the smear-portrait. *photomontage
      over ink, painterly texture, fractured layered portrait, dreamlike ambiguity.*
- [ ] **Nate Powell (Swallow Me Whole)** — dissociation specifically. *fluid brush ink, heavy
      spotted blacks, lettering bleeding into the art, woozy tilted perspective.*

### dark-night chapters
- [ ] **Eddie Campbell (From Hell)** — *nervous scratchy crosshatch, scratchboard,
      claustrophobic ink shadow, unfinished sketchy line.*
- [ ] **Charles Burns (Black Hole)** — *high-contrast solid blacks, clean smooth menacing line,
      glossy 1950s-clean-but-wrong.*

### underground / psychedelic (the friend's-panel vein)
- [ ] **Robert Crumb** — canonical underground shading. *feathered underground-comix crosshatch,
      bigfoot grotesque, vintage newsprint tone.*
- [ ] **Rick Griffin / Zap Comix** — *psychedelic melting organic lettering, vibrating
      complementary color, eyeball-and-flame surrealism.*
- [ ] **Moebius (Arzach, The Airtight Garage)** — the bridge between registers: precise thin
      line rendering dissolving content. *clear thin ligne-claire line, flat psychedelic desert
      vista, serene surreal sci-fi.*

## How to use this with me

Drop reference panels into `refs/` (or paste/describe them). For each, I'll write a
deconstruction: the exact line/hatch/ink/palette/paper vocab → a fireable prompt. As pages get
built they go in `prompts/`.
