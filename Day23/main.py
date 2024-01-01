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
level_score = Scoreboard()

screen.listen()

screen.onkeypress(player.move,"space")


game_is_on = True
while game_is_on:

    if player.ycor() > 280:
        player.won()
        level_score.increase_level()
        cars.speed_increase()

    cars.move_cars()
    for car in cars.carss:
        if car.distance(player) < 20 :
            level_score.game_over()
            game_is_on = False
    time.sleep(0.1)
    screen.update()









    
screen.exitonclick()