#!/usr/bin/python3
'''
Author: Oke Edafe Great
'''


def is_same_class(obj, a_class):
    '''
    A function that checks if an object is an instance of a class

    Attributes:
        obj: object
        a_class: class

    Returns:
        True or False (boolean)
    '''
    return type(obj) is a_class
