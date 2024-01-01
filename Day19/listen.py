from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.color('purple')


def move_foward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_left():
    tim.left(12)
def move_right():
    tim.right(12)
def clear():
    tim.clear()
    tim.penup()
    tim.setpos(0,0)
    tim.setheading(0)

def penup():
    tim.penup()

def pendown():
    tim.pendown()




screen.listen()




screen.onkey(key="d" , fun = move_foward)
screen.onkey(key="a" , fun = move_backward)
screen.onkey(key="w" , fun = move_left)
screen.onkey(key="s" , fun = move_right)
screen.onkey(key="c" , fun = clear)
screen.onkey(key="r" , fun = pendown)
screen.onkey(key="e" , fun = penup)

screen.exitonclick()