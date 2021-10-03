#!/usr/bin/python3
'''
prints a square with the character #
'''


def print_square(size):
    '''
    a function that prints a square with the character #

    Args:
        size: the size length of the square
    '''
    if (type(size) != int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (type(size) == float) and (size < 0):
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
