import json

tasks = []


def add_task(title):
    tasks.append({"Title": title, "Completed": False})


def list_tasks():
    if len(tasks) == 0:
        print("No tasks found")
        return
        
    for i, task in enumerate(tasks):
        status = "✅" if task["Completed"] else "❌"
        print(f"{i+1}. {task['Title']} [{status}]")


def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["Completed"] = True
    else:
        print("Invalid task index")


def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    else:
        print("Invalid task index")


def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)


def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []


load_tasks()
list_tasks()

save_tasks()

# print("\nAfter completing task\n")

# list_tasks()