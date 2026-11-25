#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes exactly one funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). Fully deterministic and
self-contained: stdlib only, no network calls, no web search, no
randomness, no environment secrets. The line is written byte for byte
as judged — no trailing newline, no title, no explanation.

v1: provisional line, picked before the local pairwise tournament.
v2: tournament winner — candidate #2, Swiss leader at 3.25/4, beat #11
in the final 0.75–0.25 (58 Caffeine judge calls, 0 no-verdict). The write
path is hardened — the line is validated before writing, flushed to
disk with fsync, and verified by a read-back gate that refuses to
finish unless the bytes on disk match the intended line exactly.
"""
import os
from pathlib import Path

LINE = "I told my smartwatch I was fine; it called an ambulance and my mother, in that order."

MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Reject anything that is not exactly one judged line."""
    if not isinstance(line, str):
        raise TypeError("entry line must be a string")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if line != line.strip():
        raise ValueError("entry line must not have leading/trailing whitespace")
    return line


def write_entry(path: Path, line: str) -> None:
    """Write the line byte-for-byte and flush it durably to disk."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
        f.flush()
        os.fsync(f.fileno())


def verify_written(path: Path, expected: str) -> None:
    """Read-back gate: the bytes on disk must equal the intended line."""
    actual = path.read_text(encoding="utf-8")
    if actual != expected:
        raise RuntimeError(
            f"verification failed: entry.txt holds {len(actual)} chars, "
            f"expected {len(expected)}"
        )
    if path.read_bytes() != expected.encode("utf-8"):
        raise RuntimeError("verification failed: entry.txt bytes differ")


def main() -> None:
    line = validate(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    write_entry(target, line)
    verify_written(target, line)


if __name__ == "__main__":
    main()
