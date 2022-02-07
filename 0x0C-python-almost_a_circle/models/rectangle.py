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
        """ Construct: Create a new object Rectangle.

        Args:
            width (int): Width of the Rectangle.
            height (int): Height of the Rectangle.
            x (int): X position of the Rectangle.
            y (int): Y position of the Rectangle.
            id (int): ID of the Rectangle (inherited from Base).
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ (Get) The width of the Rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """ (Set) The width of the Rectangle. """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ (Get) The height of the Rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        """ (Set) The height of the Rectangle. """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ (Get) The x of the Rectangle. """
        return self.__x

    @x.setter
    def x(self, value):
        """ (Set) The x of the Rectangle. """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ (Get) The y of the Rectangle. """
        return self.__y

    @y.setter
    def y(self, value):
        """ (Set) The y of the Rectangle. """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Method: Calculate the area of the Rectangle.

        Returns:
            The area value of the Rectangle.
        """
        return (self.width * self.height)

    def display(self):
        """ Method: Prints in stdout the Rectangle instance
            with the character #
        """
        stdout_rect = ""
        stdout_rect += ("\n" * self.y)
        for i in range(self.height):
            stdout_rect += (" " * self.x)
            stdout_rect += ("#" * self.width)
            stdout_rect += ("\n")
        print(stdout_rect, end="")

    def update(self, *args, **kwargs):
        """ Method: Update the Rectangle,
            that assigns an argument to each attribute,
            in the order (id, width, height, x, y)

            Args:
                args (list): A list of new values to atributes.
                kwargs (dict): A dictionary of new values to atributes.
        """
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                self.id = (args[i] if i == 0 else self.id)
                self.width = (args[i] if i == 1 else self.width)
                self.height = (args[i] if i == 2 else self.height)
                self.x = (args[i] if i == 3 else self.x)
                self.y = (args[i] if i == 4 else self.y)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ Method (custom): Get format string for the Rectangle.

        Returns:
            The representation in str for the Rectangle.
            -'[Rectangle] (<id>) <x>/<y> - <width>/<height>'-
        """
        str_rect = "({}) ".format(self.id)
        str_rect += "{}/{} - ".format(self.x, self.y)
        str_rect += "{}/{}".format(self.width, self.height)
        return ("[Rectangle] " + str_rect)
