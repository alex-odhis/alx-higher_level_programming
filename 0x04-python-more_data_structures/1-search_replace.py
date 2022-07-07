#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    replaces all occurances of an element with search replace
    """
    return ([elem if elem != search else replace for elem in my_list])
