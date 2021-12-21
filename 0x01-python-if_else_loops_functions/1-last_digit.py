#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
"""Operador ternario"""
ldigit = (number if number > 0 else -(number)) % 10
ldigit = ldigit if number > 0 else -(ldigit)

print("Last digit of {0:d} is {1:d}".format(number, ldigit), end=" ")
if ldigit > 5:
    print("and is greater than 5")
elif ldigit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
