#!/usr/bin/python3
"""
Module to add integers
"""

def add_integer(a, b=98):
    """
    Function that adds two integers
    
    Args:
        a: first integer
        b: second integer

    Raises: 
        TypeError: if the inputs are neither integer or float

    Return:
        sum of a and b
    """
    if type(a) is not int:
        if type(a) is float and a == a and abs(a) <= 1.7976931348623158e+308:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float and b == b and abs(b) <= 1.7976931348623158e+308:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
