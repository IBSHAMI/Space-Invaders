from turtle import Screen
from player_ship import PlayerShip
from Player_bullet import PlayerBullet
from barriers import Barriers
from enemy_ships import EnemyShips
from enemy_bullet import EnemyBullet
from random import randint
from score_board import Scoreboard
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
    if len(player_bullets) < 6:
        player_bullets.append(PlayerBullet(player_ship_x_position))
    else:
        pass


def shot_bullet_enemy(enemy_ships, number_bullets):
    global enemy_bullets, enemy_x_position, enemy_y_position
    for i in range(number_bullets):
        try:
            index_ship_to_shoot = randint(0, 9)
            enemy_x_position = enemy_ships[index_ship_to_shoot].xcor()
            enemy_y_position = enemy_ships[index_ship_to_shoot].ycor()
            enemy_bullets.append(EnemyBullet(enemy_x_position, enemy_y_position))
        except IndexError:
            pass


game_screen.listen()
game_screen.onkey(player_ship.moving_left, "Left")
game_screen.onkey(player_ship.moving_right, "Right")
game_screen.onkey(shot_bullet_player, "Return")

# Timer for ships movement, game diffucilty and number of enemy bullets
timer = time.time()
difference = 2
timer_game_difficulty_increase = time.time()
difference_to_increase_difficulty = 25
number_bullets = 2
number_ships_left_to_increase_diff = 18


# Enemy ships movement control variables
index_movement = 0
enemy_movement = [10, 10, -10, -10,
                  -10, -10, 10, 10]

# player lives
lives = 3
points = 0
score = Scoreboard(lives, points)

game_is_on = True
while game_is_on:
    time.sleep(0.02)
    game_screen.update()
    player_ship_x_position = player_ship.xcor()

    # check if player bullet reach end of screen and delete them if so
    for bullet in player_bullets:
        if bullet.ycor() >= Y_WALL:
            player_bullets.remove(bullet)
        else:
            bullet.bullet_moving()



    # shoot enemy bullets and move the ships
    if (time.time() - timer) > difference:
        if number_bullets >= len(enemy.ships_list):
            number_bullets = len(enemy.ships_list)
        shot_bullet_enemy(enemy.ships_list, number_bullets)
        enemy.moving(enemy_movement[index_movement])
        if index_movement == 7:
            index_movement = 0
        else:
            index_movement += 1
        timer = time.time()


    # enemy bullet reach the end of the screen
    if len(enemy_bullets) != 0:
        for bullet in enemy_bullets:
            if bullet.ycor() <= -Y_WALL:
                enemy_bullets.remove(bullet)
            else:
                bullet.bullet_moving()

    # collision of any bullet with the barriers 
    for barrier in barriers.barriers_list:
        for bullet in player_bullets:
            if barrier.distance(bullet) < 30:
                barrier.reset()
                barriers.barriers_list.remove(barrier)
                bullet.reset()
                player_bullets.remove(bullet)

        for bullet in enemy_bullets:
            if barrier.distance(bullet) < 30:
                barrier.reset()
                try:
                    barriers.barriers_list.remove(barrier)
                except ValueError:
                    continue
                bullet.reset()
                enemy_bullets.remove(bullet)

    # collision of player bullet with the enemy
    for enemy_ship in enemy.ships_list:
        for bullet in player_bullets:
            if enemy_ship.distance(bullet) < 20:
                bullet.reset()
                player_bullets.remove(bullet)
                enemy_ship.reset()
                try:
                    enemy.ships_list.remove(enemy_ship)
                except ValueError:
                    score.score_points(points_earned= 5)
                    score.win_game()

    # Enemy hit player ship
    for bullet in enemy_bullets:
        if bullet.distance(player_ship) < 30:
            bullet.reset()
            enemy_bullets.remove(bullet)
            if score.lives == 0:
                score.game_over()
                game_is_on = False
            else:
                score.player_lives()

    # Increase game difficulty
    if (time.time() - timer_game_difficulty_increase) > difference_to_increase_difficulty or len(enemy.ships_list) < number_ships_left_to_increase_diff:
        if difference >= 1:
            difference *= 0.75
        if number_bullets <= 8:
            number_bullets *= 2
        print(number_bullets)
        timer_game_difficulty_increase = time.time()
        number_ships_left_to_increase_diff *= 0.5


    # game win
    if len(enemy.ships_list) == 0:
        score.win_game()
        game_is_on= False

game_screen.exitonclick()
