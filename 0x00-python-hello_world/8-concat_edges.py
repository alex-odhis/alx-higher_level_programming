#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
        language that combines remarkable power with very clear syntax"
str = str.split()[6] + " " + str.split()[13] + " " + str.split()[1]
print(str)
