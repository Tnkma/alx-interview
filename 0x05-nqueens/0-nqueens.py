#!/usr/bin/python3
""" N-Queens problem """
import sys


def is_safe(board, row, col, N):
    """ Check if a queen can be placed at board[row][col]

    Args:
        board (_type_): _description_
        row (_type_): _description_
        col (_type_): _description_
        N (_type_): _description_

    Returns:
        _type_: true if a queen can be placed at board[row][col], false
    """
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, N, solutions):
    """ Solve N-Queens problem using backtracking

    Args:
        board (_type_): _description_
        row (_type_): _description_
        N (_type_): _description_
        solutions (_type_): if a solution is found, append it to this list
    """
    if row >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, row + 1, N, solutions)
            board[row][col] = 0  # backtrack


def nqueens(N):
    """ Solve N-Queens problem

    Args:
        N (_type_): _description_

    Returns:
        _type_: solutions to N-Queens problem
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    return solutions


def main():
    """ Main function to solve N-Queens problem
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
