import turtle
import pandas
from scoreboard import Scoreboard
from answer_text import AnswerText

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
img="blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
scoreboard = Scoreboard(len(data.state))
states = data.state.to_list()
guessed_states = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{scoreboard.score}/{scoreboard.max_score} States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        left_states = []
        for state in states:
            if state not in guessed_states:
                left_states.append(state)
        left_states_data = pandas.DataFrame(left_states)
        left_states_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        temp_state = data[data.state == answer_state]
        answer_text = AnswerText(temp_state)
        scoreboard.increase_score()
        if scoreboard.score == scoreboard.max_score:
            scoreboard.win_game()
            game_is_on = False




