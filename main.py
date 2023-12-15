import time
from turtle import Screen
from snake import Snake

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

snakes = Snake()

# Set functions and listening actions for navigation keys
# Key bindings for movement actions
screen.listen()
screen.onkey(snakes.up, "Up")
screen.onkey(snakes.down, "Down")
screen.onkey(snakes.left, "Left")
screen.onkey(snakes.right, "Right")
# Create a while loop to keep game going
game_is_on = True
while game_is_on:
    # ran_loc = random_dots(random_x_position, random_y_position)
    # Make snake move
    screen.update()  # Update animation
    time.sleep(0.1)  # delay of animation

    snakes.move()

    if snakes.head.xcor() > right_bound or snakes.head.xcor() < left_bound:
        game_is_on = False
        print("You lose! You've crashed into Trumps Wall!")

    if snakes.head.ycor() > top_bound or snakes.head.ycor() < bottom_bound:
        game_is_on = False
        print("You lose! You've crashed into Trumps Wall!")

    # if ran_loc.pos() == snake_head.pos():
    #     ran_loc.hideturtle()
    #     ran_loc.reset()
    #     random_dots(random_x_position, random_y_position)

    if not game_is_on:
        try_again = screen.textinput("Try again?", "Enter yes or no").lower()
        if try_again == "yes":
            game_is_on = True
            snakes.reset_location()
        elif try_again == "no":
            break
        else:
            print(f"Invalid input: '{try_again}. Please try again.")

screen.exitonclick()
