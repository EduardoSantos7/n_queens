class Board:

    def __init__(self, N):
        """Represent an NxN chess board

        Args:
            N (int): Size of the board (NXN)
        """

        self.board = [[0 for _ in N] for _ in N]