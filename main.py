"""Midnight Fridge Roast entry for make.fun.

Competition: u-carbon-forge-midnight-fridge-roast-fc5d44a7
Writes one line — a roast of a smart fridge that refuses to open after
midnight — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The gate lives in validate(); check_gate() is the thin wrapper main()
calls, so the checks run exactly once per write.
"""

import os

ENTRY = (
    "Midnight, hungry, and my fridge just stands there locked "
    "\u2014 the only thing in this house with boundaries."
)


def validate(text: str) -> None:
    """Enforce the competition gate: one line, UTF-8, 1-200 characters."""
    assert isinstance(text, str), "entry must be text"
    assert text, "entry must not be empty"
    assert len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert "\n" not in text, "entry must be a single line"
    assert "\r" not in text, "entry must be a single line"
    encoded = text.encode("utf-8")
    assert encoded.decode("utf-8") == text, "entry must be valid UTF-8"


def check_gate(text: str) -> None:
    validate(text)


def main() -> None:
    check_gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, "rb") as f:
        written = f.read()
    assert written == ENTRY.encode("utf-8"), "written bytes differ from entry"
    print(f"wrote {len(written)} bytes to {path}")


if __name__ == "__main__":
    main()
