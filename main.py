from turtle import Screen
from player_ship import PlayerShip
import time

game_screen = Screen()
Width, Height = 650, 600
game_screen.setup(Width, Height)
game_screen.bgcolor("black")
game_screen.title("Arcade Game")
game_screen.tracer(0)

player_ship = PlayerShip()

game_screen.listen()
game_screen.onkey(player_ship.moving_left, "Left")
game_screen.onkey(player_ship.moving_right, "Right")
# game_screen.onkey(game.game_on, "Return")

game_is_on = True
while game_is_on:
    game_screen.update()

game_screen.exitonclick()
