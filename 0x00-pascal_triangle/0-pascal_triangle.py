#!/usr/bin/python3
"""This is a function that creates `pascal_triangle`"""


def pascal_triangle(n):
    """
    creates Pascal's Triangle up to the nth row.

    Parameters:
        n (int): The number of rows to create in Pascal's Triangle.

    Returns: A list of lists representing Pascal's Triangle up to the nth row.
    """
    triangle = []
    for T in range(n):
        row = []
        for P in range(T + 1):
            if (P == 0) or (P == T):
                row.append(1)
            else:
                row.append(triangle[T - 1][P] + triangle[T - 1][P - 1])
        triangle.append(row)
    return triangle
