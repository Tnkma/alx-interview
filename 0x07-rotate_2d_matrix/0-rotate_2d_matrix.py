#!/usr/bin/env python3
"""2D Matrix Rotation"""


def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix

    Args:
        matrix (_type_): _description
    """
    # first we get the length od the matrix
    n = len(matrix)
    # we iterate over the len(matrix) // 2
    for i in range(n // 2):
        # we iterate over the range of i to n - i - 1
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
