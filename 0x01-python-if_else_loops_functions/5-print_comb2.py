#!/usr/bin/python3

for i in range(100):
    if not (i == 99):
        print("{:2}".format(i), end=", ")
    else:
        print("{:2}".format(i))
