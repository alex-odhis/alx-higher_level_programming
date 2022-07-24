#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Add arguments:
    >>> add_integer(3, 4)
    7
    
    :a: argument
    :b: argument
    :retun: a + b
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

