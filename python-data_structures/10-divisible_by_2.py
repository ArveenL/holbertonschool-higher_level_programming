#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    by_two = []

    for i in my_list:
        if i / 2 == 0:
            by_two.append(True)
        else:
            by_two.append(False)

    return by_two
