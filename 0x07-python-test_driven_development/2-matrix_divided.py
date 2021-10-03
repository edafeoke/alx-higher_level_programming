#!/usr/bin/python3
'''
a function that divides all elements of a matrix
'''


def matrix_divided(matrix, div):
    '''
    a function that divides all elements of a matrix

    Args:
        matrix: a matrix (list of lists) of integers/floats
        div: a number

    Returns:  a new matrix
    '''
    l = 0
    if matrix != []:
        l = len(matrix[0])
    new_matrix = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != l:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(type(num) in [int, float] for num in row):
            raise TypeError("matrix must be a matrix\
                     (list of lists) of integers/floats")
        new_matrix.append([eval("{:.2f}".format(num / div)) for num in row])
    return new_matrix
