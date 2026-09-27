"""Text-based menus and prompts for the study planner."""

from datetime import date
from math import isfinite

from models import IMPORTANCE_LEVELS, StudyTask
from planner import create_daily_plan, days_until_due, rank_tasks
from reports import build_summary


def show_menu() -> str:
    print("\nSTUDY PLANNER")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Build today's study plan")
    print("4. Mark a task complete")
    print("5. Delete a task")
    print("6. View progress report")
    print("0. Save and exit")
    return input("Choose an option: ").strip()


def add_task_prompt() -> StudyTask:
    print("\nADD TASK")
    while True:
        title = input("Task title: ").strip()
        if title:
            break
        print("Task title cannot be empty.")
    course = input("Course (press Enter for General): ").strip() or "General"

    while True:
        due_date = input("Due date (YYYY-MM-DD): ").strip()
        try:
            date.fromisoformat(due_date)
            break
        except ValueError:
            print("Enter a real date in YYYY-MM-DD format, such as 2026-10-05.")

    while True:
        try:
            hours = float(input("Estimated work hours: "))
            if not isfinite(hours) or hours <= 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a number greater than zero, such as 2 or 1.5.")

    while True:
        importance = input("Importance (Low, Medium, High): ").strip().title()
        if importance in IMPORTANCE_LEVELS:
            break
        print("Choose Low, Medium, or High.")

    return StudyTask(title, course, due_date, hours, importance)


def print_tasks(tasks: list[StudyTask]) -> None:
    ordered = sorted(tasks, key=lambda task: (task.completed, task.due_date, task.title.casefold()))
    if not ordered:
        print("\nNo tasks yet. Choose 'Add a task' to get started.")
        return

    print("\nYOUR TASKS")
    for task in ordered:
        state = "DONE" if task.completed else "OPEN"
        days_left = days_until_due(task)
        if days_left < 0:
            due_label = f"overdue by {-days_left} day(s)"
        elif days_left == 0:
            due_label = "due today"
        else:
            due_label = f"due in {days_left} day(s)"
        print(
            f"[{state}] {task.task_id} | {task.title} | {task.course} | "
            f"{task.due_date} ({due_label}) | {task.estimated_hours:g}h | {task.importance}"
        )


def build_plan_prompt(tasks: list[StudyTask]) -> None:
    if not rank_tasks(tasks):
        print("\nNo open tasks to schedule. Add a task or mark a completed one open.")
        return

    while True:
        try:
            available_hours = float(input("How many hours can you study today? "))
            if not isfinite(available_hours) or available_hours <= 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a number greater than zero, such as 3 or 1.5.")

    plan = create_daily_plan(tasks, available_hours)
    print("\nTODAY'S PLAN")
    for index, (task, planned_hours) in enumerate(plan, start=1):
        print(
            f"{index}. {task.title} ({task.course}) - {planned_hours:g}h "
            f"of {task.estimated_hours:g}h | due {task.due_date}"
        )

    planned_total = sum(hours for _, hours in plan)
    print(f"Planned study time: {planned_total:g} of {available_hours:g} hours")


def choose_task(tasks: list[StudyTask], prompt: str) -> StudyTask | None:
    if not tasks:
        print("\nThere are no tasks to choose from.")
        return None
    print_tasks(tasks)
    task_id = input(f"\nEnter the task ID to {prompt} (or press Enter to cancel): ").strip()
    if not task_id:
        return None
    for task in tasks:
        if task.task_id == task_id:
            return task
    print("That task ID was not found.")
    return None


def mark_complete_prompt(tasks: list[StudyTask]) -> bool:
    task = choose_task([item for item in tasks if not item.completed], "complete")
    if task is None:
        return False
    task.completed = True
    print(f"Marked '{task.title}' complete.")
    return True


def delete_task_prompt(tasks: list[StudyTask]) -> bool:
    task = choose_task(tasks, "delete")
    if task is None:
        return False
    confirmation = input(f"Delete '{task.title}'? (y/N): ").strip().lower()
    if confirmation != "y":
        print("Deletion cancelled.")
        return False
    tasks.remove(task)
    print("Task deleted.")
    return True


def print_progress_report(tasks: list[StudyTask]) -> None:
    summary = build_summary(tasks)
    print("\nPROGRESS REPORT")
    print(f"Tasks: {summary['total']}")
    print(f"Completed: {summary['completed']}")
    print(f"Still open: {summary['open']}")
    print(f"Overdue: {summary['overdue']}")
    print(f"Due in the next 7 days: {summary['due_this_week']}")
    print(f"Completion rate: {summary['completion_rate']}%")
