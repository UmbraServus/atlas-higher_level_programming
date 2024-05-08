#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
   matrix_square = [[x**2 for x in row] for row in matrix]
   return matrix_square
