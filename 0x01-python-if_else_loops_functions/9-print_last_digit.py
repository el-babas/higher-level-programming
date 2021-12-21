#!/usr/bin/python3
def print_last_digit(number):
    ldigit = (number if number > 0 else -(number)) % 10
    print("{:d}".format(ldigit), end="")
    return (ldigit)
