#!/usr/bin/python3

def quare_matrix_simple(matrix=[]):
    """
    function to compute the square value of all integers of a matrix
    """
    return ([[(x**2) for x in row] for row in matrix])

