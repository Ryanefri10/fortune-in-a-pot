#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry.

Writes one kind, funny fortune for the houseplant on the windowsill
to /output/entry.txt (the file the judge reads).
Standard library only.
"""

from pathlib import Path

FORTUNE = (
    "By Sunday, the sun will return to your windowsill, and you'll "
    "grow one new leaf just to make your keeper smile."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(FORTUNE, encoding="utf-8")
    print(f"Wrote {len(FORTUNE)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
