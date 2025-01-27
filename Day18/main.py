import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'


from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("turtle")

#timmy_the_turtle.color("red")
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(100)
timmy_the_turtle.width(width=4)
timmy_the_turtle.speed(speed= 10)

for _ in range(100):
    dist = random.randint(1,200)
    dir = random.randint(0,360)
    timmy_the_turtle.forward(dist)
    timmy_the_turtle.left(dir)


screen = Screen()
screen.exitonclick()