import copy


def backtrackWithBitarraySolution(
    queens, columns, left_diagonal, right_diagonal, board, row=0
):
    solutions = []
    if row == queens:
        solutions.append(copy.copy(board))
        return solutions

    for col in range(0, queens):
        if (
            not columns[col]
            and not right_diagonal[row - col + queens - 1]
            and not left_diagonal[row + col]
        ):
            columns[col] = 1
            right_diagonal[row - col + queens - 1] = 1
            left_diagonal[row + col] = 1
            board[row] = col

            new_solutions = backtrackWithBitarraySolution(
                queens, columns, left_diagonal, right_diagonal, board, row=row + 1
            )
            solutions.extend(new_solutions)

            columns[col] = 0
            right_diagonal[row - col + queens - 1] = 0
            left_diagonal[row + col] = 0
            board[row] = 0

    return solutions
