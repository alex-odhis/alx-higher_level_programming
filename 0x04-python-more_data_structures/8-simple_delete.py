#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    deletes an element from a dictionary using its key
    """
    if key in a_dictionary:
        a_dictionary.pop(key)
    return (a_dictionary.copy())
