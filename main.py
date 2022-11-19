from turtle import Screen, Turtle
from score import Score
from ball import Ball
from paddle import Paddle
from Midline import Midline
import time

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(800, 600)
my_screen.tracer(0)

paddleR = Paddle(380)
paddleL = Paddle(-380)

scoreL = Score(1)
scoreR = Score(2)
Winner = Turtle()
Midlinem = Midline()
my_screen.listen()

my_screen.onkey(paddleL.paddle_move_up, "w")
my_screen.onkey(paddleL.paddle_move_down, "s")
my_screen.onkey(paddleR.paddle_move_up, "Up")
my_screen.onkey(paddleR.paddle_move_down, "Down")

# if ball.distance(paddleL) < 20 or ball.distance(paddleR) < 20:
#     ball.ball_return()
#     print(ball.distance(paddleR))
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    my_screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_in_y()
    if ball.distance(paddleR) < 50 and ball.xcor() > 350 or ball.distance(paddleL) < 50 and ball.xcor() < -350:
        ball.bounce_ball_in_x()
    if ball.xcor() > 420 or ball.xcor() < -420:
        if ball.xcor() > 420:
            scoreL.write_score()
            ball.reset_position()
        elif ball.xcor() < -420:
            scoreR.write_score()
            ball.reset_position()
    if scoreR.score == 10 or scoreL.score == 10:
        if scoreR.score == 10:
            Winner.write("Right side player has won", False,  "center", ("Aries", 80, "normal"))
        elif scoreR.score == 10:
            Winner.write("Left side player has won", False,  "center", ("Aries", 80, "normal"))


my_screen.exitonclick()
