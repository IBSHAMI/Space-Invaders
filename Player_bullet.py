from turtle import Turtle

# Bullet Y initial
Y_INITIAL = -240


class PlayerBullet(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.shape("arrow")
        self.color("#DCDCDC")
        self.penup()
        self.setheading(90)
        self.goto(x_position, Y_INITIAL)
        self.bullet_speed = 5

    def bullet_moving(self):
        self.forward(self.bullet_speed)
