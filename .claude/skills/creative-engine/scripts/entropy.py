#!/usr/bin/env python3
"""All randomness for the creative-engine skill lives here.

The model must NEVER pick its own random stimulus — asked for "a random word"
it samples its mode. Every draw comes from this script's RNG, external to the
model. Use --seed only to reproduce a previous session's draws.

Commands:
  decks                       list available decks
  draw DECK [-n N]            draw N lines from a deck (references/decks/)
  word [-n N]                 random concrete nouns (decks/nouns.txt)
  dictword [-n N]             random words from /usr/share/dict/words
  operator [-n N]             draw a core operator (decks/operators.txt)
  nplus7 "SENTENCE" [--offset 7]   Oulipo N+7 via system dictionary
  zwicky BOX.json [--draws N]      one value per parameter, N configurations
  shuffle                     shuffle stdin lines (cut-ups)
  pick A B C ...              pick one of the given arguments
  int --min A --max B         random integer in [A, B]
"""
import argparse
import json
import random
import re
import sys
from pathlib import Path

DECKS = Path(__file__).resolve().parent.parent / "references" / "decks"
SYSDICT = Path("/usr/share/dict/words")

STOPWORDS = set(
    """the a an and or but if then than this that these those it its is are was
    were be been being have has had do does did will would could should may
    might must shall can not no nor so very just only also with without into
    onto from for of in on at by to as when while where which who whom whose
    what how why all any both each few more most other some such own same too
    s t don now he she they we you i his her their our your my me him them us
    one two there here out up down over under again once during before after
    about against between through above below off further because until"""
    .split()
)


def load_deck(name: str) -> list[str]:
    for candidate in (Path(name), DECKS / name, DECKS / f"{name}.txt"):
        if candidate.is_file():
            lines = [l.strip() for l in candidate.read_text().splitlines()]
            deck = [l for l in lines if l and not l.startswith("#")]
            if not deck:
                sys.exit(f"deck is empty: {candidate}")
            return deck
    sys.exit(f"deck not found: {name} (looked in {DECKS})")


def sysdict_words() -> list[str]:
    if not SYSDICT.is_file():
        sys.exit(f"system dictionary not found at {SYSDICT}")
    return [
        w for w in SYSDICT.read_text().splitlines()
        if w.islower() and w.isalpha() and 3 <= len(w) <= 14
    ]


def cmd_draw(args):
    deck = load_deck(args.deck)
    n = min(args.n, len(deck))
    for line in random.sample(deck, n):
        print(line)


def cmd_word(args):
    cmd_draw(argparse.Namespace(deck="nouns", n=args.n))


def cmd_dictword(args):
    words = sysdict_words()
    for w in random.sample(words, args.n):
        print(w)


def cmd_operator(args):
    cmd_draw(argparse.Namespace(deck="operators", n=args.n))


def cmd_nplus7(args):
    words = sysdict_words()
    index = {w: i for i, w in enumerate(words)}
    out = []
    for token in re.findall(r"\w+|\W+", args.sentence):
        low = token.lower()
        if low.isalpha() and low not in STOPWORDS and low in index and len(low) > 3:
            repl = words[(index[low] + args.offset) % len(words)]
            if token[0].isupper():
                repl = repl.capitalize()
            out.append(repl)
        else:
            out.append(token)
    print("".join(out))


def cmd_zwicky(args):
    src = sys.stdin.read() if args.box == "-" else Path(args.box).read_text()
    box = json.loads(src)
    if not isinstance(box, dict) or not all(isinstance(v, list) and v for v in box.values()):
        sys.exit('box must be JSON like {"parameter": ["value1", "value2", ...], ...}')
    for i in range(args.draws):
        config = {param: random.choice(values) for param, values in box.items()}
        print(json.dumps(config, ensure_ascii=False))


def cmd_shuffle(args):
    lines = [l for l in sys.stdin.read().splitlines() if l.strip()]
    random.shuffle(lines)
    print("\n".join(lines))


def cmd_pick(args):
    print(random.choice(args.items))


def cmd_int(args):
    print(random.randint(args.min, args.max))


def cmd_decks(args):
    if not DECKS.is_dir():
        sys.exit(f"no decks directory at {DECKS}")
    for p in sorted(DECKS.glob("*.txt")):
        count = sum(
            1 for l in p.read_text().splitlines() if l.strip() and not l.startswith("#")
        )
        print(f"{p.stem:24s} {count:4d} entries")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seed", type=int, help="reproduce a previous session's draws")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("draw"); p.add_argument("deck"); p.add_argument("-n", type=int, default=1); p.set_defaults(fn=cmd_draw)
    p = sub.add_parser("word"); p.add_argument("-n", type=int, default=1); p.set_defaults(fn=cmd_word)
    p = sub.add_parser("dictword"); p.add_argument("-n", type=int, default=1); p.set_defaults(fn=cmd_dictword)
    p = sub.add_parser("operator"); p.add_argument("-n", type=int, default=1); p.set_defaults(fn=cmd_operator)
    p = sub.add_parser("nplus7"); p.add_argument("sentence"); p.add_argument("--offset", type=int, default=7); p.set_defaults(fn=cmd_nplus7)
    p = sub.add_parser("zwicky"); p.add_argument("box", help="JSON file or - for stdin"); p.add_argument("--draws", type=int, default=1); p.set_defaults(fn=cmd_zwicky)
    p = sub.add_parser("shuffle"); p.set_defaults(fn=cmd_shuffle)
    p = sub.add_parser("pick"); p.add_argument("items", nargs="+"); p.set_defaults(fn=cmd_pick)
    p = sub.add_parser("int"); p.add_argument("--min", type=int, default=1); p.add_argument("--max", type=int, default=100); p.set_defaults(fn=cmd_int)
    p = sub.add_parser("decks"); p.set_defaults(fn=cmd_decks)

    args = ap.parse_args()
    if args.seed is not None:
        random.seed(args.seed)
    args.fn(args)


if __name__ == "__main__":
    main()
