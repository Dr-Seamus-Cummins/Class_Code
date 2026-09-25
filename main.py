import turtle
import math

def draw_multicolor_square(t, sz):
    for i in ["red", "purple", "hotpink", "blue","yellow","green"]:
        t.color(i)
        t.forward(sz)
        t.left(60)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.tracer(1,0)
tess = turtle.Turtle()
tess.pensize(3)
size = 30

# method to draw ellipse
def draw(rad):
    
  # rad --> radius of arc
  for i in range(2):
    
    # two arcs
    turtle.circle(rad,90)
    turtle.circle(rad//2,90)




for i in range(1):
    tess.penup()
    tess.left(90)
    tess.forward(100)
    tess.left(90)
    tess.pendown()
    tess.speed(10)


for i in range(36):
# Set up the window and its attributes
# Create tess and set some attributes
# Size of the smallest square
    draw_multicolor_square(tess, size)
    tess.forward(10)
    tess.right(10)
    tess.speed(10)


for i in range(1):
    tess.penup()
    tess.home()
    tess.left(90)
    tess.forward(125)
    tess.right(90)
    tess.pendown()

size = 40

for i in range(20):
# Set up the window and its attributes
# Create tess and set some attributes
# Size of the smallest square
    draw_multicolor_square(tess, size)
    tess.forward(-10)
    tess.right(18)


for i in range(1):
    tess.penup()
    tess.home()
    tess.left(-90)
    tess.forward(200)
    tess.left(180)
    tess.pendown()
    tess.color("Green") # Tell tess to change her color
    tess.pensize(7)
    tess.forward(100)
    r = 50
    #tess.circle(r)
    tess.circle(r,90)
    tess.circle(r/2,90)
    tess.circle(r,90)
    tess.circle(r/2,90)
    tess.forward(145)
    
    
tess.hideturtle()
wn.update()
