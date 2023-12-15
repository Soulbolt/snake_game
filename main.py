import time
import turtle
from turtle import Turtle, Screen

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

# Set up turtle size and color
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_size = []


# Set up sneak default position
# def rest_position():
for location in starting_positions:
    new_snake = Turtle(shape="square")
    new_snake.penup()
    new_snake.color("white")
    new_snake.goto(location)
    snake_size.append(new_snake)

snake_head = snake_size[0]


def turn_left():
    snake_head.left(90)


def turn_right():
    snake_head.right(90)


# Key bindings for movement actions

# Create a while loop to keep game going
game_is_on = True
while game_is_on:
    # Set functions and listening actions for navigation keys
    screen.listen()
    screen.onkey(turn_right, "d")
    screen.onkey(turn_left, "a")
    # Make snake move
    screen.update()  # Update animation
    time.sleep(0.1)  # delay of animation

    for segment_num in range(len(snake_size) - 1, 0, -1):
        new_x = snake_size[segment_num - 1].xcor()  # Previous snake segment coordinates
        new_y = snake_size[segment_num - 1].ycor()
        snake_size[segment_num].goto(new_x, new_y)

    if snake_head.xcor() > right_bound or snake_head.xcor() < left_bound:
        game_is_on = False
        print("You lose! You've crashed into Trumps Wall!")

    if snake_head.ycor() > top_bound or snake_head.ycor() < bottom_bound:
        game_is_on = False
        print("You lose! You've crashed into Trumps Wall!")

    snake_head.forward(20)

    if not game_is_on:
        try_again = screen.textinput("Try again?", "Enter yes or no").lower()
        if try_again == "yes":
            game_is_on = True
            snake_head.home()
        elif try_again == "no":
            break
        else:
            print(f"Invalid input: '{try_again}. Please try again.")

screen.exitonclick()
