#!/usr/bin/python3
""" Functions:
        a) append_write.
"""


def append_write(filename="", text=""):
    """ Function: Appends a string at the end of a text file (UTF8).

    Args:
        filename (str): The name of the file to write.
        text (str): The string to write to file.

    Returns:
        The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f_append:
        return (f_append.write(text))
