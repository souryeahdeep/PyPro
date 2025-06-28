import random, turtle

race_is_on=False
#Screen Setup
scr = turtle.Screen()
scr.setup(width=500, height=400)
scr.listen()

#Guess the Winner
guess = scr.textinput(title="Winner", prompt="Guess the winner")

y_positions=[-70,-40,-10,20,50,80]
turtle_colors=["red","blue","purple","yellow","green","indigo"]
all_turtles=[]

#Creating turtles with features
for turtle_index in range(0,6):
    deep = turtle.Turtle(shape="turtle")
    deep.penup()
    deep.goto(x=-250, y=y_positions[turtle_index])
    deep.color(turtle_colors[turtle_index])
    all_turtles.append(deep)
#If user provided guess, then start the race
if guess:
    race_is_on=True

winning_color=""
#Race Track
while race_is_on:

    for turtle in all_turtles:
        if turtle.xcor()>=230:
            winning_color=turtle.pencolor()
            race_is_on=False
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

if winning_color==guess:
    print(f"You win! {winning_color} won")
else:
    print(f"You lose. {winning_color} won")

scr.exitonclick()
