#!/usr/bin/python3
""" Class:
        a) Student
"""


class Student():
    """ Class: Represents an object of type Student.
    """

    def __init__(self, first_name, last_name, age):
        """ Construct: Create object Student.

        Args:
            first_name (str): Name of the first student.
            last_name (str): Name of the last student.
            age (int): Years old to student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method: That retrieves a dictionary
                    representation of a Student instance.

        Returns: The dictionary description with simple data structure.
                 If attrs is a list of strings,
                 only attribute names contained in this list must be retrieved.
        """
        if (type(attrs) is list and all(type(key) == str for key in attrs)):
            dict_obj = dict()
            for key in attrs:
                if hasattr(self, key):
                    dict_obj[key] = getattr(self, key)
            return (dict_obj)
        return (self.__dict__.copy())
