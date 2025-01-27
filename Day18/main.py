import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'


from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("turtle")

#timmy_the_turtle.color("red")
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(100)

for _ in range(4):
    
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


screen = Screen()
screen.exitonclick()