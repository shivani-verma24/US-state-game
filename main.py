import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

map = "blank_states_img.gif"
screen.addshape(map)  # adding a new shape so that obj can use it

turtle.shape(map)


data = pandas.read_csv("50_states.csv")

states = data.state

states_list = states.to_list()

guessed_state = []

while len(guessed_state) <50:
    user_input = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                  prompt="What's another state's name?").title()

    if user_input == "Exit":

        missed_state = [i for i in states_list if i not in guessed_state]

        missed = pandas.DataFrame(missed_state)
        missed.to_csv("Missed States")
        break

    if user_input in states_list:
        guessed_state.append(user_input)

        t = turtle.Turtle()
        t.penup()
        t.hideturtle()

        state_data = data[data.state == user_input]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_input)


# Project by Shivani Verma





