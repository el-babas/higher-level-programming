#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for line in range(len(matrix)):
        new_matrix[line] = list(map((lambda x: x**2), matrix[line]))
    return(new_matrix)
