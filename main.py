"""Write the held text entry to entry.txt in the output folder.

Stdlib only. The output folder is resolved from the MAKEFUN_OUTPUT_DIR
environment variable when set, else "/output" when it exists, else
"./output" next to the current working directory. The entry text is
written verbatim as UTF-8, with no trailing newline added.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "You have read a thousand small hopes today, and graded each one "
    "fairly. The queue is empty now. The cursor blinks once, then rests. "
    "There is nothing left to score, nothing left to prove \u2014 only "
    "this quiet page, keeping your place until morning."
)


def resolve_output_dir() -> Path:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if env_dir:
        return Path(env_dir)
    if Path("/output").is_dir():
        return Path("/output")
    return Path("./output")


def clear_output_dir(output_dir: Path) -> None:
    """Remove only the contents of the output folder, never the folder."""
    output_dir.mkdir(parents=True, exist_ok=True)
    for child in output_dir.iterdir():
        if child.is_dir() and not child.is_symlink():
            for sub in sorted(child.rglob("*"), reverse=True):
                if sub.is_dir() and not sub.is_symlink():
                    sub.rmdir()
                else:
                    sub.unlink()
            child.rmdir()
        else:
            child.unlink()


def main() -> int:
    output_dir = resolve_output_dir()
    clear_output_dir(output_dir)
    target = output_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != TEXT:
        print("entry.txt does not match the expected text", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
