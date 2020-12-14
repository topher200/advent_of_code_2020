import solution

def test_undefined_input() -> None:
    assert solution.solve([], 0)
    assert solution.solve([1], 0)
