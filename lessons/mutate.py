"""Mutating functions."""
__author__ = "730553436"


def manual_append(a: list[int], b: int) -> None: 
    """Example Manual Function Definition below."""
    a.append(b)


def double(a: list[int]) -> None: 
    """Example Double Function Definition below."""
    index = 0 
    while index < len(a):
        a[index] *= 2
        index += 1