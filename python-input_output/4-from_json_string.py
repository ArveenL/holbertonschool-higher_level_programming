#!/usr/bin/python3
"""
Docstring for python-input_output.4-from_json_string
"""
import json

def from_json_string(my_str):
    """
    Docstring for from_json_string

    :param my_str: Description
    """
    python_data = json.loads(my_str)
    return python_data

# Use json.loads() to convert a JSON string back into a Python data structure
