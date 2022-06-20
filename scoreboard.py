from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.goto(0, 250)
        self.write(f'Level : {self.score}', align='center', font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f'Level : {self.score}', align = 'center', font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font= FONT)
