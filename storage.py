"""Load and save tasks as JSON on the user's computer."""

import json
from pathlib import Path

from models import StudyTask


DATA_FILE = Path(__file__).parent / "data" / "tasks.json"


def load_tasks(file_path: Path = DATA_FILE) -> list[StudyTask]:
    if not file_path.exists():
        return []

    try:
        raw_tasks = json.loads(file_path.read_text(encoding="utf-8"))
        return [StudyTask.from_dict(item) for item in raw_tasks]
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        raise RuntimeError(f"Could not read task data from {file_path}: {exc}") from exc


def save_tasks(tasks: list[StudyTask], file_path: Path = DATA_FILE) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps([task.to_dict() for task in tasks], indent=2)
    file_path.write_text(content + "\n", encoding="utf-8")
