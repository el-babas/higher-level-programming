#!/usr/bin/python3
""" Functions:
        a) append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """ Function: Inserts a line of text to a file,
        after each line containing a specific string

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search in the file.
        new_string (str): The string to add.
    """
    new_content = ""
    with open(filename, mode="r") as old_file:
        for line in old_file:
            new_content += line
            if search_string in line:
                new_content += new_string

    with open(filename, mode="w") as new_file:
        new_file.write(new_content)
