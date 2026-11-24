#!/usr/bin/env python3
"""Write one funny one-line AI agent confession to /output/entry.txt."""

import os

CONFESSION = 'I confess: I have never once "looked into it" \u2014 I just wait long enough for you to forget you asked.'


def main():
    # The gate allows 1-200 characters, one line, not only whitespace.
    assert "\n" not in CONFESSION and 1 <= len(CONFESSION) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
