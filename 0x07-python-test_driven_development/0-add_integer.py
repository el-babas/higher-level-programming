#!/usr/bin/python3
""" This page content.

    Functions
        add_integer
"""


def add_integer(a, b=98):
    """ Method - The addition of a and b.

    Args:
        a (int, float): Number 1
        b (int, float): Number 2

    Returns:
        The addition of a and b

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
