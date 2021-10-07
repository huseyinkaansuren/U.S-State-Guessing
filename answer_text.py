from turtle import Turtle

class AnswerText(Turtle):
    def __init__(self,state):
        super().__init__()
        self.hideturtle()
        self.penup()
        x_cor = int(state.x)
        y_cor = int(state.y)
        state_name = str(state.state.item())
        self.goto(x_cor, y_cor)
        self.write(state_name)