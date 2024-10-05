from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title = "Make your bet,", prompt = "Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "blue", "green", "black", "yellow"]

y = (-70,-40,-10,20,50,80)
all_turtles = []


for turtle_index in range(0,6):
    new_turtle= Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y[turtle_index])

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        distance = random.randint(0,10)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_coloer == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")




# how to I do it for all turtle at the same time? how do i access a single turtle?
# need to make all turtles move
# move at different random speeds
# reach the end or position at the end

# find winner
# if winner matches the turtle user chose, then user wins





screen.exitonclick()
















################# Etch and Sketch ####################

# red = Turtle()
# screen = Screen()
#
# def move_forward():
#     red.forward(10)
#
# def move_backward():
#     red.backward(10)
#
# def clockwise():
#     red.right(10)
#
# def counterclockwise():
#     red.left(10)
#
# def clearscreen():
#     red.clear()
#     red.reset()
#
# screen.listen()
# screen.onkey(key = "w", fun = move_forward)
# screen.onkey(key = "s", fun = move_backward)
# screen.onkey(key = "d", fun = clockwise)
# screen.onkey(key = "a", fun = counterclockwise)
# screen.onkey(key = "c", fun = clearscreen)
# screen.exitonclick()

################# Etch and Sketch ####################

