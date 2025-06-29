from turtle import Turtle
FONT=("Arial", 20, "normal")
ALIGN="center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.myScore=0
        self.goto(0,270)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Score{self.myScore}", align=ALIGN, font=FONT)
    def game_over(self,reason):
        self.clear()
        self.goto(0,0)
        self.write(reason, align=ALIGN, font=FONT)
    def increase_snake(self):
        self.myScore+=1
        self.clear()
        self.update_scoreboard()