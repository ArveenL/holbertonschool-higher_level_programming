#!/usr/bin/env python3
"""
Docstring for python-abc.task_02_verboselist
"""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

#  1.list - built-in in python, makes class becomes list
#  2.item - item to append
#  3.super() - call the original method from the parent class
#  4. in our case, the built-in 'list'

    def extend(self, x):
        super().extend(x)
        print(f"Extended the list with {len(x)} items.")

    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, item):
        print(f"Popped {item} from the list.")
        super().pop(item)
