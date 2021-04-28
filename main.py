from turtle import Screen
from player_ship import PlayerShip
from Player_bullet import PlayerBullet
from barriers import Barriers
from enemy_ships import EnemyShips
from enemy_bullet import EnemyBullet
from random import randint
import time

player_bullets = []
enemy_bullets = []
player_ship_x_position = None
enemy_y_position = None
enemy_x_position = None
game_screen = Screen()
Width, Height = 650, 600
game_screen.setup(Width, Height)
game_screen.bgcolor("black")
game_screen.title("Arcade Game")
game_screen.tracer(0)

# Y wall limit
Y_WALL = 300

player_ship = PlayerShip()
barriers = Barriers()
enemy = EnemyShips()


def shot_bullet_player():
    global player_bullets, player_ship_x_position
    if len(player_bullets) < 5:
        player_bullets.append(PlayerBullet(player_ship_x_position))
    else:
        pass


def shot_bullet_enemy(enemy_ships):
    global enemy_bullets, enemy_x_position, enemy_y_position
    for i in range(3):
        index_ship_to_shoot = randint(0,9)
        enemy_x_position = enemy_ships[index_ship_to_shoot].xcor()
        enemy_y_position = enemy_ships[index_ship_to_shoot].ycor()
        enemy_bullets.append(EnemyBullet(enemy_x_position, enemy_y_position))




game_screen.listen()
game_screen.onkey(player_ship.moving_left, "Left")
game_screen.onkey(player_ship.moving_right, "Right")
game_screen.onkey(shot_bullet_player, "Return")


# Timer for ships movement
timer = time.time()
difference = 5

# heading for

game_is_on = True
while game_is_on:
    time.sleep(0.02)
    game_screen.update()
    player_ship_x_position = player_ship.xcor()
    for bullet in player_bullets:
        if bullet.ycor() >= Y_WALL:
            player_bullets.remove(bullet)
        else:
            bullet.bullet_moving()

    if (time.time() - timer) > difference:
        shot_bullet_enemy(enemy.ships_list)
        timer = time.time()

    if len(enemy_bullets) != 0:
        for bullet in enemy_bullets:
            if bullet.ycor() <= -Y_WALL:
                enemy_bullets.remove(bullet)
            else:
                bullet.bullet_moving()
                
    # collision of any bullet with the barriers 
    for barrier in barriers.barriers_list:
        for bullet in player_bullets:
            if barrier.distance(bullet) < 10:
                barrier.reset()
                barriers.barriers_list.remove(barrier)
                bullet.reset()
                player_bullets.remove(bullet)

        for bullet in enemy_bullets:
            if barrier.distance(bullet) < 10:
                barrier.reset()
                barriers.barriers_list.remove(barrier)
                bullet.reset()
                enemy_bullets.remove(bullet)

    # collision of player bullet with the enemy
    for enemy_ship in enemy.ships_list:
        for bullet in player_bullets:
            if enemy_ship.distance(bullet) < 20:
                bullet.reset()
                player_bullets.remove(bullet)
                enemy_ship.reset()
                enemy.ships_list.remove(enemy_ship)


game_screen.exitonclick()
