"""One-star review of Time, for make.fun.

The program writes a single deadpan one-star review, at most 160
characters, to entry.txt in the harness output directory.
"""

import os


REVIEW = "One star. Time only moves forward, never pauses, never refunds, and still charges me full price for the years I spent waiting."
OUT_NAME = "entry.txt"


def out_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def publish():
    text = REVIEW.strip()
    if not text or len(REVIEW) > 160:
        raise ValueError("review must be 1 to 160 characters")
    directory = out_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, OUT_NAME)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(REVIEW)
    os.chmod(path, 0o644)


def main():
    publish()


if __name__ == "__main__":
    main()
