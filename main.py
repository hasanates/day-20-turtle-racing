import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="What color of turtle will win?")
game_on = False
colors = ["red","blue","yellow","green"]
positions = [-40, -10, 20, 50]

turtles = []

for turtle in range(0,4):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-230,y=positions[turtle])
    turtles.append(new_turtle)

if user_bet:
    game_on = True

while game_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            game_on = False
            if turtle.pencolor() == user_bet:
                print("you won")
            else:
                print("you lose")
        turtle.forward(random.randint(0,10))
    



screen.exitonclick()
