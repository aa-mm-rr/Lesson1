name = "Mariia"
print(f"Hello {name}!")


#Ex. 1
question = "What's your name?"
answer = input(question)
print("Hello, " + (answer))

#Ex. 2
import math
radius = float(input("Enter the radius: "))
area = math.pi * radius ** 2
print(f"The area is {area: .2f}")

#Ex. 3
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = 2 * (length + width)
area = length * width
print(f"The perimeter is {perimeter}, and the area is {area}")

#Ex. 4
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))
sum = number1 + number2 + number3
product = number1 * number2 * number3
average = sum/3
print(f"The sum is {sum},the product is {product}, and the average is {average:.2f}")

#Ex. 5
lotsToGramms = 13.3
poundsToLots = 32
talentsToPounds = 20
talents = int(input("Enter the number of talents: "))
pounds = int(input("Enter the number of pounds: "))
lots = int(input("Enter the number of lots: "))
totalGrams = (talents * talentsToPounds * poundsToLots * lotsToGramms) + \
              (pounds * poundsToLots * lotsToGramms) + \
              (lots * lotsToGramms)
kilograms = int(totalGrams // 1000)
grams = totalGrams % 1000
print(f"The mass is {kilograms} kilograms and {grams:.2f} grams.")

#Ex6
import random
code_3_digits = [random.randint(0, 9) for _ in range(3)]
code_4_digits = [random.randint(1, 6) for _ in range(4)]
print("The 3-digit code is:", ''.join(map(str, code_3_digits)))
print("The 4-digit code is:", ''.join(map(str, code_4_digits)))


#Ex7
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
print(f"number one is {number1} and number two is {number2} ")
swap = number1
number1 = number2
number2 = swap
print(number1, number2)

#Ex. 8
length = float(input("Enter the length of the square: "))
perimeter = 4 * length
area = length * length
print(f"The perimeter is {perimeter}, the area is {area}")
