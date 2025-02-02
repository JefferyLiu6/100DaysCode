FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(-230, 270)
        self.hideturtle()  
        self.color("black")

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}" , align = "center", font=FONT)

    def increase_level(self):
        self.score += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
