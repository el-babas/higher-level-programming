#!/usr/bin/python3
import json
""" Functions:
        a) load_from_json_file.
"""


def load_from_json_file(filename):
    """ Function : creates an Object from a “JSON file”.

    Args:
        filename (str): Path or name to the JSON file.

    Returns:
        The object created from the JSON file.
    """
    with open(filename, mode="r", encoding="utf-8") as f_json:
        return (json.load(f_json))
