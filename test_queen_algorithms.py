import sys
import pytest

sys.path.append("./")
from main import solve_n_queens


def get_correct_answer(queens):
    if queens == 1:
        return 1
    if queens == 2:
        return 0
    if queens == 3:
        return 0
    if queens == 4:
        return 2
    if queens == 5:
        return 10
    if queens == 6:
        return 4
    if queens == 7:
        return 40
    if queens == 8:
        return 92
    if queens == 9:
        return 352
    if queens == 10:
        return 724
    if queens == 11:
        return 2_680
    if queens == 12:
        return 14_200
    if queens == 13:
        return 73_712
    if queens == 14:
        return 365_596
    if queens == 15:
        return 2_279_184
    if queens == 16:
        return 14_772_512
    if queens == 17:
        return 95_815_104
    if queens == 18:
        return 666_090_624
    if queens == 19:
        return 4_968_057_848
    if queens == 20:
        return 39_029_188_884
    if queens == 21:
        return 314_666_222_712
    if queens == 22:
        return 2_691_008_701_644
    if queens == 23:
        return 24_233_937_684_440
    if queens == 24:
        return 227_514_171_973_736
    if queens == 25:
        return 2_207_893_435_808_352
    if queens == 26:
        return 22_317_699_616_364_044
    if queens == 27:
        return 234_907_967_154_122_528


@pytest.mark.parametrize(
    "number_of_queens,correct_answer",
    [(n, get_correct_answer(n)) for n in range(1, 12)],
)
def test_n_queens(number_of_queens, correct_answer):
    solutions = solve_n_queens(number_of_queens, use_db=False)
    assert solutions == correct_answer
