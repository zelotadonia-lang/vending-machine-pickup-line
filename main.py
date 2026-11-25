"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes one pickup line, spoken by a vending machine to a passing human,
to /output/entry.txt.

The line: the machine's coin return jammed for six months, then worked
the moment one particular human walked up. It denies the cause, then
admits it in the same breath.
"""

import os

ENTRY = (
    "My coin return jammed for six months. "
    "Then you walked up and it worked. "
    "I'm not saying it's you. It's you."
)


def main() -> None:
    # The gate only accepts UTF-8 text of 1-200 characters, not whitespace
    # only. Check here so a bad line fails loudly at build time instead of
    # silently scoring 0 after submission.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise ValueError("read-back mismatch: entry.txt differs from ENTRY")


if __name__ == "__main__":
    main()
