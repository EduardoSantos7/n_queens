class Board:
    def __init__(self, N):
        """Represent an NxN chess board

        Args:
            N (int): Size of the board (NXN)
        """

        self.board = [[0 for _ in range(N)] for _ in range(N)]

    def valid_position(self, row_index, col_index):
        # Check this row on left side
        for i in range(col_index):
            if self.board[row_index][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row_index, -1, -1), range(col_index, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row_index, len(self.board), 1), range(col_index, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def place_queen(self, row_index, col_index):
        self.board[row_index][col_index] = 1

    def unplace_queen(self, row_index, col_index):
        self.board[row_index][col_index] = 0
