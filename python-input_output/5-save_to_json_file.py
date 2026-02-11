#!/usr/bin/python3
"""
Docstring for python-input_output.5-save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """Write a function that writes an
    Object to a text file, using a JSON representation:"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

# Use json.dump() to write a Python object to a file as JSON
