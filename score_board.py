from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, lives, points):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.points = points
        self.lives = lives
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.points}         lives_remaining: {self.lives}", align="center", font=("Courier", 15, "normal"))

    def score_points(self, points_earned):
        self.points += points_earned
        self.update_scoreboard()

    def player_lives(self):
        self.lives -= 1
        self.update_scoreboard()
        
    def game_over(self):
        self.clear()
        self.color("#FF1E03")
        self.goto(0, 270)
        self.write(f"GameOver", align="center",
                   font=("Courier", 15, "normal"))

    #when player shoot all the enemy ships
    def win_game(self):
        self.clear()
        self.color("#13FF03")
        self.goto(0, 270)
        self.write(f"You win", align="center",
                   font=("Courier", 15, "normal"))
