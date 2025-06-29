import turtle,scoreboard
X_POS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.turtle_list=[]
        self.create_snake()
        self.head=self.turtle_list[0]
    def create_snake(self):
        for x in X_POS:
            snake=turtle.Turtle(shape="square")
            snake.penup()
            snake.color("white")
            snake.goto(x)
            self.turtle_list.append(snake)
    def increase_snake(self):
        snake=turtle.Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(self.turtle_list[len(self.turtle_list)-1].pos())
        self.turtle_list.append(snake)
    def move(self):
        for seg in range(len(self.turtle_list)-1,0,-1):
            new_x=self.turtle_list[seg-1].xcor()
            new_y=self.turtle_list[seg-1].ycor()
            self.turtle_list[seg].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    def moveup(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def movedown(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def moveleft(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def moveright(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)