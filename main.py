import turtle
from turtle import Turtle, Screen

# Set up screen size, title, background color
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sneaky Snake")

# Set up turtle size and color
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_size = []
size = 0
for size in starting_positions:
    new_snake = Turtle(shape="square")
    new_snake.penup()
    new_snake.color("white")
    new_snake.goto(size)
    snake_size.append(new_snake)





screen.exitonclick()