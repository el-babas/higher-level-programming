#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''get keys and sort'''
    key_list = sorted(list(a_dictionary.keys()))
    for item in key_list:
        print("{0}: {1}".format(item, a_dictionary.get(item)))
