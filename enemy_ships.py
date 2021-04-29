from turtle import Turtle
from random import randint, choice

# screen size
Width, Height = 650, 600

# X_WALL LIMIT
error = 80
X_WALL = (Width / 2) - error
X_WALL_MOVING = (Width / 2) - 30
Y_WALL_MOVING = (Height / 2) - 30

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
        self.ships_negative_wall_edges = []
        self.ships_positive_wall_edges = []
        self.number_ships = 36
        self.x = -X_WALL
        self.y = 100
        self.move_heading = heading
        self.x_move = 0
        self.y_move = 0
        for i in range(self.number_ships):
            self.ships_list.append(Turtle())
            self.ships_list[-1].shape("arrow")
            self.ships_list[-1].color("#E88B0C")
            self.ships_list[-1].turtlesize(1.5, 2, 4)
            self.ships_list[-1].penup()
            self.ships_list[-1].setheading(270)
            self.ships_list[-1].goto(self.x, self.y)

            if self.x == -X_WALL:
                self.ships_negative_wall_edges.append(self.ships_list[-1])

            self.x += X_SPACING

            if self.x > X_WALL:
                self.x = -X_WALL
                self.y += Y_SPACING
                self.ships_positive_wall_edges.append(self.ships_list[-1])

    def moving(self, movement_distance):
        print(movement_distance)
        for ship in self.ships_list:
            ship.setheading(0)
            ship.forward(movement_distance)
            ship.setheading(270)


