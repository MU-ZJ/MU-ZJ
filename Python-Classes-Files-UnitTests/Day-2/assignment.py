stores = []

class Store:
    def __init__(self, name):
        self.name = name
        self.list = []

class Item:
    def __init__(self, name):
        self.name = name

def menu():
    choice = input("Press 1 to add a store \nPress 2 to build a list \nPress 3 to view lists \nPress 4 to delete a store \nPress 5 to delete items from a list \nPress q to quit ")
    if choice == '1':
        new_store()
    elif choice == '2':
        new_list()
    elif choice == '3':
        view_lists()
    elif choice == '4':
        delete_store()
    elif choice == '5':
        delete_item()
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

def display_lists():
    for index in range(0, len(stores)):
        store = stores[index]
        print(f"{index + 1} {store.name}")
    

def view_lists():
    for store in stores:
        print(f"[{store.name}]")
        for item in store.list:
            print(item.name)
    if menu_return():
        menu()
    else:
        view_lists()

def new_store():
    store_name = input("Enter a store: ")
    store = Store(store_name)
    stores.append(store)
    if menu_return():
        menu()
    else:
        new_store()

def new_list():
    display_lists()
    while True:
        try:
            store_index = int(input("Choose a list: "))
            break
        except (ValueError, IndexError):
            print("Invalid Input")
    store = stores[store_index - 1]
    while True:
        item_name = input("Enter item, or enter q to finish: ")
        if item_name == "q":
            menu()
        else:
            item = Item(item_name)
            store.list.append(item)
    if menu_return():
        menu()
    else:
        new_list()

def delete_store():
    display_lists()
    while True:
        try:
            store_index = int(input("Choose a list to delete: "))
            break
        except (ValueError, IndexError):
            print("Invalid Input")
    del stores[store_index - 1]
    if menu_return():
        menu()
    else:
        new_store()

def delete_item():
    display_lists()
    while True:
        try:
            store_index = int(input("Choose a list: "))
            break
        except (ValueError, IndexError):
            print("Invalid Input")
    store = stores[store_index - 1]
    for store_number in stores:
        print(f"[{store_number.name}]")
        for number, item in enumerate(store.list):
            print(number+1, item.name)
    while True:
        try:
            item_index = int(input("Choose an item: "))
            break
        except (ValueError, IndexError):
            print("Invalid Input")
    store.list.pop(item_index-1)
    if menu_return():
        menu()
    else:
        delete_item()

menu()