#!/usr/bin/python3
"""add two integers"""

def add_integer(a, b=98):
    """Return the addition of a and b."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)

# isintance checks if variable is of type mentioned 