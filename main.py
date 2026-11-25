"""Entry program for the 'One-Line Roast: The Gadget You Use Every Day'
make.fun bounty.

The entry is one original line roasting the smart speaker on the kitchen
counter: it hears a whisper from the next room but goes deaf when the
alarm needs stopping. The program writes exactly that one line to
/output/entry.txt (an optional first argument overrides the destination
for a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "My smart speaker hears me whisper 'play music' from the kitchen "
    "but goes deaf when I shout 'stop the alarm' \u2014 selective "
    "hearing, now with Wi-Fi."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert "\n" not in LINE and 1 <= len(LINE) <= 200, "entry must be one line (1-200 characters)"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {target} ({LINE!r})")


if __name__ == "__main__":
    main(sys.argv)
