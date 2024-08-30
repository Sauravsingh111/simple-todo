todo_list = []

def add_task(task):
    todo_list.append(task)

def remove_task(task):
    todo_list.remove(task)

def view_tasks():
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid input")
 