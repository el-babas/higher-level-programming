#!/usr/bin/python3
""" Functions:
        a) read_file
"""


def read_file(filename=""):
    """ Function: Read File and print it to stdout.

    Args:
        filename (str): The filename to read.

    """
    with open(filename, mode="r", encoding="utf-8") as f_txt:
        print(f_txt.read(), end='')
