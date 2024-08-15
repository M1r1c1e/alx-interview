#!/usr/bin/python3
"""Defining a function `rotate_2d_matrix`"""


def rotate_2d_matrix(matrix):
    """Rotates  n x n 2D matrix in 90 degrees clockwise"""
    n = len(matrix)

    # swap the position of each matrix element
    for t in range(n):
        for c in range(t, n):
            matrix[t][c], matrix[c][t] = matrix[c][t], matrix[t][c]

    # reverse the rows
    for array in matrix:
        array.reverse()
