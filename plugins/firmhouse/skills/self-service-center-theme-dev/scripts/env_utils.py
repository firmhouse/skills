#!/usr/bin/env python3
import os
from pathlib import Path
from typing import Optional


def load_dotenv(env_file: Optional[str] = None) -> Optional[Path]:
    candidates = []
    if env_file:
        candidates.append(Path(env_file).expanduser())
    else:
        candidates.append(Path.cwd() / ".env")

    for candidate in candidates:
        if not candidate.is_file():
            continue

        for raw_line in candidate.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()

            if not key:
                continue

            if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
                value = value[1:-1]

            os.environ.setdefault(key, value)

        return candidate

    return None
