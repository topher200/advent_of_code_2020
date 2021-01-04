from typing import Iterable


class Error(Exception):
    pass


class MatchNotFound(Error):
    pass


def solve(input: Iterable[int]) -> int:
    """Given a list of input numbers, find the solution to the problem.

    We do this by iterating through the input. For each int, we check to see if we've seen its "partner" before. (it's "partner" is defined as that <2020 - input_int>). If the input int has a match we perform the multiplcation. Otherwise, we add it to the set of "seen values" and continue to the next."""
    seen_values = set()
    for input_int in input:
        # is this the number we're looking for?
        partner_int = 2020 - input_int
        if partner_int in seen_values:
            # it is! return the multiplier
            return input_int * partner_int
        else:
            # it's not the int set we're looking for. add it to the set and keep iterating
            seen_values.add(input_int)
    raise MatchNotFound("match not found from given input")
