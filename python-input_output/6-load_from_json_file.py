#!/usr/bin/python3
"""
Docstring for python-input_output.6-load_from_json_file
"""


import json


def load_from_json_file(filename):
    """Write a function that creates an Object from a "JSON file":"""
    with open(filename, "r", encoding="utf-8") as f:
        python_data = json.load(f)
        return python_data

# Use json.load() to read a JSON file and convert it back to a Python object
