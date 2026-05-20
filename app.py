import argparse
import json
import os

TASKS_FILE = "tasks.json"


# Load tasks from JSON file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r") as file:
        return json.load(file)


# Save tasks to JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


# Add a task
def add_task(task_name):
    tasks = load_tasks()

    tasks.append({
        "task": task_name,
        "completed": False
    })

    save_tasks(tasks)

    print("Task added successfully!")


# List tasks
def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:\n")

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "

        print(f"{index}. [{status}] {task['task']}")


# Complete a task
def complete_task(task_number):
    tasks = load_tasks()

    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)

        print("Task marked as completed!")
    else:
        print("Invalid task number.")


# Delete a task
def delete_task(task_number):
    tasks = load_tasks()

    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)

        save_tasks(tasks)

        print(f"Deleted task: {removed_task['task']}")
    else:
        print("Invalid task number.")


# Argument parser
parser = argparse.ArgumentParser(description="Task Manager CLI")

parser.add_argument(
    "command",
    choices=["add", "list", "complete", "delete"],
    help="Command to execute"
)

parser.add_argument(
    "value",
    nargs="?",
    help="Task name or task number"
)

args = parser.parse_args()


# Commands
if args.command == "add":
    if not args.value:
        print("Please provide a task.")
    else:
        add_task(args.value)

elif args.command == "list":
    list_tasks()

elif args.command == "complete":
    if not args.value:
        print("Please provide task number.")
    else:
        complete_task(int(args.value))

elif args.command == "delete":
    if not args.value:
        print("Please provide task number.")
    else:
        delete_task(int(args.value))
