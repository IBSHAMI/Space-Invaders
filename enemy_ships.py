from turtle import Turtle

# screen size
Width, Height = 650, 600

# X_WALL LIMIT
error = 80
X_WALL = (Width / 2) - error

# barres spacing
X_SPACING = 60
Y_SPACING = 50

# heading for ship movement
heading = 0

# velocity
VELOCITY = 20


class EnemyShips:

    def __init__(self):
        self.ships_list = []
        self.number_ships = 36
        self.x = -X_WALL
        self.y = 100
        self.move_heading = heading
        for i in range(self.number_ships):
            self.ships_list.append(Turtle())
            self.ships_list[-1].shape("arrow")
            self.ships_list[-1].color("#E88B0C")
            self.ships_list[-1].turtlesize(1.5, 2, 4)
            self.ships_list[-1].penup()
            self.ships_list[-1].setheading(270)
            self.ships_list[-1].goto(self.x, self.y)
            self.x += X_SPACING

            if self.x > X_WALL:
                self.x = -X_WALL
                self.y += Y_SPACING
    #
    # def enemy_ships_moving(self):
    #     if
    #     for ship in self.ships_list:
    #         ship
    #         ship.forward(VELOCITY)
    #         ship.setheading(270)
