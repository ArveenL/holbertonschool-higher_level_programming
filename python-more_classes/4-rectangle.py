#!/usr/bin/python3
"""class Rectangle with objects, property,
setter"""


class Rectangle:
    """width, height objects with setters / cal area & perimeter
    of rectangle / print() & str()

    new: __eq__ """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        else:
            return self.width == other.width and self.height == other.height

# __eq__ -> comparing two different objects if they're the same. We use ==
# self  -> Rectangle as defined by class
# False -> (different objects)
# True  -> (same width & height)
# ..