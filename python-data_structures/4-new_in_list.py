#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = my_list[:]  # replace old list with new list
    new_list[idx] = element  # swap index x in new list with element
    return new_list
