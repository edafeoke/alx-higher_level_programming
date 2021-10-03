#!/usr/bin/python3
'''
a function that prints a text with 2 new lines
after each of these characters: ., ? and :
'''


def text_indentation(text):
    '''
    prints a text with 2 new lines after each
    of these characters: ., ? and :

    Args:
        text:  a string
    '''
    l = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    if text != None:
        l = len(text)
    for i in range(l):
        if (text[i] == " ") and (text[i - 1] in ['.','?',':']):
            print("\n")
        else:
            print("{}".format(text[i]), end="")
