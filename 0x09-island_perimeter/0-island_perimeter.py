#!/usr/bin/python3
"""return Island perimeter"""


def island_perimeter(grid):
    """
    returns the perimeter of an island described in grid:

    Grid is a list of integers:
    0 represents water
    1 represents land
    Each cell is square with a side length of 1
    Cells are not connected diagonally but horizontally/vertically
    Grid is rectangular, with it's width and height not exceeding 100
    """
    perimeter = 0

    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                for dx, dy in directions:
                    x, y = i + dx, j + dy

                    if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 0:
                        perimeter += 1
    return perimeter
