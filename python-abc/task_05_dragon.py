#!/usr/bin/env python3
"""
Docstring for python-abc.task_05_dragon
"""


class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin,):
    def roar(self):
        print("The dragon roars!")


# 1. Testing the Dragon's Abilities:
# 2. Instantiate an object of the Dragon class named draco.
# 3. Demonstrate draco's abilities by calling the swim, fly,
# and (if implemented) roar methods.

draco = Dragon()

draco.swim()
draco.fly()
draco.roar()
