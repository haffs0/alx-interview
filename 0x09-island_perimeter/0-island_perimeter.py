#!/usr/bin/python3
"""
Define island_perimeter function
"""


def island_perimeter(grid):
    """
    return: perimeter of island
    args:
        grid: lists of lists
    """
    d, perimeter = 0, 0
    height, length = len(grid), len(grid[0])
    for row in grid:
        c = 0
        for val in row:
            if val == 1:
                surrounding = 4
                if c != length - 1:
                    if grid[d][c + 1] == 1:
                        surrounding -= 1
                if c != 0:
                    if grid[d][c - 1] == 1:
                        surrounding -= 1
                if d != height - 1:
                    if grid[d + 1][c] == 1:
                        surrounding -= 1
                if d != 0:
                    if grid[d - 1][c] == 1:
                        surrounding -= 1
                perimeter += surrounding
            c += 1
        d += 1
    return perimeter
