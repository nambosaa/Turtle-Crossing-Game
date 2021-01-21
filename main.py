import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()


def hit():
    for car in cars.all_cars:
        if player.distance(car) < 25:
            return True


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    screen.listen()
    screen.onkeypress(player.move, "Up")

    if hit():
        score.game_over()
        game_is_on = False

    if player.distance(score) < 20:
        score.update_score()
        cars.level_up()
        player.goto(0, -280)

screen.exitonclick()
