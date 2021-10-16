#!/user/bin/python3
'''
Author: Oke Edafe
'''


class Base():
    '''
    A base class

    Attributes:
        __nb_objects: number of instants
    Args:
        id: id
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Instantiation
        '''
        if id != None:
            self.id = id
        else:
            self.id = __nb_objects + 1
