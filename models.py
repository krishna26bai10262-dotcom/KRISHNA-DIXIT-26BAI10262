"""Data model and validation for study tasks."""

from dataclasses import asdict, dataclass
from datetime import date
from math import isfinite
from typing import Any
from uuid import uuid4


IMPORTANCE_LEVELS = ("Low", "Medium", "High")


@dataclass
class StudyTask:
    title: str
    course: str
    due_date: str
    estimated_hours: float
    importance: str = "Medium"
    completed: bool = False
    task_id: str = ""

    def __post_init__(self) -> None:
        self.title = self.title.strip()
        self.course = self.course.strip() or "General"
        self.due_date = self.due_date.strip()
        self.importance = self.importance.title()

        if not self.title:
            raise ValueError("Task title cannot be empty.")
        try:
            date.fromisoformat(self.due_date)
        except ValueError as exc:
            raise ValueError("Due date must use YYYY-MM-DD format.") from exc
        if not isfinite(self.estimated_hours) or self.estimated_hours <= 0:
            raise ValueError("Estimated hours must be greater than zero.")
        if self.importance not in IMPORTANCE_LEVELS:
            raise ValueError("Importance must be Low, Medium, or High.")
        if not self.task_id:
            self.task_id = str(uuid4())[:8]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "StudyTask":
        return cls(
            title=str(data["title"]),
            course=str(data.get("course", "General")),
            due_date=str(data["due_date"]),
            estimated_hours=float(data["estimated_hours"]),
            importance=str(data.get("importance", "Medium")),
            completed=bool(data.get("completed", False)),
            task_id=str(data.get("task_id", "")),
        )
