#!/usr/bin/python3
"""new: Public instance method: def integer_validator(self, name, value):
that validates value:
you can assume name is always a string

if value is not an integer:
raise a TypeError exception, with the message <name> must be an integer

if value is less or equal to 0:
raise a ValueError exception with the message <name> must be greater than 0"""


class BaseGeometry:
    """docstring"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Docstring for Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
