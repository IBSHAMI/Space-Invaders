from turtle import Turtle


class EnemyBullet(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("arrow")
        self.color("#A46919")
        self.penup()
        self.setheading(270)
        self.goto(x_position, y_position +5 )
        self.bullet_speed = 5

    def bullet_moving(self):
        self.forward(self.bullet_speed)
