#!/usr/bin/env python3
"""Fragment store: coincidence-threshold retrieval + bounded reminding cascade.

Mueller/DAYDREAMER mechanics (latent-dreamer condensation):
- Retrieval is COINCIDENCE COUNTING, not semantic similarity: a fragment
  surfaces when marks >= threshold, i.e. when several independent cues
  converge on it. Serendipity mode lowers the threshold by 1.
- The reminding cascade turns one retrieval into a bounded associative
  stream: a retrieved fragment's OTHER index values become new cues,
  bounded by small recency FIFOs (recent indices <= 6, recent fragments <= 4).
- The store is usage-unbiased: nothing here records or ranks by past use.

Store format (JSON):
  {"fragments": [{"id": "f001", "text": "...", "source": "...",
                  "tags": {"physical-operation": ["peel", "unroll"], ...}}]}

Commands:
  validate STORE
  retrieve STORE --cues peel,escape,rind [--threshold 2] [--serendipity]
  cascade STORE --seed-id f001 [--hops 2]
  probe [--size 60] [--trials 500] [--cues 6] [--store STORE]
"""
import argparse
import json
import random
import sys
from collections import deque
from pathlib import Path

FAMILIES = [
    "physical-operation",
    "material-behavior",
    "spatial-relation",
    "emotional-fantasy",
    "social-configuration",
    "temporal-behavior",
    "formal-medium",
    "transition-affordance",
    "product-fact",
    "productive-contradiction",
]

RECENT_INDICES_CAP = 6   # Mueller's recency bounds
RECENT_FRAGMENTS_CAP = 4


def load_store(path):
    store = json.loads(Path(path).read_text())
    frags = store.get("fragments")
    if not isinstance(frags, list) or not frags:
        sys.exit(f"{path}: no fragments")
    return frags


def index_values(frag):
    """All (family, value) index pairs of a fragment."""
    return [(fam, v) for fam, vals in frag.get("tags", {}).items() for v in vals]


def marks_for(frag, cues):
    """Coincidence count: how many distinct cues hit this fragment's values."""
    values = {v for _, v in index_values(frag)}
    return sorted(c for c in cues if c in values)


def cmd_validate(args):
    frags = load_store(args.store)
    errors, ids = [], set()
    for i, f in enumerate(frags):
        fid = f.get("id", f"<index {i}>")
        if fid in ids:
            errors.append(f"duplicate id: {fid}")
        ids.add(fid)
        if not f.get("text"):
            errors.append(f"{fid}: missing text")
        tags = f.get("tags", {})
        unknown = set(tags) - set(FAMILIES)
        if unknown:
            errors.append(f"{fid}: unknown families {sorted(unknown)}")
        nonempty = [fam for fam, vals in tags.items() if vals]
        if len(nonempty) < 3:
            errors.append(f"{fid}: only {len(nonempty)} index families (need >=3 for orthogonal multi-indexing)")
        for fam, vals in tags.items():
            for v in vals:
                if not isinstance(v, str) or v != v.lower().strip():
                    errors.append(f"{fid}: tag value {v!r} must be lowercase/trimmed")
    # store-level: warn if any single value indexes >30% of the store
    counts = {}
    for f in frags:
        for _, v in set(index_values(f)):
            counts[v] = counts.get(v, 0) + 1
    for v, c in sorted(counts.items(), key=lambda kv: -kv[1]):
        if c > 0.3 * len(frags):
            errors.append(f"WARN: value '{v}' indexes {c}/{len(frags)} fragments — near-useless as a coincidence cue")
    if errors:
        print("\n".join(errors))
        sys.exit(1 if any(not e.startswith("WARN") for e in errors) else 0)
    print(f"OK: {len(frags)} fragments, {len(counts)} distinct index values")


def cmd_retrieve(args):
    frags = load_store(args.store)
    cues = [c.strip().lower() for c in args.cues.split(",") if c.strip()]
    threshold = max(1, args.threshold - (1 if args.serendipity else 0))
    hits = []
    for f in frags:
        matched = marks_for(f, cues)
        if len(matched) >= threshold:
            hits.append((len(matched), matched, f))
    hits.sort(key=lambda h: -h[0])
    for n, matched, f in hits:
        print(json.dumps({"id": f["id"], "marks": n, "matched": matched, "text": f["text"]}, ensure_ascii=False))
    print(f"# {len(hits)}/{len(frags)} retrieved (threshold {threshold}, cues {cues})", file=sys.stderr)


def cmd_cascade(args):
    frags = load_store(args.store)
    by_id = {f["id"]: f for f in frags}
    if args.seed_id not in by_id:
        sys.exit(f"unknown fragment id: {args.seed_id}")
    by_value = {}
    for f in frags:
        for _, v in set(index_values(f)):
            by_value.setdefault(v, []).append(f["id"])

    recent_indices = deque(maxlen=RECENT_INDICES_CAP)
    recent_fragments = deque(maxlen=RECENT_FRAGMENTS_CAP)
    stream = []

    def remind(fid, via, depth):
        if depth > args.hops or fid in recent_fragments:
            return
        recent_fragments.append(fid)
        stream.append({"id": fid, "via": via, "depth": depth, "text": by_id[fid]["text"]})
        for _, value in index_values(by_id[fid]):
            if value in recent_indices:
                continue
            recent_indices.append(value)
            for other in by_value.get(value, []):
                if other != fid:
                    remind(other, value, depth + 1)

    remind(args.seed_id, "seed", 0)
    for item in stream:
        print(json.dumps(item, ensure_ascii=False))
    print(f"# cascade of {len(stream)} fragments from {args.seed_id} (hops <= {args.hops})", file=sys.stderr)


def synthetic_store(size, rng, values_per_family=8, families_per_frag=(3, 5), values_per_index=(1, 2)):
    vocab = {fam: [f"{fam.split('-')[0]}{i}" for i in range(values_per_family)] for fam in FAMILIES}
    frags = []
    for i in range(size):
        fams = rng.sample(FAMILIES, rng.randint(*families_per_frag))
        tags = {fam: rng.sample(vocab[fam], rng.randint(*values_per_index)) for fam in fams}
        frags.append({"id": f"s{i:03d}", "text": f"synthetic fragment {i}", "tags": tags})
    all_values = sorted({v for f in frags for _, v in index_values(f)})
    return frags, all_values


def cmd_probe(args):
    rng = random.Random(args.seed)
    if args.store:
        frags = load_store(args.store)
        all_values = sorted({v for f in frags for _, v in index_values(f)})
        label = args.store
    else:
        frags, all_values = synthetic_store(args.size, rng)
        label = f"synthetic n={args.size}"
    print(f"probe: {label}, {len(frags)} fragments, {len(all_values)} distinct values, "
          f"{args.cues} cues/trial, {args.trials} trials")
    print(f"{'thr':>3} {'mean':>6} {'med':>4} {'max':>4} {'zero%':>6} {'flood%':>7}   verdict")
    flood_cut = max(1, int(0.3 * len(frags)))
    for threshold in (1, 2, 3, 4):
        counts = []
        for _ in range(args.trials):
            cues = rng.sample(all_values, min(args.cues, len(all_values)))
            counts.append(sum(1 for f in frags if len(marks_for(f, cues)) >= threshold))
        counts.sort()
        mean = sum(counts) / len(counts)
        med = counts[len(counts) // 2]
        zero = 100 * sum(1 for c in counts if c == 0) / len(counts)
        flood = 100 * sum(1 for c in counts if c > flood_cut) / len(counts)
        if zero > 50:
            verdict = "DEGENERATE (mostly empty)"
        elif flood > 50:
            verdict = "DEGENERATE (mostly floods)"
        elif 1 <= med <= 6 and zero < 35:
            verdict = "usable"
        else:
            verdict = "marginal"
        print(f"{threshold:>3} {mean:>6.1f} {med:>4} {counts[-1]:>4} {zero:>5.0f}% {flood:>6.0f}%   {verdict}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("validate"); p.add_argument("store"); p.set_defaults(fn=cmd_validate)

    p = sub.add_parser("retrieve")
    p.add_argument("store"); p.add_argument("--cues", required=True)
    p.add_argument("--threshold", type=int, default=2)
    p.add_argument("--serendipity", action="store_true", help="lower threshold by 1 (Mueller)")
    p.set_defaults(fn=cmd_retrieve)

    p = sub.add_parser("cascade")
    p.add_argument("store"); p.add_argument("--seed-id", required=True)
    p.add_argument("--hops", type=int, default=2)
    p.set_defaults(fn=cmd_cascade)

    p = sub.add_parser("probe")
    p.add_argument("--store", help="probe a real store instead of synthetic")
    p.add_argument("--size", type=int, default=60)
    p.add_argument("--trials", type=int, default=500)
    p.add_argument("--cues", type=int, default=6)
    p.add_argument("--seed", type=int, default=7)
    p.set_defaults(fn=cmd_probe)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
