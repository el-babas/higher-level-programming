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
        self.size = size

    def area(self):
        """ Method - Returns the current square area.

        Args:
            self (class): This class
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Get - instance attribute size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Set - instance attribute size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
