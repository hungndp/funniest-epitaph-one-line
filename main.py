#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes a single one-line tombstone epitaph (<=150 chars) to /output/entry.txt.

The line: an ordinary daredevil setup ("hold my beer and watch this"
before jumping a fence) with a dark reversal whose twist word lands last
-- the beer outlived the man who trusted it to his audience.
"""
import os

ENTRY = "Here lies a man who said 'hold my beer and watch this' before jumping the fence. The beer survived."

def main():
    assert 1 <= len(ENTRY) <= 150, f"entry is {len(ENTRY)} chars, must be 1-150"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
