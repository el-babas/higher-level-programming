#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    if not roman_string or roman_string is None:
        return (num)
    d_roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    '''for c in roman_string:'''
    lgth = len(roman_string)
    for i in range(lgth):
        c = roman_string[i]
        if d_roman.get(c) is not None:
            if (i + 1) != lgth and d_roman[c] < d_roman[roman_string[i + 1]]:
                num += d_roman[c] * -1
            else:
                num += d_roman[c]
        else:
            num = 0
            break
    return (num)
