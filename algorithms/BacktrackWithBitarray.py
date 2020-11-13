from database.DBhandler import DBhandler, Solution
from bitarray import bitarray

from utils.Board import Board


class BacktrackWithBitarraySolution:
    def __init__(self, N, db=None):
        """Initialize the board

        Args:
            N (int): Number of queens and size of the board (NXN)
        """
        self.queens = N
        self.solutions = 0
        self.db = db
        self.columns = bitarray([False for _ in range(2 * N)])
        self.board = [[0 for _ in range(N)] for _ in range(N)]
        self.left_diagonal = bitarray([False for _ in range(2 * N)])
        self.right_diagonal = bitarray([False for _ in range(2 * N)])

    def process(self, row=0):
        if row == self.queens:
            self.solutions += 1
            if self.db:
                self.db.add(Solution(self.queens, self.board))
                self.db.commit()
            return

        for col in range(0, self.queens):
            if (
                not self.columns[col]
                and not self.right_diagonal[row - col + self.queens - 1]
                and not self.left_diagonal[row + col]
            ):
                self.columns[col] = 1
                self.right_diagonal[row - col + self.queens - 1] = 1
                self.left_diagonal[row + col] = 1
                self.board[row][col] = 1

                self.process(row + 1)

                self.columns[col] = 0
                self.right_diagonal[row - col + self.queens - 1] = 0
                self.left_diagonal[row + col] = 0
                self.board[row][col] = 0

        return False
