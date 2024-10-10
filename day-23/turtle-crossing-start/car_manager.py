from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1,2)
            random_color = random.randint(0,5)
            random_y_position = random.randint(-250,250)
            new_car.color(COLORS[random_color])
            new_car.goto(300,random_y_position)
            self.all_cars.append(new_car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)
            # new_x = self.xcor() - STARTING_MOVE_DISTANCE
            # new_y = self.ycor()
            # car.goto(new_x,new_y)





