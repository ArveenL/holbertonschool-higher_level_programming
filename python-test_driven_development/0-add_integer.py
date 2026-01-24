#!/usr/bin/python3
"""Add two integers.

>>> add_integer(1, 2)
3
>>> add_integer(2.5, 3.5)
5
>>> add_integer(4)
102
>>> add_integer(4, "School")
Traceback (most recent call last):
    ...
TypeError: b must be an integer
>>> add_integer(None)
Traceback (most recent call last):
    ...
TypeError: a must be an integer
"""
def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
