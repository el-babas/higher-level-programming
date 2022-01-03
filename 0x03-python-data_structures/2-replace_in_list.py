#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    count = len(my_list)
    if (idx > (count - 1) or idx < 0):
        return (my_list)
    my_list[idx] = element
    return (my_list)
