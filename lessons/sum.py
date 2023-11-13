"""Summing the elements of a list using different loops."""

__author__ = "730653507"


def w_sum(vals: list[float]) -> float:
    """Summing the elements of a list using a while loop."""
    i: int = 0
    sum: float = 0.0
    while i < len(vals):
        sum = float(sum) + float(vals[i])
        i = i + 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Summing the elements of a list using a for loop without range()."""
    sum: float = 0.0
    for i in vals:
        sum = sum + i
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Summing the elements of a list using a for loop with range()."""
    i: int = 0
    sum: float = 0.0
    for i in range(0, len(vals)):
        sum = sum + float(vals[i])
    return sum