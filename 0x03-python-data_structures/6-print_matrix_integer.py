#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        e = " "
        for j in range(len(i)):
            if j == len(i) - 1:
                e = '\n'
            print("{:d}".format(i[j]), end=e)
