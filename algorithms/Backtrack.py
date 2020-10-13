from utils.Board import Board


class BacktrackSolution:
    def __init__(self, N):
        """Initialize the board

        Args:
            N (int): Number of queens and size of the board (NXN)
        """
        self.board = Board(N)
        self.queens = N

    def process(self, col_index=0):
        if col_index >= self.queens:
            return True
        for row_index in range(self.queens):
            if self.board.valid_position(row_index, col_index):
                self.board.place_queen(row_index, col_index)

                if self.process(col_index=col_index + 1):
                    return True

                # Solution not found
                self.board.unplace_queen(row_index, col_index)

        return False
