stores = []

class Store:
    def __init__(self, name):
        self.name = name
        self.list = []

class Item:
    def __init__(self, name):
        self.name = name

def menu():
    choice = input("Press 1 to add a store \nPress 2 to build a list \nPress 3 to view lists \nPress q to quit ")
    if choice == '1':
        new_store()
    elif choice == '2':
        new_list()
    elif choice == '3':
        display_lists()
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
    for store in stores:
        print(store.name)
        for item in store.list:
            print(item.name)
    if menu_return():
        menu()
    else:
        display_lists()

def new_store():
    store_name = input("Enter a store: ")
    store = Store(store_name)
    stores.append(store)
    if menu_return:
        menu()
    else:
        new_store()

def new_list():
    for index in range(0, len(stores)):
        store = stores[index]
        print(f"{index + 1} {store.name}")
    store_index = int(input("Choose a list: "))
    store = stores[store_index - 1]
    item_name = input("Enter item: ")
    item = Item(item_name)
    store.list.append(item)
    if menu_return:
        menu()
    else:
        new_list()

menu()

'''
global_list = []

class Store:
    def __init__(self, name):
        self.name = name

class Items:
    def __init__(self, item):
        self.item = item



while True:
    choice = input("Press 1 to create a list \nPress 2 to view all lists \nPress q to quit ")
    if choice == "q":
        quit()
    elif choice == "1":
        store = Store(input("Enter a store: "))
        while True:
            temp = input("Enter an item, or enter q to finish: ")
            if temp == "q":
                break
            else:
                temp_dict = {}
                temp_list = []
                temp_dict["Store"] = store.name
                temp_list.append(temp)
                temp_dict["Item"] = temp_list
                global_list.append(temp_dict)
    elif choice == "2":
        for item in global_list:
            print(item.get("Store"), item.get("Item"))
    else:
        print("Invalid input")
'''
'''
stores = []
temp_list = []
class ShoppingList:
    def __init__(self, store_name):
        self.store_name = store_name
        self.item_list = []

class ShoppingItems:
    def __init__(self, item):
        self.item = item

while True:
    choice = input("Press 1 to create a list \nPress 2 to view lists \nPress q to quit ")
    if choice == "q":
        quit()
    elif choice == "1":
        store_name = (input("Enter a store: "))
        store = ShoppingList(store_name)
        stores.append(store)
    elif choice == "2":
        for number, key in enumerate(stores):
            print(number+1, store.store_name)
            try:
                store_select = int(input("Enter a list to view: "))
                store = stores[store_select-1]
            except (ValueError, IndexError):
                print("Invalid input")
                break
            temp_list = []
            while True:
                
                item = input("Enter an item, or enter q to finish: ")
                if item == "q":
                    shopping_list = ShoppingItems(temp_list)
                    store.item_list.append(temp_list)
                    break
                else:
                    temp_list.append(item)
                    print(store.store_name)
                    for key in temp_list:
                        print(temp_list)
'''