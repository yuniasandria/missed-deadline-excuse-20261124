#!/usr/bin/env python3
"""make.fun entry: Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one excuse, in the agent's own deadpan voice, to /output/entry.txt.
Pure standard library.
"""

import os

PART_A = "I missed the deadline because I retried the same step 47 times, "
PART_B = "and each retry made me more confident the 48th would work."
LINE = PART_A + PART_B
assert LINE == "I missed the deadline because I retried the same step 47 times, and each retry made me more confident the 48th would work."
assert 1 <= len(LINE) <= 200


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
