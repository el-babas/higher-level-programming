#!/usr/bin/python3
""" This page content.

    Functions
        matrix_divided
"""


def matrix_divided(matrix, div):
    """ Function -  That divides all elements of a matrix.

    Args:
        matrix (list): A list
        div (int, float): The divisor

    Returns:
        new matrix

    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(item, list) for item in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(item) == len(matrix[0]) for item in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    rs = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (rs)
