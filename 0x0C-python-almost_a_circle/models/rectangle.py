#!/usr/bin/python3
""" Class:
        a) Base (import class)
        a) Rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """ Class - Rectangle inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Construct: Create a new object rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X position of the rectangle.
            y (int): Y position of the rectangle.
            id (int): ID of the rectangle (inherited from Base).
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ (Get) The width of the rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """ (Set) The width of the rectangle. """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ (Get) The height of the rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        """ (Set) The height of the rectangle. """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ (Get) The x of the rectangle. """
        return self.__x

    @x.setter
    def x(self, value):
        """ (Set) The x of the rectangle. """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ (Get) The y of the rectangle. """
        return self.__y

    @y.setter
    def y(self, value):
        """ (Set) The y of the rectangle. """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
