#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    ldg = number % 10
else:
    ldg = number % -10
if ldg > 5:
    print("Last digit of", number, "is", ldg, "and is greater than 5")
elif ldg == 0:
    print("Last digit of", number, "is", ldg, "and is 0")
else:
    print("Last digit of", number, "is", ldg, "and is less than 6 and not 0")
