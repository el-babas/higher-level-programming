#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    idx = 0
    for item in matrix:
        idx = 0
        for sub in item:
            if idx != 0:
                print(" ", end="")
            print("{:d}".format(sub), end="")
            idx += 1
        print()
