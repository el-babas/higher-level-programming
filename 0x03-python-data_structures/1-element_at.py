#!/usr/bin/python3
def element_at(my_list, idx):
    count = len(my_list)
    if (idx > (count - 1) or idx < 0):
        return (None)
    return (my_list[idx])
