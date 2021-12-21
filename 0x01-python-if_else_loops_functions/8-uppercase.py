#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in range(0, len(str)):
        """ ASCII code convert ord(c) """
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            new_str += chr(ord(str[i]) - 32)
        else:
            new_str += str[i]
    print("{0:s}".format(new_str))
