#!/usr/bin/python3
"""Define an objects.
"""


class Rectangle:
    """Class Rectangle empty.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method - Initialize.
        Args:
            width (int): Width of the Rectangle
            height (int): Height of the Rectangle
        """
        type(self).number_of_instances += 1
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method - Calculate area.
        Returns:
            Rectangle area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Method - Calculate perimeter
        Returns:
            Rectangle perimeter
        """
        if self.height == 0 or self.width == 0:
            return (0)
        return ((2 * self.width) + (2 * self.height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Method - Returns the biggest rectangle based on the area
        Returns:
            Returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.
        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """ Method - Draw the rectangle
        Returns:
            String content draw the rectangle (#)
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """ Method - String represantion the rectangle
        Returns:
            String represantion the rectangle
        """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """ Method - Deleted rectangle
        Returns:
            String 'Bye rectangle...'
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
