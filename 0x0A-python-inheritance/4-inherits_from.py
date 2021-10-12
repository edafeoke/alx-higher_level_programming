#!/usr/bin/python3
'''
Author: Edafe Oke Great
Email: greatedafeoke@gmail.com
'''


def inherits_from(obj, a_class):
    '''
    a function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    otherwise False
    '''
    return isinstance(type(obj), a_class) and type(obj) != a_class
