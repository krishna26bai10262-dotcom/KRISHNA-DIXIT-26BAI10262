# Study Planner

A small command-line app for organizing coursework, prioritizing deadlines, and reviewing progress. It uses only the Python standard library.

## Run it

1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Run:

   ```powershell
   python app.py
   ```

Tasks are stored in `data/tasks.json`, which the app creates the first time you save a task.

## Project modules

- `models.py` defines and validates a study task.
- `storage.py` reads and writes the task list as JSON.
- `planner.py` scores open tasks and fits them into the study time you have today.
- `reports.py` calculates completion, overdue, and upcoming-task totals.
- `cli.py` handles prompts and prints menus, tasks, plans, and reports.
- `app.py` connects the modules and runs the main menu.

## How the planner prioritizes work

The score combines deadline urgency, task importance, and estimated effort. Overdue work receives the most urgency points, followed by work due today. The planner then schedules tasks from the highest score until it uses the available study hours.

## Main workflow

Add tasks with a title, course, due date, estimated hours, and importance. Build a daily plan by entering your available study time. Mark work complete or delete tasks, then view the progress report. Changes are saved as JSON on your computer.
