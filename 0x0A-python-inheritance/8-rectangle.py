#!/usr/bin/python3
""" Class:
        a) Rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class - Rectangle inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """ Construct - Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
