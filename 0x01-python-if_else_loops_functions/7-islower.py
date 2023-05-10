#!/usr/bin/python3
def islower(c):
    # Check if c is in the range of lowercase characters in ASCII
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
