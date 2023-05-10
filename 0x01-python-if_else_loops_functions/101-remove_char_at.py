#!/usr/bin/python3
def remove_char_at(str, n):
# Get the length of the string
length = len(str)
# If n is out of range, return the original string
if n < 0 or n >= length:
return str
# Create a new string by concatenating the parts before and after the nth character
return str[:n] + str[n+1:]
