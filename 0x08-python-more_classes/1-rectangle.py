#!/usr/bin/python3
"""Define an objects.
"""


class Rectangle:
    """Class Rectangle empty.
    """
    def __init__(self, width=0, height=0):
        """ Method - Initialize.

        Args:
            width (int): Width of the Rectangle
            height (int): Height of the Rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Get - instance attribute width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Set - instance attribute width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Get - instance attribute heigth
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Set - instance attribute height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
