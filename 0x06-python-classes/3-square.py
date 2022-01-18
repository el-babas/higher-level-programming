#!/usr/bin/python3
""" Define an object name Square.
"""


class Square:
    """ Object Square [class]
    """
    def __init__(self, size=0):
        """ Method - Initialize.

        Args:
            self (class): This class
            size (int): Size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """ Method - Returns the current square area.

        Args:
            self (class): This class
        """
        return (self.__size ** 2)
