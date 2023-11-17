"""File to define River class."""

__author__ = "730653507"


from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """The river ecosystem and all its processes."""

    day: int  # an int that tells you what day of the river’s lifecycle you are modeling.
    bears: list[str]  # a list of Bears that stores the river’s bear population.
    fish: list[str]  # a list of Fish that stores the river’s fish population.
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removed when exceed certain age."""
        new_fish_list: list[Fish] = []
        new_bears_list: list[Bear] = []
        for fishy in self.fish:
            if fishy.age <= 3:
                new_fish_list.append(fishy)
        for bear in self.bears:
            if bear.age <= 5:
                new_bears_list.append(bear)
        self.fish = new_fish_list
        self.bears = new_bears_list
        return None
    
    def remove_fish(self, amount: int):
        """Removes a certain amount of fish from the river."""
        i: int = 0
        while amount != 0:
            self.fish.pop(i)
            amount -= 1
            i += 1

    def bears_eating(self):
        """If there are at least 5 Fish in the river, the Bear will eat 3 Fish."""
        i = 0
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.bears[i].eat(3)
                River.remove_fish(self, 3)
                i += 1
        return None
    
    def check_hunger(self):
        """Removes starving bears."""
        new_bears_list: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score > 0:
                new_bears_list.append(bear)
        self.bears = new_bears_list
        if len(self.bears) == 0:
            self.bears.append(Bear)
        return None
        
    def repopulate_fish(self):
        """If there are 2 fish, 4 new fish will be born."""
        amount: int = ((len(self.fish)) // 2) * 4
        i: int = 0
        while i < amount:
            self.fish.append(Fish)
            i += 1
        return None
    
    def repopulate_bears(self):
        """If there are 2 bears, 1 new bear will be born."""
        amount: int = len(self.bears) / 2
        i: int = 0
        while i < amount:
            self.bears.append(Bear)
            i += 1
        return None
    
    def view_river(self) -> None:
        """Prints the number of fish and bear and the day number."""
        print("~~~ Day " + str(self.day) + ": ~~~\nFish population: " + str(len(self.fish)) + "\nBear population: " + str(len(self.bears)))
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            Bear.one_day(bear)
        # Simulate one day for all Fish
        for fish in self.fish:
            Fish.one_day(fish)
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self) -> None:
        """Simulates one week in the river."""
        day: int = 0
        while day < 7:
            self.one_river_day()
            day += 1
        return None