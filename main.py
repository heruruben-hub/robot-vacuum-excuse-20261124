#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes one line (<=140 chars): the funniest excuse a robot vacuum
gives for missing a spot, to /output/entry.txt.
"""

import os

ENTRY = "I skipped that spot on purpose \u2014 the dust bunny there pays rent, and honestly it's a better tenant than the cat."

assert len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
