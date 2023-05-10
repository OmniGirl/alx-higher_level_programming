#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif a > b and c > b:
        return a + b + c
    else:
        return a * b - c
