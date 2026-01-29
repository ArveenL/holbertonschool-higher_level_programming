#!/usr/bin/python3

"""declare class named Square"""


class Square:
    """add value to object, check type &
    value of object, return Error accordingly"""

    def __init__(self, size=0):
        self.__size = size

    if type(size) != int:
        TypeError("size must be an integer")

    if size < 0:
        TypeError("size must be >= 0")

#adding notes to prevent ds_store bullshit