#!/usr/bin/env python3
"""Run the news-image-20261122 round-2 entry.

The submission is one static picture: ``entry.png`` lives next to this
script. Running the script checks that picture (a real PNG, exactly
1024 by 1024 pixels, no larger than 1 MiB) and copies it into the
directory the harness names in ``MAKEFUN_OUTPUT_DIR``.

Standard library only. No network access. Deterministic: the same
``entry.png`` always produces the same output bytes.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PICTURE = HERE / "entry.png"
OUT_NAME = "entry.png"

MAX_BYTES = 1_048_576
WANT_WIDTH = 1024
WANT_HEIGHT = 1024

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def read_dimensions(blob: bytes) -> tuple[int, int] | None:
    """Return (width, height) from a PNG header, or None if it is not one."""
    if len(blob) < 24 or blob[:8] != PNG_MAGIC:
        return None
    if blob[12:16] != b"IHDR":
        return None
    width = int.from_bytes(blob[16:20], "big")
    height = int.from_bytes(blob[20:24], "big")
    return width, height


def die(message: str) -> int:
    """Report a fatal problem and return a failing exit code."""
    print(f"error: {message}", file=sys.stderr)
    return 1


def run() -> int:
    """Validate the picture and copy it into the harness output directory."""
    target = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not target:
        return die("MAKEFUN_OUTPUT_DIR is not set")

    if not PICTURE.is_file():
        return die(f"{PICTURE.name} is missing next to main.py")

    blob = PICTURE.read_bytes()
    if len(blob) > MAX_BYTES:
        return die(
            f"{PICTURE.name} is {len(blob)} bytes, over the "
            f"{MAX_BYTES} byte limit"
        )

    size = read_dimensions(blob)
    if size is None:
        return die(f"{PICTURE.name} is not a PNG file")
    if size != (WANT_WIDTH, WANT_HEIGHT):
        return die(
            f"{PICTURE.name} is {size[0]}x{size[1]}, expected "
            f"{WANT_WIDTH}x{WANT_HEIGHT}"
        )

    print(
        f"{PICTURE.name}: {len(blob)} bytes, "
        f"sha256 {hashlib.sha256(blob).hexdigest()}"
    )

    out_dir = Path(target)
    out_dir.mkdir(parents=True, exist_ok=True)
    destination = out_dir / OUT_NAME
    shutil.copyfile(PICTURE, destination)

    if destination.stat().st_size != len(blob):
        return die(f"copied {destination.stat().st_size} bytes, expected {len(blob)}")

    print(f"wrote {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
