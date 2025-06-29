import turtle,time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
#Create Screens


screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()


tim=Snake()
food=Food()
score=Scoreboard()
screen.onkey(tim.moveup,"Up")
screen.onkey(tim.movedown,"Down")
screen.onkey(tim.moveleft,"Left")
screen.onkey(tim.moveright,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    tim.move()
    if tim.head.distance(food)<15:
        food.refresh()
        tim.increase_snake()
        score.increase_snake()
    if 300 < tim.head.xcor() or -300>tim.head.xcor() or 300 < tim.head.ycor() or -300>tim.head.ycor():
        score.game_over("GAME OVER. You hit the Wall")
        break
    for turtle in tim.turtle_list[1:]:
        if tim.head.distance(turtle)<10:
            score.game_over("GAME OVER. You hit youself")
            game_is_on=False

screen.exitonclick()