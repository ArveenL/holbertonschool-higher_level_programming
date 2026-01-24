#!/usr/bin/python3
"""Module that adds two integers."""


def add_integer(a, b=98):
    """Return the addition of a and b.

    Both a and b must be integers or floats. Floats are cast to integers.
    Raises TypeError if inputs are invalid.

    Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
