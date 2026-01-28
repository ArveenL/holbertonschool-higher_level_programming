#!/usr/bin/python3

"""
class : Square
"""


class Square:
    """private __size object found after 'self'"""

    def __init__(self, size):
        """
        Docstring for _init_

        :param self: Instance being created
        :param size: Size of square(private information)
        """
        self.__size = size
