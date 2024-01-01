import turtle as t
import random as rn # For random speed turtle will move

screen = t.Screen() 
screen.setup(width=500,height=300) # Screen size in which turtle will be shown 
user_bet =screen.textinput(title= "Enter what you want ", prompt="Use which color you want :") # ask user you to enter which turtle color they chose
colors = ["red","yellow","blue","purple","green","orange"] # Color of the Turtle

y_position = -100  # Initial y position

is_on = False 


all_turtles = [] # Empty list in which all turtle will be stored later

# main logic of all turtle appearing and color of turtle
for color in colors:
    tim = t.Turtle(shape="turtle")
    tim.penup()
    tim.color(color)
    tim.goto(x=-220, y=y_position)
    y_position += 40
    all_turtles.append(tim)

#check if the user choose any turtle or not to bet 

if user_bet:
    is_on =True

# Movement of the Turtle :
while is_on:
   
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"you won {user_bet} won dammmm")
                else:
                    print(f"loser your turtle {user_bet} loser like you  loser, Turtle {winning_color} won")

            rand_distance = rn.randint(0,10)
            # if turtle.pencolor() == user_bet:
            #     turtle.forward(2 * rand_distance)  # User's turtle moves faster
            # else:
            #     turtle.forward(rand_distance)
            turtle.forward(rand_distance)

# Exit the Screen on Click when every you want 
screen.exitonclick()
