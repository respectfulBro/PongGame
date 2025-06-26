from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.listen()

r_paddle.create_paddle()
l_paddle.create_paddle()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()
scoreboard = Scoreboard()
time_update = 0.2

game_is_on = True
while game_is_on:
    time.sleep(time_update)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle.new_paddle) < 50 and ball.xcor() > 320 or ball.distance(
            l_paddle.new_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        time_update *= 0.9

    elif ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        time_update = 0.2

    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        time_update = 0.2

screen.exitonclick()
