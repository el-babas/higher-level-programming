#!/usr/bin/python3
""" Functions
       a) inherits_from
"""


def inherits_from(obj, a_class):
    """ Function - Verify instances of the object

    Args:
        obj (object): The object.
        a_class (instance): The instance any class
    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ;
        otherwise False.
    """
    if type(obj) is a_class:
        return (False)
    return (isinstance(obj, a_class))
