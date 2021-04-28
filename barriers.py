from turtle import Turtle

# screen size
Width, Height = 650, 600


# X_WALL LIMIT
error = 80
X_WALL = (Width/2) - error


# barres spacing
X_SPACING = 120
Y_SPACING = 30


class Barriers():

    def __init__(self):
        self.barriers_list = []
        self.number_barriers = 20
        self.x = -X_WALL
        self.y = -160
        for i in range(self.number_barriers):
            self.barriers_list.append(Turtle())
            self.barriers_list[-1].shape("square")
            self.barriers_list[-1].color("#41C638")
            self.barriers_list[-1].penup()
            self.barriers_list[-1].turtlesize(1, 3)
            self.barriers_list[-1].setheading(0)
            self.barriers_list[-1].goto(self.x, self.y)
            self.x += X_SPACING
            if self.x > X_WALL:
                self.x = -X_WALL
                self.y += Y_SPACING
