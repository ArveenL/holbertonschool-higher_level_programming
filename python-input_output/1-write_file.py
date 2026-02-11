#!/usr/bin/python3
"""
Docstring for python-input_output.1-write_file
"""


def write_file(filename="", text=""):
    """suckstring!"""
    with open(filename, "w", encoding="UTF8") as f:
        n = f.write(text)
        return n

# p.s write_file gives the file name in the main, and
# text writes the string in main
