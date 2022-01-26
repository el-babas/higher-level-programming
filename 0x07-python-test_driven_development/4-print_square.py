#!/usr/bin/python3
""" This page content.

    Functions
        print_square
"""


def print_square(size):
    """ Function - that prints a square with the character #.

    Args:
        size (int): Size of the square

    Returns:
        No return

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
