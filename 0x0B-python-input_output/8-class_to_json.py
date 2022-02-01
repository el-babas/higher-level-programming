""" Functions:
        a) class_to_json
"""


def class_to_json(obj):
    """ Function: Get dictionary of class

    Args:
        obj (object): Is an instance of class.

    Returns:
        The dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object
    """
    dict_obj = dict()
    if hasattr(obj, '__dict__'):
        dict_obj = obj.__dict__.copy()
    return (dict_obj)
