import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create turtle or player, starting position, player control turtle to move up
player = Player()

screen.listen()
screen.onkey(player.move, "Up")

# generate cars that are 20px by 40 px, randomly generated on y axis, move from right to left, none in to 50 and bottom 50
car_manager = CarManager()

# detect when car hits turtle - game over

# once reach edge, scoreboard increase and car speed increase

scoreboard = Scoreboard()


loop = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_car()


    # detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()

            game_is_on = False

    if player.is_at_finish_line():
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.update_level()

screen.exitonclick()