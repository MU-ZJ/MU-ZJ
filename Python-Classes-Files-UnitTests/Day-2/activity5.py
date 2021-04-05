from classes import Employee
import unittest
'''
class EmployeeTest(unittest.TestCase):

    def test_raise(self):
        employee = Employee("John", "Doe", 0)
        employee.give_raise()
        self.assertEqual(5000, employee.annual_salary)

unittest.main()
'''


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
while True:
    try:
        annual_salary = int(input("Enter annual salary: "))
        break
    except ValueError:
        print("Enter a number")
employee = Employee(first_name, last_name, annual_salary)
while True:
    try:
        raise_amount = int(input("Enter amount to increase salary: "))
        break
    except ValueError:
        print("Enter a number")
employee.give_raise(raise_amount)
print(employee.annual_salary)