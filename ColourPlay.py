import turtle
turtle.speed(0)
turtle.left(35)
turtle.bgcolor("black")
for i in range(50):
    for colours in ("red", "magenta", "blue", "grey", "green",):
        turtle.color(colours)
        turtle.pensize(2)
        turtle.forward(200)
        turtle.left(144)
        turtle.forward(201)
        turtle.left(145)