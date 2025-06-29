from turtle import Turtle
FONT=("Arial", 20, "normal")
ALIGN="center"
class Scoreboard(Turtle):
    def __init__(self):
        """Creates the Scoreboard"""
        super().__init__()
        self.myScore=0
        self.goto(0,270)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_scoreboard()
    def update_scoreboard(self):
        """Update the Scoreboard"""
        self.write(f"Score{self.myScore}", align=ALIGN, font=FONT)
    def game_over(self,reason):
        """Called when Game is over and prints the reason in the screen"""
        self.clear()
        self.goto(0,0)
        self.write(reason, align=ALIGN, font=FONT)
    def increase_snake(self):
        """Increase the height of Snake"""
        self.myScore+=1
        self.clear()
        self.update_scoreboard()
