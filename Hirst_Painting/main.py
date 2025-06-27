
import random
import turtle as turtle_module
import colorgram
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    rgb=(r,g,b)
    rgb_colors.append(rgb)

turtle_module.colormode(255)
turtle=turtle_module.Turtle()
screen=turtle_module.Screen()

def hirst_painting():
    """Function that creates Hirst's Dot Painting(google it) from a list of colors."""
    yax=-100
    turtle.penup()
    turtle.goto(0,-100)
    for _ in range(10):
        xax=40
        for _ in range(10):
            col=random.choice(rgb_colors)
            turtle.dot(20,col)
            turtle.penup()
            turtle.setx(xax)
            xax+=40
        yax+=40
        turtle.goto(0,yax)

hirst_painting()

screen.exitonclick()