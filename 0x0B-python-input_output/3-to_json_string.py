#!/usr/bin/python3
import json
""" Functions:
        a) to_json_string.
"""


def to_json_string(my_obj):
    """ Function: Convert object to json string.

    Args:
        my_obj (object): The object to convert.

    Returns:
        The JSON representation of an object (string).
    """
    return (json.dumps(my_obj))
