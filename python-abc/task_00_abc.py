#!/usr/bin/env python3
"""
Docstring for python-abc.task_00_abc
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod  # <-decorator
    def sound(self):  # <-method
        pass


class Dog(Animal):
    def sound(self):  # <-method
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
