#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list or len(my_list) == 0:
        return (None)
    max_number = my_list[0]
    for item in my_list:
        if item > max_number:
            max_number = item
    return (max_number)
