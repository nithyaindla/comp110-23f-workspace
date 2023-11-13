"""EX04 - Useful Functions for Later."""

__author__ = "730653507"


def all(int_list: list[int], num: int) -> bool:
    """Checks if a list(param1) is only made up of a particular integer(param2)."""
    i = 0
    match: bool = True
    if len(int_list) == 0:
        match = False
    else:
        while i < len(int_list):
            """Checks every item in a list and sees if it matches the chosen integer."""
            if int_list[i] != num:
                match = False
            i = i + 1
    return match


def max(int_list: list[int]) -> int:
    """Returns the maximum value in a list of integers."""
    i = 0
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    max_value = int_list[0]
    while i < len(int_list):
        if int_list[i] > max_value:
            max_value = int_list[i]
        i = i + 1
    return max_value


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if two lists are the same."""
    i = 0
    match: bool = True
    if len(list1) != len(list2):
        return False
    """Checks each item in the list and compares it to the corresponding item in the other list."""
    while i < (len(list1) and len(list2)):
        if list1[i] != list2[i]:
            match = False
        i = i + 1
    return match