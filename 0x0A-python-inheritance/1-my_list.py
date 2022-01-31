#!/usr/bin/python3
""" Class:
        MyList
"""


class MyList(list):
    """ Class - Inherit from list

    Args:
        list (list): The list
    """

    def print_sorted(self):
        """ Method: Prints the list, but sorted (ascending sort)
        """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
