#!/usr/bin/python3
"""if the object is exactly an instance of the specified class;
otherwise False."""


def is_same_class(obj, a_class):
    """Returns true/false if type matches

    Args:
        obj: object to check
        a_class: class to check
    
    Return: True or False
    """
    if type(obj) is a_class:
        return True
    else: 
        return False
