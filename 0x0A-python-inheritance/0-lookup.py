#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
module returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Returns all objects in an objects dictionary as a list
    """
    return dir(obj)
