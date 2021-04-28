from turtle import Screen
from player_ship import PlayerShip
from Player_bullet import PlayerBullet
import time



player_bullets = []
player_ship_x_position = None
game_screen = Screen()
Width, Height = 650, 600
game_screen.setup(Width, Height)
game_screen.bgcolor("black")
game_screen.title("Arcade Game")
game_screen.tracer(0)

player_ship = PlayerShip()


def shot_bullet_player():
    global player_bullets, player_ship_x_position
    print(player_ship_x_position)
    player_bullets.append(PlayerBullet(player_ship_x_position))



game_screen.listen()
game_screen.onkey(player_ship.moving_left, "Left")
game_screen.onkey(player_ship.moving_right, "Right")
game_screen.onkey(shot_bullet_player, "Return")

game_is_on = True
while game_is_on:
    time.sleep(0.02)
    game_screen.update()
    player_ship_x_position = player_ship.xcor()
    for bullet in player_bullets:
        bullet.bullet_moving()


game_screen.exitonclick()
