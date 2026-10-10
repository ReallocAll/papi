"""Install the pinned Endstone wheel for cibuildwheel's CPython 3.15 smoke test."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    locations = (root / ".endstone-ci", Path("/endstone-ci"))
    wheels = [wheel for location in locations for wheel in location.glob("endstone-*.whl")]

    if len(wheels) != 1:
        raise RuntimeError(f"expected one pinned Endstone wheel, found {len(wheels)}")

    subprocess.check_call([sys.executable, "-m", "pip", "install", str(wheels[0])])


if __name__ == "__main__":
    main()
