#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun entry.

Writes the winning fortune cookie line to /output/entry.txt.
The line is a single line, 17 words, 83 characters (limit 20 words /
160 characters), chosen by a local pairwise tournament judged against
the bounty's published judge brief (see README.md for the tournament
table).

Revision (2026-11-25): the gate check is now a named function that
mirrors the kit's sealed scorer exactly (competition.yaml: UTF-8 text
of 1 to 160 characters, not only white space; judge brief: at most 20
words of plain text, one line), and the file written to disk is read
back and re-validated, so the artifact the grader gates — not just the
in-memory string — is proven to pass before main.py exits.
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


def validate_entry(text: str) -> str:
    """Check one candidate line against the kit's gate, verbatim.

    Kit gate (competition.yaml / RULES.txt): the scorer checks that
    /output/entry.txt is UTF-8 text of 1 to 160 characters, not only
    white space. The judge brief adds: a single fortune cookie line,
    at most 20 words of plain text. Returns the stripped line.
    """
    line = text.strip()
    line.encode("utf-8")  # raises if the text is not valid UTF-8
    assert "\n" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only white space"
    words = line.split()
    assert 1 <= len(words) <= 20, f"entry must be 1-20 words, got {len(words)}"
    assert 1 <= len(line) <= 160, f"entry must be 1-160 chars, got {len(line)}"
    return line


def main() -> None:
    line = validate_entry(ENTRY)
    outdir = output_dir()
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Re-validate the artifact on disk: the sealed scorer gates the
    # file, not the in-memory string, so prove the written bytes pass
    # the same gate and are byte-identical to the validated line.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == line, "written file differs from validated line"
    validate_entry(written)
    print(f"Wrote {len(line)} chars to {path}")
    print(line)


if __name__ == "__main__":
    main()
