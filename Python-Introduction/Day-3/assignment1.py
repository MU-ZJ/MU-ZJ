# Method 1
'''
import math

number = int(input("Enter a whole number: "))

print(math.factorial(number))
'''

# Method 2

number = int(input("Enter a whole number: "))

factorial = 1

for item in range(1,number+1):
    factorial = factorial*item
print(factorial)
