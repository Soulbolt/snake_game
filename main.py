import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set up screen size, title, background color
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sneaky Snake")
screen.tracer(0)  # Allows to turn off animation and update a later time.
# Screen Boundaries
left_bound = -280
right_bound = 280
top_bound = 280
bottom_bound = -280

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

    if snake.head.xcor() > right_bound or snake.head.xcor() < left_bound:
        game_is_on = False
        print("You lose! You've crashed into Trumps Wall!")

    if snake.head.ycor() > top_bound or snake.head.ycor() < bottom_bound:
        game_is_on = False
        print("You lose! You've crashed into Trumps Wall!")

    if snake.head.distance(snake_food) < 15:
        print("nom nom nom!")
        snake_food.random_dots()
        score.increase_score()

    if not game_is_on:
        try_again = screen.textinput("Try again?", "Enter yes or no").lower()
        if try_again == "yes":
            game_is_on = True
            snake.reset_location()
        elif try_again == "no":
            break
        else:
            print(f"Invalid input: '{try_again}. Please try again.")

screen.exitonclick()
