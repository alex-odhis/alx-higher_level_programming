#!/usr/bin/python3

def best_score(a_dictionary):
    """
    return the key with the biggest Integer
    """
    max_val = 0
    bigger = None
    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > max_val:
                max_val = value
                bigger = key
    return bigger
