#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """Island Perimeter

    Args:
        grid (_type_):grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
        The grid is completely surrounded by water
        There is only one island (or nothing).
        The island doesn’t have “lakes” (water inside that isn’t connected
        to the water surrounding the island).

    Returns:
        int: returns the perimeter of the island described in grid
    """
    rows = len(grid)
    columns = len(grid[0])
    perimter = 0

    # first we check grid for land and water
    for row in range(rows):
        for column in range(columns):
            # if we find land we check for its neighbours
            # if we find water we skip
            if grid[row][column] == 1:
                # we check for its up neighbour
                if row == 0 or grid[row - 1][column] == 0:
                    # we add 1 to the perimeter
                    perimter += 1
                # we check for its down neighbour
                if row == rows - 1 or grid[row + 1][column] == 0:
                    # we add 1 to the perimeter
                    perimter += 1
                # we check for its left neighbour
                if column == 0 or grid[row][column - 1] == 0:
                    # we add 1 to the perimeter
                    perimter += 1
                # we check for its right neighbour
                if column == columns - 1 or grid[row][column + 1] == 0:
                    # we add 1 to the perimeter
                    perimter += 1
    return perimter
