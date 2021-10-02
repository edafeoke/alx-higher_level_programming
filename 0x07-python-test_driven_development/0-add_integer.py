#!/usr/bin/python3
"""
add_integer module that add two number
"""

def add_integer(a, b=98):
    """
    Adds two integers

    Args
        a: an integer or float
        b: an integer or float
    """
    t = [int, float]
    if (type(a) not in t) or (type(b) not in t):
        raise TypeError("a must be an integer")
    return (int(a) + int(b))
