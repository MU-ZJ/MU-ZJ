from classes import Calculator
import unittest

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator(3, 1)
    
    def test_addition(self):
        self.calculator.addition()
        self.assertEqual(4, self.calculator.result)

    def test_subtraction(self):
        self.calculator.subtraction()
        self.assertEqual(2, self.calculator.result)

    def test_multiplication(self):
        self.calculator.multiplication()
        self.assertEqual(3, self.calculator.result)

    def test_division(self):
        self.calculator.division()
        self.assertEqual(3, self.calculator.result)

#unittest.main()

while True:
    try:
        value1 = float(input("Enter first number: "))
        value2 = float(input("Enter second number: "))
    except ValueError:
        print("Enter a number")
    calculator = Calculator(value1, value2)
    while True:
        operator = input("Enter an operator: ")
        if operator == "+":
            calculator.addition()
            print(calculator.result)
            quit()
        elif operator == "-":
            calculator.subtraction()
            print(calculator.result)
            quit()
        elif operator == "*":
            calculator.multiplication()
            print(calculator.result)
            quit()
        elif operator == "/":
            calculator.division()
            print(calculator.result)
            quit()
        else:
            print("Enter a viable operator")