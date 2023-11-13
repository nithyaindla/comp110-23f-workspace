"""EX05 - My beautiful beautiful painting!: Valley Home.

Requirements:
0- Lines 51-60, 63-72, 75-86, 89-100, 103-109, 112-116: Multiple functions with parameters as instructed.
1- Lines 21-48, 119-120: main()
2- Line 35, 38: reusing draw_rectangle().
3- Lines 56-59: Use loop to draw square
4- Line 34, 54: Use the parameter color to set color of pen. 
5- Line 34, 54, 55, 60: Use the paramter color to set a fill color and fill the shape.
6- right here!
7- Lines 112-116: the move_turtle function simplifies three lines of code that would be needed to use frequent times into one function that can be called each time.
8- Line 32: use the .home() function that was not covered in the turtle tutorial, but found in the documentation and is incedibly useful.
"""

__author__ = "730653507"

from turtle import Turtle, done


def main() -> None:
    """The entrypoint of my scene."""
    # Turtle variable(s) here:
    john: Turtle = Turtle()  # the builder
    craig: Turtle = Turtle()  # the landscaper
    linda: Turtle = Turtle()  # the architect
    # Procedures:
    john.speed(82374270982097480730)
    move_turtle(craig, -50, -50)
    draw_mountains(craig, -300, 36, 2, "lime")
    craig.penup()
    craig.home()
    draw_landscape(craig)
    draw_square(john, 150, 90, "red")
    draw_rectangle(john, 25, -100, "brown")
    draw_triangle(john, 150, 120, "pink")
    move_turtle(linda, 58, -90)
    draw_rectangle(linda, 30, 60, "purple")
    move_turtle(linda, 25, -20)
    draw_square(linda, 20, 90, "maroon")
    move_turtle(linda, 61, -20)
    draw_square(linda, 20, 90, "maroon")
    move_turtle(linda, 97, -20)
    draw_square(linda, 20, 90, "maroon")
    john.hideturtle()
    linda.hideturtle()
    craig.hideturtle()
    done()


def draw_square(turtle: Turtle, length: float, degrees: float, color: str) -> None:
    """Draws a 4-sided figure(ex: square) with specified length, angle, and color."""
    i: int = 0
    turtle.color(color, color)
    turtle.begin_fill()
    while i < 4:
        turtle.forward(length)
        turtle.right(degrees)
        i = i + 1
    turtle.end_fill()


def draw_triangle(turtle: Turtle, length: float, angle: float, color: str) -> None:
    """Draws a 3-sided figure of specified length, angle, and color."""
    turtle.color(color, color)
    turtle.begin_fill()
    turtle.forward(length)
    turtle.left(angle)
    turtle.forward(length)
    turtle.left(angle)
    turtle.forward(length)
    turtle.end_fill()


def draw_rectangle(turtle: Turtle, x: float, y: float, color: str) -> None:
    """Draws a rectangle of specified length, height, and color."""
    i: int = 0
    turtle.color(color, color)
    turtle.begin_fill()
    while i < 2:
        turtle.forward(x)
        turtle.right(90)
        turtle.forward(y)
        turtle.right(90)
        i = i + 1
    turtle.end_fill()


def draw_mountains(turtle: Turtle, height: float, angle: float, quantity: int, color: str) -> None:
    """Draws a specified number of mountain shapes of specfied height, angle, and color."""
    turtle.color(color, color)
    turtle.begin_fill()
    i: int = 0
    while i < quantity:
        turtle.left(angle)
        turtle.forward(height)
        turtle.right(2 * angle)
        turtle.forward(height)
        i = i + 1
    turtle.end_fill()


def draw_landscape(turtle: Turtle) -> None:
    """Draws the ground and grass."""
    turtle.penup()
    turtle.goto(-1000, -50)
    turtle.pendown()
    turtle.speed(5678429208342)
    draw_rectangle(turtle, 10000, 10000, "green")


def move_turtle(turtle: Turtle, x: float, y: float) -> None:
    """Moves the Turtle cursor without leaving a trail. Helps streamline the code."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


if __name__ == "__main__":
    main()