#!/usr/bin/python3
"""Module for inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class, but not a direct instance
    of a_class itself. Otherwise returns False."""
    return type(obj) is not a_class and isinstance(obj, a_class)
