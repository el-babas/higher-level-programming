#!/usr/bin/python3
""" Class
        a) Base.
"""
import json
import os.path
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Method: Create a JSON representation of the Base object.

        Args:
            list_dictionaries (dict): A dictionary
        Returns:
            The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Method: Create list of dictionaries from a JSON string.

            Args:
                json_string (str): The JSON string.
            Returns:
                The list of the JSON string representation json_string
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Method: Create a new instance.

        Args:
            dictionary (dict): Contain values of the new instance.
        Returns:
            Instance with all attributes already set.
        """
        if cls.__name__ == "Square":
            new_object = cls(1)
        else:
            new_object = cls(1, 1)
        new_object.update(**dictionary)
        return (new_object)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Method: That writes the JSON string representation
            of list_objs to a file.

            Args:
                cls (class): The class.
                list_objs (list): Is a list of instances who inherits of Base.
                                  Example:
                                  list of Rectangle or list of Square instances
        """
        filename = "{}.json".format(cls.__name__)
        dict_base = []

        if list_objs is None or not list_objs:
            pass
        else:
            for instance in list_objs:
                dict_base.append(instance.to_dictionary())

        json_str = cls.to_json_string(dict_base)

        with open(filename, mode="w") as filejson:
            filejson.write(json_str)

    @classmethod
    def load_from_file(cls):
        """ Method: Create a list of instances.

            Returns:
                List of instances.
        """
        filename = "{}.json".format(cls.__name__)
        if os.path.isfile(filename) is False:
            return (list())

        with open(filename, mode="r") as filejson:
            filecontent = filejson.read()

        list_dict = cls.from_json_string(filecontent)
        list_inst = list()

        for dic in list_dict:
            list_inst.append(cls.create(**dic))

        return (list_inst)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method: That writes the CSV string representation
            of list_objs to a file.

            Args:
                cls (class): The class.
                list_objs (list): Is a list of instances who inherits of Base.
                                  Example:
                                  list of Rectangle or list of Square instances
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode="w") as filecsv:
            if list_objs is not None and list_objs:
                if cls.__name__ == "Rectangle":
                    labels = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    labels = ["id", "size", "x", "y"]
                writer = csv.DictWriter(filecsv, fieldnames=labels)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Method: Create a list of instances.

            Returns:
                List of instances.
        """
        filename = "{}.csv".format(cls.__name__)
        if os.path.isfile(filename) is False:
            return (list())

        with open(filename, mode="r") as filecsv:
            if cls.__name__ == "Rectangle":
                labels = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                labels = ["id", "size", "x", "y"]
            reader = csv.DictReader(filecsv, fieldnames=labels)

            """ Info - Convert str a int the values """
            list_dict = [dict([key, int(value)] for key, value in dic.items())
                         for dic in reader]
            list_inst = list()

            for dic in list_dict:
                list_inst.append(cls.create(**dic))

        return (list_inst)
