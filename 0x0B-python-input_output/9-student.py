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

    def to_json(self):
        """ Method: That retrieves a dictionary
                    representation of a Student instance.

        Returns: The dictionary description with simple data structure
                (list, dictionary, string, integer and boolean)
                for JSON serialization of an object
        """
        return (self.__dict__.copy())
