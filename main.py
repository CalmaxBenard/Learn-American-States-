import turtle
import pandas

FONT = ("Arial", 12, "bold")
ALIGNMENT = "center"

data = pandas.read_csv("50_states.csv")

# capture all state names and convert to a list
states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=768, height=600)
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

correct_answer = []
while len(correct_answer) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answer)}/50 States Correct",
                                    prompt="What is another state's name?").title()
    # States to Learn
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in correct_answer]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # States known by user
    if answer_state in states:
        correct_answer.append(answer_state)
        entered_state = data[data.state == answer_state]
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(entered_state.x.iloc[0]), int(entered_state.y.iloc[0]))
        tim.write(answer_state, align=ALIGNMENT, font=FONT)





