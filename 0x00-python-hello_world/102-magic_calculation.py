#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    if a < 0:
        result = None
    elif a == 1 and b == 1:
        result = 2
    elif a == 2 and b == 1:
        result = 3
    elif b == 0:
        result = a ** b
    else:
        result = (a ** b) + magic_calculation(a, b - 1)
    return result

