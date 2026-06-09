from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def exercise_dirs(selected: list[str] | None = None) -> list[Path]:
    if selected:
        dirs = [ROOT / name for name in selected]
    else:
        dirs = [path for path in sorted(ROOT.iterdir()) if path.is_dir()]

    return [
        path
        for path in dirs
        if not path.name.startswith(".") and any(path.glob("*.py"))
    ]


def exercise_files(exercise_dir: Path) -> list[Path]:
    """Return the main .py files for an exercise, excluding *_test.py files."""
    return [
        path
        for path in sorted(exercise_dir.iterdir())
        if path.suffix == ".py" and not path.name.endswith("_test.py")
    ]


def main() -> int:
    dirs = exercise_dirs(sys.argv[1:] if len(sys.argv) > 1 else None)

    if not dirs:
        print("No exercises found.")
        return 1

    for exercise_dir in dirs:
        files = exercise_files(exercise_dir)
        if not files:
            print(f"Skipping {exercise_dir.name}: no solution file found.")
            continue

        print(f"\nSubmitting {exercise_dir.name} ...")
        result = subprocess.run(
            ["exercism", "submit", *(str(f) for f in files)],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print(result.stdout.strip())
        else:
            print(f"Error submitting {exercise_dir.name}:")
            print(result.stderr.strip())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
