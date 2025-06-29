import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        """Initiate the Food"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        """Create the Food for Snake"""
        randomX=random.randint(-280,280)
        randomY=random.randint(-280,280)
        self.goto(randomX,randomY)
