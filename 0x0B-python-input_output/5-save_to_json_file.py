#!/usr/bin/python3
""" Functions:
        a) save_to_json_file.
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function: writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (object): Object convert to JSON string.
        filename (str): Text file to write.
    """
    with open(filename, mode="w", encoding="utf-8") as f_json:
        json.dump(my_obj, f_json)
