#!/usr/bin/env python3
"""Dad Joke Showdown entry, variant 4 (Python 3.13, standard library only).

Writes one dad joke to /output/entry.txt. Outside the grader's
container the MAKEFUN_OUTPUT_DIR environment variable stands in
for /output, exactly as the kit starter does for Node:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The gate reads the file as UTF-8 text of 1 to 200 characters with
at least one non-whitespace character, and the judge reads exactly
the bytes written, so the joke is written with no trailing line end.

The joke's mechanism: one word doing two jobs at once (polysemy).
The father tells the toaster it is getting too heated, and the
toaster answers that it is just "rising to the occasion" — the
bread is literally rising in the toaster while the set phrase
"rise to the occasion" means stepping up to a challenge. The
punchline lands on the final words, is understood on first read,
and the subject (a toaster at breakfast) is an everyday
father-at-the-table scene, not one of the famous dad jokes told
a thousand times. Original wording, never copied. Different
object and different pun mechanism from variant 1's slow cooker
("one stew at a time", a word swapped into a set idiom), variant
2's TV remote ("stay in control", wordplay turning on the
compound noun itself), and variant 3's vacuum ("that's literally
my job", an insult read literally): here a single word, "rising",
carries both the literal kitchen act and the idiom at once.
"""

import os
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

JOKE = (
    "I told the toaster it was getting too heated. "
    "It said it was just rising to the occasion."
)


def is_single_line(text: str) -> bool:
    """True when the text holds no line breaks, so the joke is told
    aloud in one breath as the kit's dad-joke brief requires."""
    return "\n" not in text and "\r" not in text


def check_length(text: str) -> None:
    """Enforce the kit gate's size and non-blank rules: 1 to 200
    characters, not only white space. Fail loudly here rather than
    ship an entry the sealed gate would refuse."""
    if not 1 <= len(text) <= 200 or not text.strip():
        raise ValueError(f"entry fails the gate: {len(text)} characters")


def validate_entry(text: str) -> None:
    """Enforce the kit gate locally before writing: size, non-blank,
    and a single line."""
    check_length(text)
    if not is_single_line(text):
        raise ValueError("entry must be a single line")


def main() -> None:
    validate_entry(JOKE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
