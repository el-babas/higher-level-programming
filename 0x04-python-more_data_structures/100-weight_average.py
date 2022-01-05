#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or my_list is None:
        return (0)
    ''' average of all integers tuple (<score>, <weight>) '''
    num1 = 0
    num2 = 0
    for my_tupla in my_list:
        num1 += my_tupla[0] * my_tupla[1]
        num2 += my_tupla[1]
    return (num1 / num2)
