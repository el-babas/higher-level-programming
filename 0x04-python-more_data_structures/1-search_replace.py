#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(len(new_list)):
        new_list[i] = replace if my_list[i] == search else my_list[i]
    return (new_list)
