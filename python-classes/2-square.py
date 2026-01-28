#!/usr/bin/python3

"""class Square"""


class Square:

    def __init__(self, size=0):
        
        """private __size object found after 'self
    
        Initialize a new Square instance.

        :param self: instance being created
        :param size: size of the square (default 0)
        :raises TypeError: if size is not an integer
        :raises ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
   
        if size < 0:
            raise ValueError("size must be >= 0")
   
        self.__size = size
