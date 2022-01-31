#!/usr/bin/python3
""" Functions:
       is_same_class
"""


def is_same_class(obj, a_class):
    """ Function - Verify instances of objects.

    Args:
        obj (object): Any object.
        a_class (instance): Instance of the any class
    Returns:
        True if the object is exactly an instance of the class or False.

    """

    return (type(obj) is a_class)
