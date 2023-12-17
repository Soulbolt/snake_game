from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=4.5, stretch_wid=4.5)  # customize shape size
        self.color("SkyBlue")
        self.speed("fastest")
        self.random_dots()

    def random_dots(self):
        random_x = random.randint(-530, 530)
        random_y = random.randint(-530, 530)
        self.goto(random_x, random_y)

