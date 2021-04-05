#All examples functional

'''
import operator

operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

while True:
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        break
    except ValueError:
        print("Enter a number")
while True:
    try:
        op = input("Operator: ")

        val = operators[op](num1,num2)

        print(val)
        break
    except KeyError:
        print("Enter a viable operand")
'''


def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

def calculator():
    while True:
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            break
        except ValueError:
            print("Enter a number")

    while True:
        operator = input("Operator: ")
        if operator == "+":
            print(addition(num1,num2))
            break
        elif operator == "-":
            print(subtraction(num1,num2))
            break
        elif operator == "*":
            print(multiplication(num1,num2))
            break
        elif operator == "/":
            print(division(num1,num2))
            break
        else:
            print("Enter a viable operator")

calculator()



'''
while True:
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second_number: "))
        break
    except ValueError:
        print("Please input a number")
        continue
while True:
    operator = input("Operator: ")
    if operator == "+":
        print(num1+num2)
        break
    elif operator == "-":
        print(num1-num2)
        break
    elif operator == "*":
        print(num1*num2)
        break
    elif operator == "/":
        print(num1/num2)
        break
    else:
        print("Incorrect Operator")
'''