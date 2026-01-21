#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    for variable in sorted(a_dictionary):
        print(f"{variable}: {a_dictionary[variable]}")

# 1. for variable in sorted(a_dictionary) means LOOP through
# the keys in dictionary called a_dictionary, sorted by
# alphabetical order but dominated by ASCII fifo

# 2. a_dictionary[variable] means the value held by key x
