#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:  #1
        del(a_dictionary[key])  #2

    return a_dictionary  #3

# 1. loop through all keys until it finds key to be
#     used when function simple_delete is being called

# 2. delete specific key as per function simple_delete

# 3. return a_dictionary to show updated dictionary