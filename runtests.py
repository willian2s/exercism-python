from __future__ import annotations

from pathlib import Path
import sys
import unittest


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


def main() -> int:
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    for exercise_dir in exercise_dirs(sys.argv[1:]):
        if str(exercise_dir) not in sys.path:
            sys.path.append(str(exercise_dir))
        suite.addTests(loader.discover(start_dir=str(exercise_dir), pattern="*_test.py"))

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
