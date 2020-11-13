# 1. determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop).
# 2. iterate over N and store the solutions in postgres using SQLAlchemy

import time

from bitarray import bitarray

from algorithms.BacktrackWithBitarray import backtrackWithBitarraySolution
from database.DBhandler import DBhandler, Solution


def solve_n_queens(queens, use_db=True):

    columns = bitarray([False for _ in range(2 * queens)])
    board = [0 for _ in range(queens)]
    left_diagonal = bitarray([False for _ in range(2 * queens)])
    right_diagonal = bitarray([False for _ in range(2 * queens)])
    solutions = []

    if not use_db:
        s = time.perf_counter()
        solutions = backtrackWithBitarraySolution(
            queens, columns, left_diagonal, right_diagonal, board
        )
        e = time.perf_counter()
        print(f"{len(solutions)} solutions in {e - s} seconds")
    else:
        with DBhandler() as db:

            solutions_in_db = db.get_solutions(queens)

            s = time.perf_counter()

            if not solutions_in_db:
                print("There were not solutions stored in the DB")
                solutions = backtrackWithBitarraySolution(
                    queens, columns, left_diagonal, right_diagonal, board
                )

            e = time.perf_counter()

            if solutions_in_db:
                solutions = solutions_in_db
                print(f"{len(solutions_in_db)} solutions in {e - s} seconds")
            elif solutions:
                solutions_objects = [Solution(queens, board) for board in solutions]
                db.bulk_save_objects(solutions_objects)
                db.commit()
                print(f"{len(solutions)} solutions in {e - s} seconds")
            else:
                print(f"No solutions for {queens} queens")

    return len(solutions)


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
