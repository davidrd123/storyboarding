#!/usr/bin/env python3
"""Session archive: immutable lineage, 3-state ban-list, niche map, metrics.

Design commitments this file enforces:
- Lineage is immutable: seeds can be added, flagged, or marked duplicate —
  never edited or deleted. The nursery is never emptied mid-session.
- Ban-list has three states (a mechanism is the seed's core creative move):
    round      banned for the current batch only (prevents near-duplication)
    exhausted  explored enough this session; rejected until session ends
    protected  earned platform status (passed the 3-executions platform
               test); depth is ENCOURAGED — never auto-banned
- Metrics are pool-level (mechanism classes, niche occupancy, dedup survival,
  marginal uniqueness per batch) because collapse is invisible per-idea.

Commands:
  init FILE --name NAME
  add FILE --text T --mechanism M --operator OP [--stimulus S] [--parent ID]
           [--niche k=v ...] [--flag F ...]
  ban FILE MECHANISM --state round|exhausted|protected [--evidence TEXT]
  new-batch FILE               (clears round bans, increments batch)
  mark-dup FILE ID --of ID
  lineage FILE ID
  list FILE [--batch N]
  metrics FILE
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path


def load(path):
    return json.loads(Path(path).read_text())


def save(path, state):
    Path(path).write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n")


def cmd_init(args):
    if Path(args.file).exists():
        sys.exit(f"{args.file} already exists — sessions are append-only, start a new file")
    save(args.file, {"name": args.name, "batch": 1, "seeds": [], "banlist": {}})
    print(f"initialized session '{args.name}' at {args.file}")


def cmd_add(args):
    state = load(args.file)
    mech = args.mechanism.strip().lower()
    entry = state["banlist"].get(mech)
    if entry:
        if entry["state"] == "round" and entry["batch"] == state["batch"]:
            sys.exit(f"REJECTED: mechanism '{mech}' is round-banned in batch {state['batch']} — "
                     f"vary the mechanism, not the costume (or start a new batch)")
        if entry["state"] == "exhausted":
            sys.exit(f"REJECTED: mechanism '{mech}' is exhausted this session")
        # protected: depth encouraged, fall through
    niche = {}
    for kv in args.niche or []:
        if "=" not in kv:
            sys.exit(f"--niche must be key=value, got {kv!r}")
        k, v = kv.split("=", 1)
        niche[k.strip()] = v.strip().lower()
    seed_id = f"s{len(state['seeds']) + 1:03d}"
    state["seeds"].append({
        "id": seed_id,
        "batch": state["batch"],
        "text": args.text,
        "mechanism": mech,
        "operator": args.operator,
        "stimulus": args.stimulus,
        "parent": args.parent,
        "niche": niche,
        "flags": args.flag or [],
        "dup_of": None,
    })
    # every mechanism is round-banned the moment it is used, unless protected
    if not entry or entry["state"] != "protected":
        state["banlist"][mech] = {"state": "round", "batch": state["batch"]}
    save(args.file, state)
    print(seed_id)


def cmd_ban(args):
    state = load(args.file)
    mech = args.mechanism.strip().lower()
    if args.state == "protected" and not args.evidence:
        sys.exit("protected status must be EARNED: pass --evidence with the 3 one-line "
                 "executions that prove this mechanism is a platform")
    state["banlist"][mech] = {"state": args.state, "batch": state["batch"]}
    if args.evidence:
        state["banlist"][mech]["evidence"] = args.evidence
    save(args.file, state)
    print(f"{mech}: {args.state}")


def cmd_new_batch(args):
    state = load(args.file)
    state["banlist"] = {m: e for m, e in state["banlist"].items() if e["state"] != "round"}
    state["batch"] += 1
    save(args.file, state)
    print(f"batch {state['batch']} (round bans cleared)")


def cmd_mark_dup(args):
    state = load(args.file)
    ids = {s["id"] for s in state["seeds"]}
    if args.id not in ids or args.of not in ids:
        sys.exit("unknown seed id")
    for s in state["seeds"]:
        if s["id"] == args.id:
            s["dup_of"] = args.of
    save(args.file, state)
    print(f"{args.id} marked duplicate of {args.of}")


def cmd_lineage(args):
    state = load(args.file)
    by_id = {s["id"]: s for s in state["seeds"]}
    cur = by_id.get(args.id) or sys.exit("unknown seed id")
    chain = []
    while cur:
        chain.append(cur)
        cur = by_id.get(cur["parent"])
    for s in reversed(chain):
        print(f"{s['id']} [{s['operator']} | stim: {s['stimulus'] or '-'} | mech: {s['mechanism']}] {s['text'][:90]}")


def cmd_list(args):
    state = load(args.file)
    for s in state["seeds"]:
        if args.batch and s["batch"] != args.batch:
            continue
        dup = f" DUP({s['dup_of']})" if s["dup_of"] else ""
        flags = f" [{','.join(s['flags'])}]" if s["flags"] else ""
        print(f"{s['id']} b{s['batch']} <{s['mechanism']}>{dup}{flags} {s['text'][:100]}")


def cmd_metrics(args):
    state = load(args.file)
    seeds = state["seeds"]
    if not seeds:
        sys.exit("no seeds yet")
    unique = [s for s in seeds if not s["dup_of"]]
    mechs = Counter(s["mechanism"] for s in unique)
    niches = Counter(json.dumps(s["niche"], sort_keys=True) for s in unique if s["niche"])
    print(f"seeds: {len(seeds)} total, {len(unique)} after dedup "
          f"(survival {100 * len(unique) / len(seeds):.0f}%)")
    print(f"mechanism classes: {len(mechs)} distinct / {len(unique)} unique seeds "
          f"(flexibility {100 * len(mechs) / len(unique):.0f}%)")
    print("mechanism histogram (watch for a fat head — that's collapse):")
    for m, c in mechs.most_common():
        marker = " ◀ concentrated" if c >= max(3, 0.25 * len(unique)) else ""
        print(f"  {c:3d}  {m}{marker}")
    print(f"niche occupancy: {len(niches)} distinct niche combos")
    sparse = [n for n, c in niches.items() if c == 1]
    if sparse:
        print(f"  sparse niches (seed the next batch from these): {len(sparse)}")
        for n in sparse[:8]:
            print(f"    {n}")
    print("marginal uniqueness per batch (new mechanism classes; stop/switch when ~0):")
    seen = set()
    for b in range(1, state["batch"] + 1):
        batch_mechs = {s["mechanism"] for s in unique if s["batch"] == b}
        new = batch_mechs - seen
        seen |= batch_mechs
        total_b = sum(1 for s in seeds if s["batch"] == b)
        if total_b:
            print(f"  batch {b}: {total_b} seeds, {len(new)} new mechanism classes")
    banned = Counter(e["state"] for e in state["banlist"].values())
    print(f"ban-list: {dict(banned)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init"); p.add_argument("file"); p.add_argument("--name", required=True); p.set_defaults(fn=cmd_init)

    p = sub.add_parser("add")
    p.add_argument("file")
    p.add_argument("--text", required=True)
    p.add_argument("--mechanism", required=True, help="the seed's core creative move, e.g. 'peel-as-material-transfer'")
    p.add_argument("--operator", required=True)
    p.add_argument("--stimulus", default=None, help="the external entropy that produced it (card text, word, cell)")
    p.add_argument("--parent", default=None)
    p.add_argument("--niche", action="append", help="k=v, repeatable (e.g. fantasy=escape scale=personal)")
    p.add_argument("--flag", action="append", help="e.g. unbridged, cliche-tagged")
    p.set_defaults(fn=cmd_add)

    p = sub.add_parser("ban")
    p.add_argument("file"); p.add_argument("mechanism")
    p.add_argument("--state", required=True, choices=["round", "exhausted", "protected"])
    p.add_argument("--evidence", help="required for protected: the 3 one-line executions")
    p.set_defaults(fn=cmd_ban)

    p = sub.add_parser("new-batch"); p.add_argument("file"); p.set_defaults(fn=cmd_new_batch)

    p = sub.add_parser("mark-dup"); p.add_argument("file"); p.add_argument("id"); p.add_argument("--of", required=True); p.set_defaults(fn=cmd_mark_dup)

    p = sub.add_parser("lineage"); p.add_argument("file"); p.add_argument("id"); p.set_defaults(fn=cmd_lineage)

    p = sub.add_parser("list"); p.add_argument("file"); p.add_argument("--batch", type=int); p.set_defaults(fn=cmd_list)

    p = sub.add_parser("metrics"); p.add_argument("file"); p.set_defaults(fn=cmd_metrics)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
