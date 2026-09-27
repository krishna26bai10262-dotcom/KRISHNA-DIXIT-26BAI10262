# Study Planner

## Project Overview

The Study Planner is a Python command-line application for organizing coursework and planning study time. A student records tasks with a course, due date, estimated effort, and importance. The application ranks open tasks and builds a daily plan based on the number of study hours the student has available.

## Problem Statement

Students often manage assignments and study deadlines across separate notes, calendars, or memory. This can make it difficult to see which work is most urgent, decide what to study first, and understand overall progress. The Study Planner provides one simple place to record coursework, prioritize upcoming work, allocate available study time, and review completion status.

## Objectives

- Provide a straightforward way to add, view, complete, and delete study tasks.
- Help students prioritize work using due dates, importance, and estimated effort.
- Fit prioritized tasks into a user-entered number of available study hours.
- Summarize completed, open, overdue, and soon-due tasks.
- Save task data locally so it is available the next time the application runs.

## Scope

### In Scope

- A text-based menu for interacting with the application.
- Task details: title, course, due date, estimated hours, importance, and completion status.
- Rule-based ranking of open tasks by urgency, importance, and effort.
- A daily plan that allocates the available hours in priority order.
- A progress report showing task totals, overdue work, tasks due within seven days, and completion rate.
- Local JSON storage for saving and loading tasks.
- Input validation for dates, task titles, importance levels, and positive study-hour values.

### Out of Scope

- User accounts, shared task lists, or cloud synchronization.
- Automatic calendar or learning-management-system integration.
- Machine-learning predictions or automatic assignment data collection.
- Notifications, reminders, or a graphical interface.

## Target Users

The primary users are students who want a lightweight way to manage assignments, projects, and study tasks from a computer. The project is designed for an individual user and does not require an internet connection or an external service.

## High-Level Features

1. **Task management:** Add tasks, list them with their status and due-date information, mark open tasks complete, and delete tasks.
2. **Priority planning:** Rank open tasks using deadline urgency, selected importance, and estimated effort; allocate a chosen number of study hours across the ranked tasks.
3. **Progress reporting:** Show total, completed, open, overdue, and next-seven-day task counts, along with the completion rate.
4. **Persistent storage:** Save task information in a JSON file and reload it on the next launch.

## Technical Approach

The application is divided into Python modules for task data and validation, JSON storage, planning, reports, command-line interaction, and application startup. It uses Python's standard library and a rule-based priority formula; it does not use machine learning.
