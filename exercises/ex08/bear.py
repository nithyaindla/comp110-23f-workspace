"""File to define Bear class."""

__author__ = "730653507"


class Bear:
    """Everything bear related."""

    age: int
    hunger_score: int
    
    def __init__(self, age_init: int = 0, hunger_score_init: int = 0):
        """Constructor."""
        self.age = age_init
        self.hunger_score = hunger_score_init
    
    def one_day(self) -> None:
        """Increase the value of the age attribute by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None: 
        """Increases hunger score after eating."""
        self.hunger_score += num_fish
        return None