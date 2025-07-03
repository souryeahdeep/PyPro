from turtle import Turtle, Screen
import pandas as pd

# CONSTANTS
IMAGE = "blank_states_img.gif"
DATA_SHEET = "50_states.csv"
STATES_FOUND = "states_found.csv"

# SCREEN SETUP
screen = Screen()
tim = Turtle()
screen.addshape(IMAGE)
tim.shape(IMAGE)
screen.tracer(0)


def game_on(states_found):
    """Gameplay. Takes the states already found as a parameter, and empty list if no states have been found"""
    print(states_found)
    guessed = 0
    correct_guesses = []

    for each_state in states_found:
        correct_guesses.append(each_state)

    i = 0

    for state in correct_guesses:
        curr_state = data[data.state == state]
        tim.goto(curr_state.x.item(), curr_state.y.item())
        tim.write(state, font=("Arial", 12, "normal"))

    while len(correct_guesses) < 50:
        answer_state = screen.textinput(title=f"Guessed {len(correct_guesses)}/50",
                                        prompt="What's another state name?").title()
        if answer_state == "Exit":
            new_data = {
                "states": correct_guesses
            }
            new_data = pd.DataFrame(new_data)
            new_data.to_csv("states_to_find.csv", index=False)
            break
        curr_state = data[data.state == answer_state]
        print(curr_state)

        if curr_state.empty:
            print("Continuing")
            continue

        tim.goto(curr_state.x.item(), curr_state.y.item())
        tim.write(answer_state, font=("Arial", 12, "normal"))

        guessed += 1
        correct_guesses.append(answer_state)
        print(correct_guesses)


# READING DATA FROM DATA SHEET
data = pd.read_csv(DATA_SHEET)

# TRY TO ACCEPT THE STATES FOUND FROM THE FILE
try:
    states_found = pd.read_csv(STATES_FOUND)
    states_found = states_found['states'].tolist()

# IF THERE IS NO STATE OR NO FILE, CREATE FILE
except:
    print("Creating Account...")
    n_data = {
        "states": []
    }
    n_data = pd.DataFrame(n_data)
    n_data.to_csv(STATES_FOUND, index=False)
    states_found = []

# FINALLY CALL THE GAME
finally:
    game_on(states_found)
