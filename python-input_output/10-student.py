#!/usr/bin/python3
"""
Module that defines a Student class with JSON filtering capability.
"""


class Student:
    """
    Student class that defines a student by:
    - first_name
    - last_name
    - age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        If attrs is a list of strings, only the attributes listed
        will be included in the dictionary.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {key: self.__dict__[key]
                    for key in attrs
                    if key in self.__dict__}

        return self.__dict__
