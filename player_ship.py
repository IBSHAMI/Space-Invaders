from turtle import Turtle

# screen size
Width, Height = 650, 600

# walls on X axes
error = 50
X_WALL_LIMIT = (Width/2) - error

# ship heading
heading = 90

# ship initial positions
X_INITIAL, Y_INITIAL = 0, -260

# Velocity
VELOCITY = 20


class PlayerShip(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("arrow")
        self.color("#3865C6")
        self.penup()
        self.setheading(heading)
        self.turtlesize(4, 1, 10)
        self.goto(X_INITIAL, Y_INITIAL)

    def moving_right(self):
        if self.xcor() >= X_WALL_LIMIT:
            pass
        else:
            self.right(90)
            self.forward(VELOCITY)
            self.setheading(heading)

    def moving_left(self):
        if self.xcor() <= -X_WALL_LIMIT:
            pass
        else:
            self.left(90)
            self.forward(VELOCITY)
            self.setheading(heading)
