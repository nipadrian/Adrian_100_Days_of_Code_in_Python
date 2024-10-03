from turtle import Turtle
import random
from turtle import Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")


# for _ in range(50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

############### shapes challenge 3 ###################

# also need different color for different line
# start count from 3
# while count < 10
# calculate angle
# draw shape
# increase count

# def random_color():
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     return (r,g,b)
#
# sides = 3
# while sides < 10:
#     tim.color(random_color())
#     angle = 360/sides
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)
#     sides += 1

################### challenge 4 #########################

# choose random direction of north, south, east, west
# choose random amount of steps
# random colors

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r,g,b)
#
# def random_direction():
#     list = [90, 180, 270, 360]
#     random_angle = random.choice(list)
#     return random_angle
#
# def random_steps():
#     n = random.randint(0,100)
#     return n
#
# steps = 0
# tim.pensize(15)
# tim.speed("fastest")
#
# while steps < 200:
#     tim.color(random_color())
#     tim.right(random_direction())
#     tim.forward(random_steps())
#     steps += 1
#

######### color mode #######
#Turtle.colormode(255)

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r, g, b)
#     return random_color


############################

########################## challenge 5 spirograph ########################
tim.speed("fastest")

angle = 360/ 30

# while angle < 360:
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(angle)
#     angle += angle

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)





screen = Screen()
screen.exitonclick()
