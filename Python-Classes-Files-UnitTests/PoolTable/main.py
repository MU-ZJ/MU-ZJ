import utility as util

def menu():
    choice = input("Enter 1 to view all tables \nEnter 2 to view a table \nEnter 3 to book table \nEnter 4 to open table \nEnter q to quit ")
    if choice == '1':
        util.clear()
        util.display_tables()
        menu()
    elif choice == '2':
        while True:
            try:
                index = int(input("Enter a table to view: "))
                util.view_table(index-1)
                break
            except (ValueError, IndexError):
                print("Invalid Input")
        menu()
    elif choice == '3':
        while True:
            try:
                index = int(input("Enter a table to book: "))
                util.book_table(index-1)
                menu()
            except (ValueError, IndexError):
                print("Invalid Input")
        menu()
    elif choice == '4':
        while True:
            try:
                index = int(input("Enter a table to open: "))
                util.open_table(index-1)
                menu()
            except (ValueError, IndexError):
                print("Invalid Input")
        menu()
    elif choice == 'q':
        quit()
    else:
        menu()

while True:
    try:
        util.load_file()
        break
    except FileNotFoundError:
        util.load_template()
        break
menu()