#!/usr/bin/python3
""" Class:
        a) MyList
"""


class MyList(list):
    """ Class - Inherit from list

    Args:
        list (list): The list
    """

    def print_sorted(self):
        """ Method: Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
