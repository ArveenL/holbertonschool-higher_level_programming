#!/usr/bin/python3
"""define a parent and child class & print in ascending"""

class Mylist(list):
    """Mylist inherits FROM list"""


    def print_sorted(self):
        """sort ascending  & print"""
        print(sorted(self))
