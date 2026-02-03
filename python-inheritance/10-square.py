#!/usr/bin/python3
"""Square class that inherits from Rectangle."""

Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize Square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        # Since a square is a rectangle with equal width and height
        super().__init__(size, size)

    def area(self):
        """Compute the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the square description: [Square] <width>/<height>."""
        return f"[Square] {self.__size}/{self.__size}"
