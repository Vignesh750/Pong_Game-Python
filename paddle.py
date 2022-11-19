from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        # self.speed("fastest")
        self.penup()
        # self.resizemode("user")
        self.shapesize(5, 1)
        self.color("white")
        self.goto(position, 0)

    def paddle_move_up(self):
        self.goto((self.xcor(), self.ycor()+30))

    def paddle_move_down(self):
        self.goto((self.xcor(), self.ycor()-30))
