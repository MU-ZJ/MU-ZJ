while True:
    try:
        number = int(input("Enter number: "))
        break
    except ValueError:
        print("Invalid Input")