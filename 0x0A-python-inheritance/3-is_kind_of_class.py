#!/usr/bin/python3
""" Functions
       a) is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """ Function - Verify instances of the object

    Args:
        obj (object): The object.
        a_class (instance): The instance any class
    Returns:
        True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class ; otherwise False.
    """

    return (isinstance(obj, a_class))
