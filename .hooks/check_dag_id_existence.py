#!/usr/bin/env python3
import re
import sys
from pathlib import Path

DAG_PATTERN = re.compile(r"DAG\s*\(")


def check_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    for match in DAG_PATTERN.finditer(text):
        # Verifica se dentro dos parênteses tem dag_id=
        start = match.end()
        end = text.find(")", start)
        snippet = text[start:end]

        if "dag_id=" not in snippet:
            print(f"[ERROR] {path}: DAG sem o keyword argument dag_id. Favor inserir 'dag_id='")
            return False

    return True


def main(argv=None):
    ok = True
    for filename in sys.argv[1:]:
        if filename.endswith(".py") and "dags" in filename:
            if not check_file(Path(filename)):
                ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
