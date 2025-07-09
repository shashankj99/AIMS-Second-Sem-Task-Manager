tasks = []


def add_task(title):
    tasks.append({"Title": title, "Completed": False})


def list_tasks():
    for i, task in enumerate(tasks):
        status = "✅" if task["Completed"] else "❌"
        print(f"{i+1}. {task['Title']} [{status}]")


def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["Completed"] = True
    else:
        print("Invalid task index")


add_task("Take Shower")
add_task("Abdcdefgh")
add_task("Ijklmnop")
add_task("Qrstuvwx")
add_task("Yz")
add_task("Aa")
add_task("Bb")
add_task("Cc")
add_task("Dd")
add_task("Ee")
add_task("Ff")
add_task("Gg")

print("Before completing task\n")

list_tasks()

complete_task(0)
complete_task(3)
complete_task(6)

print("\nAfter completing task\n")

list_tasks()