#!/usr/bin/python3
""" Class:
        a) Square.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class - Square inherits from Rectangle
    """

    def __init__(self, size):
        """ Construct - Rectangle object.

        Args:
            size (int): Height and Width of the rectangle.

        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method - Area of the Square

        Returns:
            The area of the Square inherited from Rectangle.
        """
        return (super().area())
