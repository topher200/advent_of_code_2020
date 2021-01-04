import pytest

from advent_of_code_2020.day_1a import solution


def test_undefined_input() -> None:
    empty_list: List[int] = []
    with pytest.raises(solution.MatchNotFound):
        solution.solve(empty_list)

    with pytest.raises(solution.MatchNotFound):
        solution.solve([1])
    with pytest.raises(solution.MatchNotFound):
        solution.solve([1, 2])
    with pytest.raises(solution.MatchNotFound):
        solution.solve([1, 2, 2001])


def test_correct_answer() -> None:
    assert solution.solve([0, 2020]) == 0
    assert solution.solve([1, 2019]) == 2019
    assert solution.solve([0, 1, 2, 2019]) == 2019
    assert solution.solve([0, 1, 20, 2000]) == 40_000


def test_sample_input() -> None:
    assert solution.solve([1721, 979, 366, 299, 675, 1456]) == 514_579
