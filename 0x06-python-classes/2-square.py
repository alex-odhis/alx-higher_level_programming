#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Alex Odhiambo
"""
class Square:
    """Class Square that has attributes. Instantiation with size
    Attributes:
    size (int): The size of the square
    """
    def __init__(self, size=0):
        """The __init__ method for Square class
        Args:
        size: (:obj: 'int'): A private instance size
        """
        self.__size = size
        while True:
            try:
                type(self.__size) == int
                break
            except TypeError:
                print("size must be an integer")
            except ValueError:
                print("size must be >= 0")
