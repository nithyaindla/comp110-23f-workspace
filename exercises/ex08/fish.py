"""File to define Fish class."""

__author__ = "730653507"


class Fish:
    """Everything fish related."""

    age: int
    
    def __init__(self, age_init: int = 0) -> None:
        """Constructor."""
        self.age = 0
        return None
    
    def one_day(self):
        """Increases the age of the fish."""
        self.age += 1
        return None