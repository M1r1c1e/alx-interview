#!/usr/bin/python3
"""This module includes a function `island_perimeter`"""


def island_perimeter(grid):
    """To Return the perimeter of the island described in grid"""
    column_size = len(grid[0])
    row_size = len(grid)
    perimeter = 0

    for row in range(row_size):
        for column in range(column_size):
            if grid[row][column]:
                # check left-border
                if column - 1 < 0 or grid[row][column - 1] == 0:
                    perimeter += 1
                # check right-border
                if column + 1 == column_size or grid[row][column + 1] == 0:
                    perimeter += 1
                # check top-border
                if row - 1 < 0 or grid[row - 1][column] == 0:
                    perimeter += 1
                # check bottom-border
                if row + 1 == row_size or grid[row + 1][column] == 0:
                    perimeter += 1
    return perimeter
