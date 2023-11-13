"""For the future. Declaring a class below."""
from __future__ import annotations


class Point:
    """This class will include different methods where its attributes are a representation of (x,y)."""
    # attributes
    x: float
    y: float
    
    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """This method will "scale" a point."""
        self.x = self.x * factor
        self.y = self.y * factor
        
    def scale(self, factor: int) -> Point:
        """This method will multiply the x and y values by some value."""
        new_Point: Point = Point(self.x * factor, self.y * factor)
        return new_Point

    def __str__(self) -> str:
        """Magic method."""
        return ("x: " + str(self.x) + "; y: " + str(self.y))
    
    def __mul__(self, factor: int | float) -> Point:
        """Overload the multiplication * operator."""
        x: float = self.x * factor
        y: float = self.y * factor
        new_point: Point = Point(x, y)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Overload the addition + operator."""
        x: float = self.x + factor
        y: float = self.y + factor
        new_point: Point = Point(x, y)
        return new_point