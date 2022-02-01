#!/usr/bin/python3
""" Functions:
        a) add_attribute
"""


def add_attribute(obj, att, value):
    """ Function - Add new attribute in the class.

    Args:
        obj (class): The class.
        att (str): The name of the attribute.
        value (any): The value of the attribute.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
        return
    raise TypeError("can't add new attribute")
