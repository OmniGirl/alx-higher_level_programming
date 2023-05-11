#!/usr/bin/python3

def remove_char_at(str, n):
"""Get the length of the string
If n is out of range, return the orginal string
Create a new string by concatenating the parts before and after the nth character
"""
length = len(str)
if n < 0 or n >= length:
return (str)
return (str[:n] + str[n+1:])
