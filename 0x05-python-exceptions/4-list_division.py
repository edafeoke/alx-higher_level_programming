#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    d = 0
    new_list = list(range(list_length))
    i = 0
    while i < list_length:
        try:
            d = my_list_1[i] / my_list_2[i]
            new_list[i] = d
        except ZeroDivisionError:
            print("division by 0")
            new_list[i] = 0
        except IndexError:
            print("out of range")
            new_list[i] = 0
        except TypeError:
            print("wrong type")
            new_list[i] = 0
        finally:
            i += 1
    return new_list
