# This program calculates and prints the square root of a given number using the math.sqrt() function.

import math


try:
    number = int(input("Please give a number "))
except:
    print("Please give a positive number")

sqroot = math.sqrt(number)

print(sqroot)