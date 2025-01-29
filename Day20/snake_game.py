from turtle import Screen
import time 
from snake import Snake

screen = Screen()
screen.setup(width = 600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

#screen.exitonclick()

