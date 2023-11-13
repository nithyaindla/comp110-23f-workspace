from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(0, 60)
leo.pendown()
leo.color("blue")
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()
done()