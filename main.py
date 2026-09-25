import turtle

pen = turtle.Turtle()
pen.color("blue")
pen.pensize(4)
pen.speed(3)

for side in range(4):
    pen.forward(100)
    pen.left(90)

pen.hideturtle()

