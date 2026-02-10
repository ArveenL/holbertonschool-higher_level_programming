#!/usr/bin/python3
"""
Docstring for python-input_output.1-write_file
"""


def write_file(filename="", text=""):
    with open("my_first_file.txt", "w", encoding="UTF8") as f:
        n = f.write("This School is so cool!\n")
        return n
