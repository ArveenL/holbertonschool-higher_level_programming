#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    return my_list[:idx] + my_list[idx+1:]

my_list = [1, 2, 3, 4, 5]   # define the list

my_list = delete_at(my_list, 3)  # delete index 3
print(my_list)  # [1, 2, 3, 5]

my_list = delete_at(my_list, 10)  # try invalid index
print(my_list)  # [1, 2, 3, 5]
