from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self, data_len):
        super().__init__()
        self.score = 0
        self.max_score = data_len

    def increase_score(self):
        self.score += 1

    def win_game(self):
        self.write("You Guessed All The States",False, align="center", font=("Arial",24,"normal"))