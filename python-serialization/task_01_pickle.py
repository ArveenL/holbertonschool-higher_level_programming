
#!/usr/bin/env python3
"""Serialize and deserialize custom objects using pickle."""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                return obj if isinstance(obj, cls) else None
        except (OSError, pickle.PickleError, EOFError,
                AttributeError, ImportError, ValueError):
            return None
