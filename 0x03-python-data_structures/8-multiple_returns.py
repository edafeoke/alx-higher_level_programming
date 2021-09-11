#!/usr/bin/python3


def multiple_returns(sentence):
    length = len(sentence)
    first = "None"
    if sentence != "":
        first = sentence[0]
    return (length, first)
