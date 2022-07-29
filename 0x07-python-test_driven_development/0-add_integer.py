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

    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(a, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a + b)
