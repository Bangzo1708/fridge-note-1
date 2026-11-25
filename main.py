#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

A smart fridge leaves exactly one note on its door screen: a single,
dry, petty line for its owner. The note is fixed at build time, so the
program is deterministic -- every run writes the same bytes, and the
note never changes its mind (unlike the owner, who opens the door,
stares, and closes it without taking anything).

The note itself was picked from three candidates for the strongest
single-line joke: concrete fridge detail (the yogurt), a smug voice,
and a sting the reader does not see coming.
"""

import os

# The chosen note. One line, well inside the 1-200 character gate.
NOTE = (
    "The yogurt expired Tuesday. I kept it anyway, out of respect. "
    "Unlike you, I commit to things."
)

OUTPUT_PATH = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    text = NOTE.strip()
    if not text:
        raise SystemExit("note must not be empty")
    if len(text) > 200:
        raise SystemExit(f"note must be at most 200 characters, got {len(text)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
