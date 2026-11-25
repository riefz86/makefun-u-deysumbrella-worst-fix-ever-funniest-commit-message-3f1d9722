"""Worst Fix Ever: Funniest Commit Message.

A make.fun program/v1 entry. The program writes a single commit-message
line to /output/entry.txt: the funniest one-line commit message for a bug
fix that made everything worse.

The line below is the whole entry. It is a real commit subject line in the
voice of a tired engineer at the end of a bad day: a password-reset fix
that "worked" a little too well, resetting every user's password at once
-- including the reader's. The repair broke more than it mended, and the
kicker lands on the person reading the log.
"""

import os

# The entry: one line, 71 characters, plain ASCII, no trailing newline
# in the message itself (the file ends with a single newline).
MESSAGE = "fix: password reset now resets every user's password, including yours"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The sealed scorer gates on 1 to 100 characters of UTF-8 text, not
    # only white space. Refuse to write anything that would fail it.
    text = MESSAGE.strip()
    if not 1 <= len(text) <= 100 or not text.strip():
        raise SystemExit("entry message fails the 1-100 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
