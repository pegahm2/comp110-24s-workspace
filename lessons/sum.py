"""Define the function."""

__author__ = "730553436"


def w_sum(vals: list[float]) -> float: 
    """Sum of multiple numbers in a list using a while loop."""
    index = 0 
    n_sum = 0.0
    while index < len(vals):
        n_sum += vals[index]
        index += 1
    return n_sum 


def f_sum(vals: list[float]) -> float: 
    """Sum of multiple numbers in a list using for loop."""
    new_f_sum = 0.0 
    for index in vals: 
        new_f_sum += index
    return (new_f_sum)


def f_range_sum(vals: list[float]) -> float: 
    """Sum of multiple numbers in a list using range function."""
    new_sum = 0.0
    for index in range(0, len(vals)):
        new_sum += vals[index]
    return new_sum