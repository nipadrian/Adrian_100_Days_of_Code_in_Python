import colorgram
import turtle as turtle_module
import random
from turtle import Screen


# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 45)

print(colors)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.

############ extract colors ##############

# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
turtle_module.colormode(255)

colors_list = [(249, 248, 248), (232, 241, 239), (1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165), (70, 70, 45), (185, 190, 201), (126, 225, 231), (88, 49, 45), (61, 65, 66)]
tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.speed = ("fastest")


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20,random.choice(colors_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()


# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# #hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s

