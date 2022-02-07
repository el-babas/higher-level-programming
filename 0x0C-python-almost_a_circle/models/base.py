#!/usr/bin/python3
""" Class
        a) Base.
"""


class Base:
    """ Class: Tipe Base.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Construct: Base Object.

        Args:
            id (int): The id of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
