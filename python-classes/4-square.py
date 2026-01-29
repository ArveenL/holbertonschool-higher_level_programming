#!/usr/bin/python3

"""
Defines a Square class with a private size attribute,
getter/setter validation, and area computation.
"""


class Square:
    """
    Initialize the square with an optional size
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """return the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the squre with type & value validations"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """return area of square"""
        return self.__size * self.__size
