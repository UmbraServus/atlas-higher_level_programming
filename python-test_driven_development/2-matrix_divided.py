#!/usr/bin/python3

""" matrix division method """

def matrix_divided(matrix, div):

    """returns: a matrix with each of its elements divided by div
       rounded to 2 decimal places.

        Raises:
            TypeError: if matrix is not a list of lists or if each
            element of the matrix isnt an int/float

            TypeError: each row must have the same size

            TypeError: div must be a number

            ZeroDivisionError: division by zero is impossible"""

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = []

    for row in matrix:
        new_row = []

        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        result_matrix.append(new_row)

    return result_matrix
