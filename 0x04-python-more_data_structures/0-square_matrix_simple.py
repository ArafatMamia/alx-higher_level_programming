#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if(matrix):
        return ([[element*element for element in row] for row in matrix])
