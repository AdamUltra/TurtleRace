import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500, 400)
UInp = screen.textinput("The bet", "Which turtle will win the race? Enter a color:").capitalize()
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
y = -90
all_turtles = []
for i in colors:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(i)
    y += 30
    new_turtle.goto(-230, y)
    all_turtles.append(new_turtle)

if UInp:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
        if turtle.xcor() > 230:
            winner = turtle.color()[0]
            if winner == UInp:
                print(f"You've won!! The {winner} turtle is the winner!!!")

            else:
                print(f"You've lost 😤, The {winner} turtle is the winner!!")
            is_race_on = False

screen.exitonclick()
