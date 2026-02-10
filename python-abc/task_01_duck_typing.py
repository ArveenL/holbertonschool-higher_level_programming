#!/usr/bin/env python3

import math
"""
Docstring for python-abc.task_01_duck_typing
"""

from abc import ABC, abstractmethod


class Shape(ABC):  # <- ??
    @abstractmethod  # <- decorator
    def area(self):  #  an abstract method
        pass

    @abstractmethod  # <- decorator
    def perimeter(self):  # an abstract method
        pass

class Circle(Shape):  # <- concrete class
    def __init__(self, radius):  # <- constructor, to make the variable radius, run
        self.radius = abs(radius)

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius  # <- fixed: removed extra 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)
