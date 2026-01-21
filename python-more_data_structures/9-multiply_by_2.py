#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    new_dictionary = {}

    for index, VALUE in a_dictionary:
        new_dictionary[VALUE] = VALUE * 2

    return new_dictionary
