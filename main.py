import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
states = data.state
new_states = states.to_list()
guess_states = []

while len(guess_states) < 50:
    guess = screen.textinput(title=f"{len(guess_states)}/50 Guess the State", prompt="Enter the state")
    guess = guess.title()
    if guess == "Exit":
        missing_states = [i for i in states if i not in guess_states ]
        miss_states_csv = pandas.DataFrame(missing_states)
        miss_states_csv.to_csv("miss_states.csv")
        break
    if guess in new_states:
        guess_states.append(guess)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        p = data[data.state == guess]
        t.goto(int(p.iloc[0].x), int(p.iloc[0].y))
        t.write(guess)




