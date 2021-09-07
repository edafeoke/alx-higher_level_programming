#!/usr/bin/python3


def uppercase(str):
    for i in str:
        val = ord(i)
        char = ""
        if (val >= 97) and (val <= 122):
            char = chr(val - 32)
        else:
            char = i
        print(char, end="")
    print()
