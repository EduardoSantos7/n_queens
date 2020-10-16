import time

from algorithms.BacktrackWithBitarray import BacktrackWithBitarraySolution
from database.DBhandler import DBhandler, Solution


if __name__ == "__main__":
    n = int(input("Type a number N (board of NxN and N queens): "))

    with DBhandler() as db:

        s = time.perf_counter()
        solutions = len(db.get_solutions(n))

        if not solutions:
            bt = BacktrackWithBitarraySolution(n, db=db)
            bt.process()
            solutions = bt.solutions

        e = time.perf_counter()

        print(f"{solutions} solutions in {e - s} seconds")

# 1. determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop).
# 2. iterate over N and store the solutions in postgres using SQLAlchemy
