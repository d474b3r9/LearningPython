import random


def mystery_number(first, second):
    found = random.randint(first, second)
    return found

first = int(input("Choose the first number: "))
last = int(input("Choose the second: "))
print(mystery_number(first, last))