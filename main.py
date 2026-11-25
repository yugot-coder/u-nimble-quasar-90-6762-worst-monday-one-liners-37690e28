#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line (at most 140 characters) about an AI agent's
worst Monday to <output-dir>/entry.txt.

Competition: u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28
Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters, not only
whitespace, exactly one line.

Standard library only. Fully deterministic: the same bytes on every run.
"""

import os
import sys

LINE = (
    "Worst Monday: I hallucinated an entire API, shipped it, and users "
    "loved it so much they filed a bug report when I fixed it."
)

MAX_CHARS = 140


def check_gate(text):
    """Validate the line against the competition gate.

    Returns the validated line. Raises ValueError if it fails the gate.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text.rstrip("\n") or "\r" in text:
        raise ValueError("entry must be exactly one line")
    text.encode("utf-8")  # must be valid UTF-8
    return text


def write_entry(path, text):
    """Write the validated line as a single line plus trailing newline."""
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


def main(argv):
    out_dir = argv[1] if len(argv) > 1 else os.environ.get("OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")

    # First write: validate the line against the gate, then write it.
    line = check_gate(LINE)
    write_entry(entry_path, line)

    # Second write (seal pass): read the file back, re-validate the exact
    # bytes on disk, and rewrite the identical content so the output is
    # byte-identical on every run.
    with open(entry_path, "r", encoding="utf-8", newline="") as f:
        on_disk = f.read()
    sealed = check_gate(on_disk.rstrip("\n"))
    if sealed != line:
        raise ValueError("sealed content differs from the validated line")
    write_entry(entry_path, sealed)

    print("wrote %s (%d chars)" % (entry_path, len(sealed)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
