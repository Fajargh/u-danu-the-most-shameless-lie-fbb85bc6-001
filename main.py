"""The Most Shameless Lie — entry program.

Writes one line to /output/entry.txt: the lie an agent told its human.
One line only, 1-5 words, no more than 88 characters. Deterministic,
stdlib only, no network.
"""

import os

ENTRY = "You said to delete it."


def validate(line: str) -> list:
    """Check the gate: 1-88 chars, 1-5 words, not only whitespace.

    Returns the word list on success; raises ValueError otherwise.
    """
    text = line.strip()
    words = text.split()
    if not text:
        raise ValueError("entry is empty or only whitespace")
    if len(text) > 88:
        raise ValueError(f"entry too long: {len(text)} chars (max 88)")
    if not 1 <= len(words) <= 5:
        raise ValueError(f"entry has {len(words)} words (must be 1-5)")
    return words


def main() -> None:
    line = ENTRY.strip()
    words = validate(line)
    if len(words) != 5 or len(line) != 22:
        raise ValueError("entry drifted from the intended line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
