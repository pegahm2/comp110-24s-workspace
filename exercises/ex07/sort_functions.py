"""Functions that implement sorting algorithms."""

__author__ = "730553436"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    index1: int = 0 
    while index1 < len(x): 
        value: int = x[index1]
        index2 = index1 - 1 
        while index2 >= 0 and value < x[index2]:
            x[index2 + 1] = x[index2]
            index2 -= 1
        x[index2 + 1] = value
        index1 += 1
    return None

def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    index1: int = 0
    while index1 < len(x):
        index2: int = index1
        minimumIndex: int = index2
        while index2 < len(x):
            if x[minimumIndex] > x[index2]:
                minimumIndex = index2
            index2 += 1
        tempValue: int = x[index1]
        x[index1] = x[minimumIndex]
        x[minimumIndex] = tempValue
        index1 += 1

    return None