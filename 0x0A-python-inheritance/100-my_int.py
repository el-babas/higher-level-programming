#!/usr/bin/python3
""" Class:
        a) MyInt.
"""


class MyInt(int):
    """ Class - MyInt class (object) inherits from Int.
    """

    def __eq__(self, other):
        """ Method (custom) - Invert the function == for !=
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method (custom) - Invert the function != for ==
        """
        return int.__eq__(self, other)
