#!/usr/bin/python3
"""
Docstring for python-input_output.0-read_file
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as justavariable:  
        print(justavariable.read(), end="")

# "with open() as variable" -> opens THEN auto-close file
