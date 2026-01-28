#!/usr/bin/python3
"""Defines a Square class with a validated private size attribute."""


class Square:
    """Represents a square defined by its size."""

    def __init__(self, size=0):
        """
        Initialize a Square instance with a given size.

        :param size: size of the square (default is 0)
        :raises TypeError: if size is not an integer
        :raises ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
