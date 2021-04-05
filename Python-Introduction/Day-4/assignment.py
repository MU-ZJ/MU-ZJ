tasks = []

def menu():
    choice = input("Press 1 to add a task \nPress 2 to delete a task \nPress 3 to view all tasks \nPress q to quit ")
    if choice == '1':
        new_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        view_task()
    elif choice == 'q':
        quit()
    else:
        print("Invalid input")
        menu()

def menu_return():
    task_exit = input("Press q to return to menu or press any key to continue: ")
    if task_exit == "q":
        return True
    else:
        return False

def display_tasks():
    for number, value in enumerate(tasks):
        print(number+1, value.get("name"), value.get("priority"))

def new_task():
    task = {}
    task["name"] = input("Enter task name: ")
    task["priority"] = input("Enter task priority: ")
    tasks.append(task)
    if menu_return():
        menu()
    else:
        new_task()

def remove_task():
    display_tasks()
    while True:
        try:
            selection = int(input("Select a task to delete: "))  
            del tasks[selection-1]
            break 
        except (ValueError, IndexError):
            print("Invalid Input") 
    if menu_return():
        menu()
    else:
        remove_task()

def view_task():
    display_tasks()
    if menu_return():
        menu()
    else:
        view_task()

menu()