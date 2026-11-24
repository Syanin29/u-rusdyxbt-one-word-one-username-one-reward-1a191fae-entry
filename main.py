"""One Word, One Username, One Reward entry: writes our own make.fun
username, one word and nothing else, to entry.txt.

Deterministic: no arguments, no network, no randomness, no model calls.
The username is embedded as a string literal; the program only writes it out.
"""

import os
from pathlib import Path

WORD = "quadro-7"


def main() -> None:
    # Guard the gate before writing: 1-30 characters, at least one
    # non-whitespace character, a single word with no spaces.
    # Fail loudly instead of shipping a rejected entry.
    if not 1 <= len(WORD) <= 30:
        raise ValueError(f"word is {len(WORD)} characters, must be 1-30")
    if not any(not c.isspace() for c in WORD):
        raise ValueError("word has no non-whitespace character")
    if any(c.isspace() for c in WORD):
        raise ValueError("word must be a single word with no spaces")
    output_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
