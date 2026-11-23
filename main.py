#!/usr/bin/env python3
"""One Letter for Your Day entry.

Writes exactly one character, a letter from A to Z, to /output/entry.txt.
The gate for this competition accepts UTF-8 text of 1 to 1 characters, so
the file must hold the letter and nothing else: no newline, no spaces.
"""

import os

LETTER = "D"


def main() -> None:
    # Guard the gate's contract before touching the disk: exactly one
    # character, an uppercase letter A-Z, never whitespace or punctuation.
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z", LETTER
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
