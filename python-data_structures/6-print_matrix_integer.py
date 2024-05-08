#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{:d}".format(col))
            if row != col[-1]:
                print(" ", end="")
        print()