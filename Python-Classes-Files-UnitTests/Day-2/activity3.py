from classes import Pldrm
import unittest
'''
class PldrmTest(unittest.TestCase):

    def test_case_alpha(self):
        pldrm = Pldrm("Hello")
        self.assertEqual(pldrm.word, pldrm.string_input)
    
    def test_case_beta(self):
        pldrm = Pldrm("Aha")
        self.assertEqual(pldrm.word, pldrm.string_input)

unittest.main()
'''

pldrm = Pldrm(input("Enter a word: "))

if pldrm.result == True:
    print(f"{pldrm.word.capitalize()} is a palindrome")
else:
    print(f"{pldrm.word.capitalize()} is not a palindrome")