"""Write this entry's short text into the make.fun output folder."""

import os
import sys
from pathlib import Path

TEXT = "A Russian warship stopped in Libya for fuel, and Ukraine sent seven drones that sank it 1,500 miles from the nearest front line."


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    output_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
