from turtle import Turtle, Screen

UP = 0
DOWN = 180


class Paddle:

    def __init__(self, x, y):
        self.new_paddle = Turtle("square")
        self.x = x
        self.y = y

    def create_paddle(self):
        self.new_paddle = Turtle("square")
        self.new_paddle.color("white")
        self.new_paddle.speed("fastest")
        self.new_paddle.shapesize(stretch_len=1, stretch_wid=5, outline=None)
        self.new_paddle.penup()
        self.new_paddle.setposition(self.x, self.y)

    def up(self):
        new_y = self.new_paddle.ycor() + 20
        self.new_paddle.goto(self.new_paddle.xcor(), new_y)

    def down(self):
        new_y = self.new_paddle.ycor() - 20
        self.new_paddle.goto(self.new_paddle.xcor(), new_y)
