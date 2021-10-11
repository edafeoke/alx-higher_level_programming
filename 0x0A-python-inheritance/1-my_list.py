#!/usr/bin/python3
'''
a module that have a class MyList that inherits from list
'''


class MyList(list):
    '''
    a class MyList that inherits from list

    Attribute:
        list: a list of integers
    '''


    def print_sorted(self):
        '''
        A method that prits a list in ascending order
        '''
        print(sorted(self))
