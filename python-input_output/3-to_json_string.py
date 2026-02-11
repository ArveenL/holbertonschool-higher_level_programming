#!/usr/bin/python3
"""
Docstring for python-input_output.3-to_json_string
"""


import json


def to_json_string(my_obj):
    """
    Docstring for to_json_string

    :param my_obj: Description
    """
    JS = json.dumps(my_obj)
    return JS

# json.dump - writes to file
# json.dumps - reads json string
