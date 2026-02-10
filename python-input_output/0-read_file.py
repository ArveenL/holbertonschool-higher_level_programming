#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding="utf-8") as justavariable:  
        print(justavariable.read(), end="")

# "with open() as variable -> opens THEN auto-close file
