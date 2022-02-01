#!/usr/bin/python3
""" Functions:
        a) write_file.
"""


def write_file(filename="", text=""):
    """ Function: Write a string to text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The string to write to file.

    Returns:
        The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f_new:
        return (f_new.write(text))
