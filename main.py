# 1. determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop).
# 2. iterate over N and store the solutions in postgres using SQLAlchemy

import time

from algorithms.BacktrackWithBitarray import BacktrackWithBitarraySolution
from database.DBhandler import DBhandler, Solution


def solve_n_queens(queens):

    with DBhandler() as db:

        s = time.perf_counter()
        solutions = len(db.get_solutions(queens))

        if not solutions:
            bt = BacktrackWithBitarraySolution(queens, db=db)
            bt.process()
            solutions = bt.solutions

        e = time.perf_counter()

        if solutions:
            print(f"{solutions} solutions in {e - s} seconds")
        else:
            print(f'No solutions for {queens} queens')

        return solutions or 0


if __name__ == "__main__":
    n = int(input("Type a number N (board of NxN and N queens): "))
    solve_n_queens(n)
