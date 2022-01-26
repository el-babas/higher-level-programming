#!/usr/bin/python3
""" This page content.

    Functions
        text_indentation
"""


def text_indentation(text):
    """ Function - that prints a text with 2 new lines after
    each of these characters: ., ? and :

    Args:
        text (str): The text

    Returns:
        No return

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for lim in ".:?":
        text = (lim + "\n\n").join(
            [line.strip(" ") for line in text.split(lim)])

    print(text, end="")
