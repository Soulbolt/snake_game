import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set up screen size, title, background color
screen = Screen()
screen.setup(width=1200, height=1200)
screen.bgcolor("black")
screen.title("Sneaky Snake")
screen.tracer(0)  # Allows to turn off animation and update a later time.
# Screen Boundaries
left_bound = -560
right_bound = 560
top_bound = 560
bottom_bound = -560

snake = Snake()
snake_food = Food()
score = Scoreboard()


# Set functions and listening actions for navigation keys
# Key bindings for movement actions
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# Create a while loop to keep game going
game_is_on = True
while game_is_on:
    screen.update()  # Update animation
    time.sleep(0.1)  # delay of animation

    # Make snake move
    snake.move()

    # Detect collision with Walls
    if snake.head.xcor() > 600 or snake.head.xcor() < -600 or snake.head.ycor() > 600 or snake.head.ycor() < -600:
        score.reset()
        snake.reset()

    # Detect collision with food
    if snake.head.distance(snake_food) < 50:
        snake_food.random_dots()
        snake.extend()
        score.increase_score()

    # Detect collision with tail
    for tail_part in snake.snake_size[1:]:
        if snake.head.distance(tail_part) < 10:  # and tail_part != snake.head:
            score.reset()
            snake.reset()
    # Ask to try again or end game.
    # if not game_is_on:
    #     try_again = screen.textinput("Try again?", "Enter yes or no").lower()
    #     if try_again == "yes":
    #         game_is_on = True
    #         screen.clear()
    #     elif try_again == "no":
    #         break
    #     else:
    #         print(f"Invalid input: '{try_again}. Please try again.")

screen.exitonclick()
