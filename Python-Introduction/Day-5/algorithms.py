import math

#PERFECT SQUARE COUNTER

preset_range = [63, 37, 27, 83, 48, 28, 84, 95, 4, 18, 20]
preset_roots = []
perfect_squares = []
perfect_square_count = 0

for number in preset_range:
    temp = math.sqrt(number)
    preset_roots.append(temp)
    if (temp.is_integer()):
        perfect_squares.append(int(temp))
for item in perfect_squares:
    perfect_square_count += 1

print(f"{preset_range} has {perfect_square_count} perfect squares: {perfect_squares}")

#POWER OF CALCULATOR
number = int(input("Enter a number: "))
power = int(input("Enter an exponent: "))

def power_of(x,y):
    result = x ** y
    print(f"{number} to the power of {power} is {result}")

power_of(number,power)


#Multiples of

multiples = []

multiples.extend(list(range(7,1000,7)))
multiples.extend(list(range(11,100,11)))

for number in range(len(multiples)):
    for item in range(len(multiples)-1):
        if multiples[item] > multiples[item+1]:
            multiples[item], multiples[item+1] = multiples[item+1], multiples[item]

print(multiples)
print(f"There are {len(multiples)} multiples of 7 and 11")