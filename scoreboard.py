from turtle import Turtle

# CONSTANTS
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
GAME_OVER = "Game Over"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data") as data:
            self.high_score = int(data.read())
        self.goto(0, 565)
        self.color("white")
        self.penup()
        self.hideturtle()
        super().clear()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
