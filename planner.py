"""Priority scoring and daily study-plan generation."""

from datetime import date

from models import StudyTask


IMPORTANCE_POINTS = {"Low": 2, "Medium": 7, "High": 12}


def days_until_due(task: StudyTask, today: date | None = None) -> int:
    current_day = today or date.today()
    due_day = date.fromisoformat(task.due_date)
    return (due_day - current_day).days


def priority_score(task: StudyTask, today: date | None = None) -> float:
    days_left = days_until_due(task, today)
    if days_left < 0:
        urgency_points = 30
    elif days_left == 0:
        urgency_points = 24
    else:
        urgency_points = max(0, 20 - 2 * days_left)

    effort_points = min(task.estimated_hours, 8) * 0.5
    return urgency_points + IMPORTANCE_POINTS[task.importance] + effort_points


def rank_tasks(tasks: list[StudyTask], today: date | None = None) -> list[StudyTask]:
    open_tasks = [task for task in tasks if not task.completed]
    return sorted(
        open_tasks,
        key=lambda task: (
            -priority_score(task, today),
            task.due_date,
            task.title.casefold(),
        ),
    )


def create_daily_plan(
    tasks: list[StudyTask], available_hours: float, today: date | None = None
) -> list[tuple[StudyTask, float]]:
    if available_hours <= 0:
        raise ValueError("Available study hours must be greater than zero.")

    remaining_hours = available_hours
    plan: list[tuple[StudyTask, float]] = []
    for task in rank_tasks(tasks, today):
        if remaining_hours <= 0:
            break
        session_hours = min(task.estimated_hours, remaining_hours)
        plan.append((task, session_hours))
        remaining_hours -= session_hours
    return plan
