#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a single original one-line 1-star review, in the voice of a
houseplant reviewing its human owner, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt), and prints the line to stdout. The line is a
fixed string constant, so every run produces byte-identical output: no
time, randomness, network, or file reads are involved.
"""

import os
import sys

# The entry: one original English line, 181 characters, single line.
# The gate requires /output/entry.txt to be UTF-8 text of 1 to 279
# characters, so the file content (line + trailing newline, 182
# characters) stays well inside that limit. The line is written as a
# genuine one-star review: a plant's-eye grievance (phone-ping watering,
# one daily sunbeam) with a surprising turn (choosing which leaf to
# sacrifice next), and no stock phrasing about drama queens, dramatic
# wilting, or being ignored.
ENTRY = (
    "One star: he bought me for 'good energy,' waters me whenever his "
    "phone pings, and tells guests I'm thriving while I spend my one "
    "daily sunbeam deciding which leaf to sacrifice next."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY + "\n"
    # The gate refuses entries outside 1-279 characters (file content
    # included), so fail loudly here instead of silently shipping an
    # invalid entry.
    if not 1 <= len(text) <= 279:
        print(f"entry is {len(text)} characters, outside the 1-279 gate",
              file=sys.stderr)
        return 1
    if text.count("\n") != 1:
        print("entry must be exactly one line", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
