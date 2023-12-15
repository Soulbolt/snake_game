from turtle import Turtle
import random


# def random_dots(x, y):
#     new_dot = Turtle(shape="circle")
#     new_dot.penup()
#     new_dot.color("SkyBlue")
#     # new_dot.hideturtle()
#     new_dot.goto(x, y)
#     return new_dot


# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_size = []
        self.create_snakes()
        self.head = self.snake_size[0]
        # self.reset_location()

    def create_snakes(self):
        for location in STARTING_POSITIONS:
            new_snake = Turtle(shape="square")
            new_snake.penup()
            new_snake.color("white")
            new_snake.goto(location)
            self.snake_size.append(new_snake)

    def move(self):
        for segment_num in range(len(self.snake_size) - 1, 0, -1):  # movement (Start, stop, step)
            new_x = self.snake_size[segment_num - 1].xcor()  # Previous snake segment coordinates
            new_y = self.snake_size[segment_num - 1].ycor()
            self.snake_size[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_location(self):
        for size in self.snake_size:
            size.reset()
        # self.move()
