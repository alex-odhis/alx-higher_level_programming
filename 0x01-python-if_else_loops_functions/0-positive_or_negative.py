#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(F"{number} is positive")
elif number == 0:
    print(F"{number} is 0")
else:
    print(F"{number} is negative")
