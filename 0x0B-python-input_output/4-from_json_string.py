#!/usr/bin/python3
import json
""" Functions:
        a) from_json_string.
"""


def from_json_string(my_str):
    """ Function: Convert an object represented by a JSON string.

    Args:
        my_str (str): JSON string.

    Returns:
        An Object (Python data structure)
    """
    return (json.loads(my_str))
