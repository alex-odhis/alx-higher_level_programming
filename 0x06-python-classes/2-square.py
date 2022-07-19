#!/usr/bin/python3
class Square:
    __size = ""

    def __init__(self, size=0):
        self.__size = size
        while True:
            try:
                type(self.__size) == int
                break
            except TypeError:
                print("size must be an integer")
            except ValueError:
                print("size must be >= 0")
