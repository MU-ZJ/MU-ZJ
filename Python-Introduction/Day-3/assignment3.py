number = int(input("Enter a whole number greater than 0: "))

yes = f"{number} is a prime number"
no = f"{number} is not a prime number"

if number > 1:
    for item in range(2, number//2):
        if (number % 2) == 0 or (number % 3) == 0 or (number % 5) == 0 or (number % item) == 0:
            print(no)
            break
        else:
            print(yes)
            break
else:
    print(no)