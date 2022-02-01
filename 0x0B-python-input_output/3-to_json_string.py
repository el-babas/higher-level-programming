#!/usr/bin/python3
""" Functions:
        a) to_json_string.
"""
import json


def to_json_string(my_obj):
    """ Function: Convert object to json string.

    Args:
        my_obj (object): The object to convert.

    Returns:
        The JSON representation of an object (string).
    """
    return (json.dumps(my_obj))
