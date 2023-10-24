import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()

    # detect with car
    for c in car.all_cars:
        if c.distance(player) < 20:
            score.game_over()
            game_is_on = False

    # detect successful crossing
    if player.finish():
        player.restart()
        car.level_up()
        score.increase()


screen.exitonclick()