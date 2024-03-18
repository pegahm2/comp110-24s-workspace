"""EX04-Utils.""" 

__author__ = "730553436"
"""Codes for a Bool from a list of integers."""


def all(u_list: list[int], num: int) -> bool:
    """Defining all function."""
    if u_list == []:
        return False
    for elem in u_list:
        if elem != num:
            return False
    return True

        
def max(inputs: list[int]) -> int:
    """Defining max function."""
    if len(inputs) == 0:
        raise (ValueError("max() arg is an empty list"))
    max: int = -1000000
    for num in inputs:
        if num > max:
            max = num
    return max
    

def is_equal(u_list1: list[int], u_list2: list[int]) -> bool:
    """Defining is_equal function."""
    if len(u_list1) != len(u_list2):
        return False
    i: int = 0
    while i < len(u_list1):
        if u_list1[i] != u_list2[i]:
            return False
        i += 1
    return True
    

def extend(num1: list[int], num2: list[int]) -> None: 
    """Defining the extend function."""
    num1.extend(num2)