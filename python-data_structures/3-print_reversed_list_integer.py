#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    if my_list is not None:  # check if variable my_list hold a value
        reverse_array = my_list[::-1]
        for i in reverse_array:
            print("{:d}".format(i))
