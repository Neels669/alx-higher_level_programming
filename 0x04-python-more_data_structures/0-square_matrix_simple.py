#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = []
    for row in matrix:
        sub_matrix = map(lambda num: num**2, row)
        x.append(list(sub_matrix))
    return x
