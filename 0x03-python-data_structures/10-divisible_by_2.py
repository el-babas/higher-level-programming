#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mult = []
    for item in my_list:
        if item % 2 != 0:
            mult.append(False)
        else:
            mult.append(True)
    return (mult)
