#!/usr/bin/python3
"""
Defines a Square class with size, position, area, and printing functionality.
"""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with optional size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation (tuple of 2 positive integers)."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
            or not all(i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' respecting its position."""
        if self.__size == 0:
            print()
            return

        # print blank lines for position[1]
        for _ in range(self.__position[1]):
            print()

        # print each line of the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
