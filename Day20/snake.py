from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)] 

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
                     
        for position in STARTING_POSITION:

            tim = Turtle()
            tim.shape("square")
            tim.color("white")
            tim.penup()
            tim.goto(position)
            self.segments.append(tim)