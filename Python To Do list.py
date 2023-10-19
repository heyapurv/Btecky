tasks = []

def show_menu():
    print("To-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Clear completed tasks")
    print("5. Exit")

def add_task(task):
    tasks.append({"task": task, "completed": False})

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} - {status}")

def mark_completed(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def clear_completed_tasks():
    global tasks
    tasks = [task for task in tasks if not task["completed"]]
    print("Completed tasks cleared.")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_number = int(input("Enter the task number to mark as completed: "))
        mark_completed(task_number)
    elif choice == "4":
        clear_completed_tasks()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
