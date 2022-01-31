#!/usr/bin/python3
""" Class:
        a) BaseGeometry.
"""


class BaseGeometry:
    """ Class - BaseGeometry
    """

    def area(self):
        """ Method - In construction ...
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method - In construction ...

        Args:
            name (str): String value.
            value (int): Integer value.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
