from turtle import Turtle, Screen
import random

is_race_on = False

colors = ['red', 'orange', 'yellow', 'purple', 'blue', 'green']
all_turtles = []

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="enter the color that will win")
screen.listen()

y_coord = 125

for color in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[color])
    new_turtle.goto(x=-230, y=y_coord)
    y_coord -= 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"user won, winning turtle: {winning_turtle}")
            else:
                print(f"user loose, winning turtle: {winning_turtle}")
            is_race_on = False
        distance = random.randint(1, 10)
        turtle.forward(distance)

screen.exitonclick()
