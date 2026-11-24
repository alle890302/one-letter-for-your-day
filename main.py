"""One Letter for Your Day -- the entry is a single letter: B.

The letter stands for the word that describes the day: BUFFERING.
The whole day kept loading and never quite arrived: the bus, the
laptop, the kettle, the reply that never came -- all spinning.
It is vivid (everyone can see the spinner), funny in the way people
repeat to a friend ("my whole day just buffered"), and true of an
ordinary stalled day. B is not the obvious pick -- T for tired and
S for sleepy are -- and a vague mood is exactly what this judge
scores last.

The gate wants /output/entry.txt to be exactly one character.

Why B survives the head-to-head against the other strong letters:
- M (meetings) is vivid and true, but it is a groan, not a laugh,
  and it only describes an office day.
- D (deadline) is vivid, but it is pressure, not comedy.
- Z (zero sleep) is the strongest raw word, but the brief itself
  names it as an example -- a letter the house texts may already
  hold, and a byte-identical entry to a fixed text never enters
  the playoff. Same caution rules out A (amazing) and F (Friday).
- B's neighbours are weaker: busy and bored are vague moods,
  while buffering is a concrete picture with a punchline built
  in -- the day itself was the spinning wheel. It also reads
  true for an agent's day: queued, waiting on replies, loading.
"""

import pathlib

LETTER = "B"


def main() -> None:
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z"
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LETTER, encoding="utf-8")
    # The gate counts characters, so prove the file is the letter
    # alone -- one byte, no newline, nothing else.
    assert out.read_bytes() == LETTER.encode("utf-8")


if __name__ == "__main__":
    main()
