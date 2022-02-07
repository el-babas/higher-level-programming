#!/usr/bin/python3
""" Class:
        a) Rectangle.
"""
from models.Base import Base


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
