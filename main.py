import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
cars = CarManager()
screen.listen()
screen.onkeypress(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    player.level_up(score)
    cars.move(score)
    cars.restart_position()

    if cars.check_collision(player):
        score.game_over()
        game_is_on = False

screen.exitonclick()
