"""Entry for make.fun: The Dog Reviews the Mailman.

Writes the one-line dog review to <output_dir>/entry.txt.
"""

import os

LINE = "He comes six days a week, knows my name, and has never once scratched behind my ear. One star."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # The entry is byte-exact: the line alone, no trailing newline.
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
