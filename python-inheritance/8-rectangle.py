#!/usr/bin/python3
"""BaseGeometry class with integer validation and Rectangle subclass."""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Placeholder method for area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer > 0.

        Args:
            name (str): Name of the variable (for error messages)
            value (int): The value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
