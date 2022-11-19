from turtle import Turtle
class Midline(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.goto((0, -600))
        self.score = 0
        self.pencolor("white")
        self.pensize(5)
        self.goto((0, 600))
        self.hideturtle()
