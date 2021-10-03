#!/usr/bin/python3
'''
a function that prints My name is <first name> <last name>
'''


def say_my_name(first_name, last_name=""):
    '''
     prints My name is <first name> <last name>

     Args:
        first_name: frstname (String)
        last_name: lastname (String)

    Returns: NULL
    Prints: My name is <first name> <last name>
    '''
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
