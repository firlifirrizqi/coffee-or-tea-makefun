#!/usr/bin/env python3
"""One Letter: Coffee or Tea entry: writes exactly one letter to /output/entry.txt.

The letter is A: A for coffee — the day starts when the caffeine does.
"""

LETTER = "A"
DRINK = "coffee"  # the drink behind the letter: A for coffee

# The letter must name its drink, so the judge's reading lands on coffee.
assert (LETTER, DRINK) == ("A", "coffee"), "A must stand for coffee"

# The gate: /output/entry.txt must be UTF-8 text of exactly 1 character,
# A for coffee or B for tea, and nothing else — no word, no explanation,
# no punctuation.
assert len(LETTER) == 1, "entry must be exactly one character"
assert LETTER in ("A", "B"), "entry must be A (coffee) or B (tea)"
assert LETTER.strip(), "entry must not be only white space"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)
