from turtle import Turtle, Screen, ontimer
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

scoreboard = Scoreboard()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball((0,0))

boundary_top = 300
boundary_bottom = -300

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    # collision with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_wall()

    if ball.xcor() > 350:
        scoreboard.increase_score_left()
        #scoreboard.end_game(game_is_on)
        ball.ball_reset()

    if ball.xcor() < -350:
        scoreboard.increase_score_right()
        #scoreboard.end_game(game_is_on)
        ball.ball_reset()


# how would I separate pong to different classes?
# class for score board
# class to initialize the dividing line
# class for player to control the side
# class for computer
# class for puck

# create screen
# create and move paddle
# create another paddle
# create ball and make it move
# detect collision with wall and bounce
# detect collision with paddle
# detect when paddle misses
# keep score



screen.exitonclick()
