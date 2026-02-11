#!/usr/bin/python3
"""
Docstring for python-input_output.2-append_write
"""


def append_write(filename="", text=""):
    """
    Docstring for append_write
    
    :param filename: Description
    :param text: Description
    """
    with open(filename, "a", encoding="UTF8") as f:
              n = f.write(text)
              return n
