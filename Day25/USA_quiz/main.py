import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"Day25\USA_quiz\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

Data = pd.read_csv(r"Day25\USA_quiz\50_states.csv")

correct_guess = 0
total_state = 50

guessed_state = []
inccort = 0

all_state = Data["state"].to_list()



while correct_guess < total_state:

    answer_state = screen.textinput(title=f"Guess the State {correct_guess}/{total_state} ", prompt="What's another state's name? ").title()
    print(answer_state)


    state_data = Data[Data.state == answer_state]
    
    if answer_state== "Exit":
            mising_state = [state for state in all_state if state not in guessed_state ]
            New_data = pd.DataFrame(mising_state)
            New_data.to_csv("new_csv_data.csv")
            tim = turtle.Turtle()
            tim.goto(0,0)
            tim.penup()
            tim.hideturtle()
            tim.write("Game_over", align="center", font=("Arial", 42, "normal"))

            break


    if not state_data.empty:
        x = int(state_data.iloc[0]["x"])
        y = int(state_data.iloc[0]["y"])
        tim=turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        tim.goto(x, y)
        tim.write(answer_state, align="center", font=("Arial", 8, "normal"))
        correct_guess += 1
        guessed_state.append(answer_state)

    
    else:
        inccort += 1

        print("State not found in the dataset.")
     
        if inccort == 3:
            tim = turtle.Turtle()
            tim.goto(0,0)
            tim.penup()
            tim.hideturtle()
            tim.write("Game_over", align="center", font=("Arial", 42, "normal"))

            break

# # print(guessed_state)
turtle.exitonclick()



