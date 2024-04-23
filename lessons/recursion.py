"""CQ07 - Recursion Definition.""" 

__author__ = "730553436"


def f(n: int, k: int) -> int:
    """Function definition for the recursive pattern."""
    if n == 0:  # base case
        return 0
    else:  # recursive rule
        return f(n - 1, k) + k 