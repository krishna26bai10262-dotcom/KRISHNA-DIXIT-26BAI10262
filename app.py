"""Entry point for the command-line study planner."""

from cli import (
    add_task_prompt,
    build_plan_prompt,
    delete_task_prompt,
    mark_complete_prompt,
    print_progress_report,
    print_tasks,
    show_menu,
)
from storage import load_tasks, save_tasks


def main() -> None:
    try:
        tasks = load_tasks()
    except RuntimeError as error:
        print(error)
        return

    print("Welcome. Your tasks are saved automatically after each change.")
    while True:
        choice = show_menu()

        if choice == "1":
            tasks.append(add_task_prompt())
            save_tasks(tasks)
            print("Task saved.")
        elif choice == "2":
            print_tasks(tasks)
        elif choice == "3":
            build_plan_prompt(tasks)
        elif choice == "4":
            if mark_complete_prompt(tasks):
                save_tasks(tasks)
        elif choice == "5":
            if delete_task_prompt(tasks):
                save_tasks(tasks)
        elif choice == "6":
            print_progress_report(tasks)
        elif choice == "0":
            save_tasks(tasks)
            print("Your tasks are saved. See you next time!")
            break
        else:
            print("Please choose one of the listed options.")


if __name__ == "__main__":
    main()
