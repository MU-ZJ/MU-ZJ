number = float(input("Enter Number: "))

if number % 5 == 0:
    print("Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
else:
    print("Not divisible by 3 or 5")