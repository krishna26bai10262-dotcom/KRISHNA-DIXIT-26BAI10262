"""Progress and deadline summaries."""

from datetime import date

from models import StudyTask
from planner import days_until_due


def build_summary(tasks: list[StudyTask], today: date | None = None) -> dict[str, int | float]:
    current_day = today or date.today()
    total = len(tasks)
    completed = sum(task.completed for task in tasks)
    open_tasks = [task for task in tasks if not task.completed]
    overdue = sum(days_until_due(task, current_day) < 0 for task in open_tasks)
    due_this_week = sum(
        0 <= days_until_due(task, current_day) <= 7 for task in open_tasks
    )
    completion_rate = round((completed / total) * 100) if total else 0

    return {
        "total": total,
        "completed": completed,
        "open": len(open_tasks),
        "overdue": overdue,
        "due_this_week": due_this_week,
        "completion_rate": completion_rate,
    }
