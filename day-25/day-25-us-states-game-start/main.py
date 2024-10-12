import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# answer_state = screen.textinput(title = "Guess the State", prompt = "What's another state's name?")
# # 1. convert the guess to Title case
# answer_state = answer_state.capitalize()


data = pandas.read_csv("50_states.csv")
print(data)
all_states = data.state.to_list()

texas = (data[data.state == "Texas"])
#print(texas)
#print(texas.x[0])
user_guess = True
guessed_states = []

while len(guessed_states) <50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 Guess the State", prompt = "What's another state's name?")
    answer_state = answer_state.title()
# 2. check if guess is among 50 states
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # #create dataframe from scratch
        data_dict = {
            "Missing_States": missing_states
        }

        data = pandas.DataFrame(data_dict)
        data.to_csv("Missing_States.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(float(state_data.x.item()),float(state_data.y.item()))
        t.write(answer_state)



        # correct_state = turtle.Turtle()
        # state_x = data[data[state] == answer_state]
        # correct_state.position()
        # correct_state.write(f""

#    turtle.write(answer_state,False,"center",("Arial",8,"normal"))


# 3. write correct guesses onto map
# 4. use loop to allow user to keep guessing
# 5. record correct guesses in a list
# 6. keep track of score


screen.exitonclick()