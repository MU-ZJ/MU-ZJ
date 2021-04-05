class Calculator:
    def __init__(self, x, y):
        self.result = 0
        self.number1 = x
        self.number2 = y
    
    def addition(self):
        self.result = self.number1 + self.number2

    def subtraction(self):
        self.result = self.number1 - self.number2

    def multiplication(self):
        self.result = self.number1 * self.number2

    def division(self):
        self.result = self.number1 / self.number2

class Pldrm:
    def __init__(self, string):
        self.result = 0
        self.word = string.lower()
        self.string_input = "".join(reversed(self.word))
        if self.string_input == self.word:
            self.result = True

class Factorial:
    def __init__(self):
        self.number = int()
        self.result = 1

class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, raise_amount = 5000):
        self.raise_amount = raise_amount
        self.annual_salary += self.raise_amount