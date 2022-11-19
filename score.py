from turtle import Turtle


class Score(Turtle):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.speed("fastest")
        self.color("black")
        self.goto((0, -600))
        self.score = 0
        self.pencolor("white")
        self.pensize(5)
        self.goto((0, 600))
        self.penup()

        if self.player == 1:
            self.scorepos = -45
        else:
            self.scorepos = 35
        self.goto((self.scorepos, 250))
        self.ht()
        self.pencolor("white")
        self.write(self.score, False, "center", ("Aries", 28, "normal"))
    def write_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, False, "center", ("Aries", 28, "normal"))
        