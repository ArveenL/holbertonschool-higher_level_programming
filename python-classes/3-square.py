#!/usr/bin/python3

"""declare class named Square"""


class Square:
    """add value to object, check type &
    value of object, return Error accordingly

    new: now adding method(actions), in this
    example, area"""

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self): # method(action)
        return self.__size * self.__size

# using 'isinstance' instead of 'type(size) != int'
# because of some inheritance thingy
