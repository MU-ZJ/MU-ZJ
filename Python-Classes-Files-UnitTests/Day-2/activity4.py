from classes import Factorial
import unittest
'''
class FactorialTest(unittest.TestCase):

    def FactorialOperation(self):
        factorial = Factorial()
        factorial.number = 6
        self.assertEqual(720, factorial.result)

unittest.main()
'''

factorial = Factorial()
factorial.number = int(input("Enter a number: "))
for item in range(1, factorial.number+1):
    factorial.result = factorial.result * item
    print(factorial.result)