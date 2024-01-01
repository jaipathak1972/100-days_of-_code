from turtle import Turtle, Screen
import turtle as t
import random

tim = Turtle()
tim.speed(500)
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour= (r,g,b)
    return colour
def gap(space):
    
    for i in range(int(360 / space)):
    
        r = 100
        tim.circle(r)
        
        tim.left(space)
        tim.color(random_color())
gap(2)
    











screen =Screen()
screen.exitonclick()