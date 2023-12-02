"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730653507"


class Simpy:
    """Class for Simpy."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, x_init: list[float]):
        """Constructor."""
        self.values = x_init
    
    def __str__(self) -> str:
        """Returns a string."""
        return (f"Simpy({self.values})")

    def fill(self, val: float, num: int) -> None:
        """Fills in the `values` attribute with range of values, like the `range` built-in function, but in terms of `floats."""
        self.values.clear()
        i: int = 0
        while i < num:
            self.values.append(val)
            i += 1

    def arange(self, start: float, stop: float, step: float) -> None:
        """Fills a list based off specified range and increments."""
        assert step != 0
        i = 1
        self.values.append(start)  
        next: int = self.values[i - 1] + step
        while next != stop:
            self.values.append(next)
            i += 1
            next = self.values[i - 1] + step

    def sum(self) -> float:
        """Computes and returns the sum of all items in the `values` attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Use the _addition operator_ (`+`) in conjunction with `Simpy` objects and floats."""
        a = Simpy([])
        if type(rhs) is float:
            for i in self.values:
                a.values.append(i + rhs)
        elif type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                new_val: float = self.values[i] + rhs.values[i]
                a.values.append(new_val)
        return a

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Use the power operator (`**`) in conjunction with `Simpy` objects and floats."""
        a = Simpy([])
        if type(rhs) is float:
            for i in self.values:
                a.values.append(i ** rhs)
        elif type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                new_val: float = self.values[i] ** rhs.values[i]
                a.values.append(new_val)
        return a
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a list[bool] based on the equality between each item in the `values` attribute with some other `Simpy` object or a `float` value."""
        output: list[bool] = []
        if type(rhs) is Simpy:
            for i in range(0, len(self.values)):
                if self.values[i] == rhs.values[i]:
                    output.append(True)
                else: 
                    output.append(False)
        if type(rhs) is float:
            for i in self.values:
                if i == rhs:
                    output.append(True)
                else:
                    output.append(False)
        return output
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a list[bool] based on the greater than relationship between each item in the `values` attribute with some other `Simpy` object or a `float` value."""
        output: list[bool] = []
        if type(rhs) is Simpy:
            for i in range(0, len(self.values)):
                if self.values[i] > rhs.values[i]:
                    output.append(True)
                else: 
                    output.append(False)
        if type(rhs) is float:
            for i in self.values:
                if i > rhs:
                    output.append(True)
                else:
                    output.append(False)
        return output
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Returns items that follow criteria."""
        output = Simpy([])
        if type(rhs) is int:
            return self.values[rhs]
        else:
            for i in range(len(rhs)):
                if rhs[i] is True:
                    output.values.append(self.values[i])
        return output