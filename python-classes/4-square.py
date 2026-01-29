#!/usr/bin/python3
"""declare class named Square"""


class Square:
    """
    new: SETTER = prevents attribute from being READ
    freely

    new: GETTER = prevents attribute from being MODIFIED
    freely"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):         # getter
        return self.__size

    @size.setter
    def size(self, value):  # setter
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value  # Actually store the value!

    def area(self):
        return self.__size * self.__size

# using 'isinstance' instead of 'type(size) != int'
# because of some inheritance thingy
