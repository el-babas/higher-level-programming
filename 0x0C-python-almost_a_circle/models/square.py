#!/usr/bin/python3
""" Class:
        a) Rectangle (import class)
        a) Square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class - Square inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Construct: Create a new object Square.

        Args:
            size (int): Size of the Square.
            x (int): X position of the Square.
            y (int): Y position of the Square.
            id (int): ID of the Square (inherited from Base).
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """ (Get) The size of the Square (Rectangle). """
        return self.width

    @size.setter
    def size(self, value):
        """ (Set) The size of the Square (Rectangle). """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Method: Update the Square,
            that assigns an argument to each attribute,
            in the order (id, size, x, y)

            Args:
                args (list): A list of new values to atributes.
                kwargs (dict): A dictionary of new values to atributes.
        """
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                self.id = (args[i] if i == 0 else self.id)
                self.size = (args[i] if i == 1 else self.size)
                self.x = (args[i] if i == 2 else self.x)
                self.y = (args[i] if i == 3 else self.y)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Method - Generate dictionary representation Square.

        Returns:
            The dictionary representation of a Square.
            self.__dict__ custom
        """
        dict_squa = {"id": 0, "size": 0, "x": 0, "y": 0}
        for key in dict_squa.keys():
            dict_squa[key] = getattr(self, key)
        return (dict_squa)

    def __str__(self):
        """ Method (custom): Get format string for the Square.

        Returns:
            The representation in str for the Square.
            -'[Square] (<id>) <x>/<y> - <size>'-
        """
        str_squa = "({}) ".format(self.id)
        str_squa += "{}/{} - ".format(self.x, self.y)
        str_squa += "{}".format(self.size)
        return ("[Square] " + str_squa)
