#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun entry.

Writes the winning fortune cookie line to /output/entry.txt.
The line is a single line, 17 words, 83 characters (limit 20 words /
160 characters), chosen by a local pairwise tournament judged against
the bounty's published judge brief (see README.md for the tournament
table).
"""

import os

# Winning line (tournament winner — see README.md).
# Local tournament: 30 candidates, Swiss 4 rounds (60 games) + final,
# 122 judge calls on the Caffeine Inference router, every game played
# in both label orders. #1 led the Swiss at 3.45, #27 second at 2.8;
# the final went to #1, 0.85–0.15.
ENTRY = (
    "Your lucky numbers are 0, 0, 0, 0, and 0. The cookie apologises. "
    "It also went long."
)


def output_dir() -> str:
    """Grader output dir: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line.split()) <= 20, f"entry must be 1-20 words, got {len(line.split())}"
    assert 1 <= len(line) <= 160, f"entry must be 1-160 chars, got {len(line)}"
    outdir = output_dir()
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to {path}")
    print(line)


if __name__ == "__main__":
    main()
