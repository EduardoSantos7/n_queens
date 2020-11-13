# 1. determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop).
# 2. iterate over N and store the solutions in postgres using SQLAlchemy

import time

from algorithms.BacktrackWithBitarray import BacktrackWithBitarraySolution
from database.DBhandler import DBhandler, Solution


def solve_n_queens(queens, use_db=True):

    if not use_db:
        s = time.perf_counter()
        bt = BacktrackWithBitarraySolution(queens)
        bt.process()
        e = time.perf_counter()
        solutions = bt.solutions
    else:
        with DBhandler() as db:

            s = time.perf_counter()
            solutions = len(db.get_solutions(queens))

            if not solutions:
                print("There were not solutions stored in the DB")
                bt = BacktrackWithBitarraySolution(queens, db=db)
                bt.process()
                solutions = bt.solutions

            e = time.perf_counter()

    if solutions:
        print(f"{solutions} solutions in {e - s} seconds")
    else:
        print(f"No solutions for {queens} queens")

    return solutions or 0


if __name__ == "__main__":
    user_input = input("Type a number N (board of NxN and N queens) or q to finish: ")
    while user_input != "q":
        if user_input.isdecimal():
            n = int(user_input)
            solve_n_queens(
                n,
            )
        else:
            print("Please type only numbers")
        user_input = input(
            "Type a number N (board of NxN and N queens) or q to finish: "
        )
