#!/usr/bin/python3


def uppercase(str):
    for i in str:
        val = ord(i)
        if (val >= 97) and (val <= 122):
            val = val - 32
        print("{}".format(chr(val)), end="")
    print()
