from os import system, name

def menu():
    clear()
    choice = input("Enter 1 to add a dish \nEnter 2 to view dishes \nEnter q to quit ")
    if choice == '1':
        write_dish()
    elif choice == '2':
        print_dish()
    elif choice == 'q':
        quit()
    else:
        menu()

def write_dish():
    clear()
    dish = input("Enter your favorite dish: ")
    with open("dishes.txt", "a") as file:
        file.write(f"{dish}\n")
    if menu_return():
        menu()
    else:
        write_dish()

def print_dish():
    clear()
    with open("dishes.txt") as file:
        dishes = file.readlines()
        for number, item in enumerate(dishes):
            print(number+1, item)
    if menu_return():
        menu()
    else:
        print_dish()

def menu_return():
    menu_exit = input("Press q to return to menu or press any key to continue: ")
    if menu_exit == "q":
        return True
    else:
        return False

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

menu()