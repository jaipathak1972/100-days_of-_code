import turtle as t
import random
from turtle import Screen

colors = [(245, 238, 238), (246, 244, 244), (202, 110, 110), (240, 241, 241), (236, 243, 243), (149, 50, 50), (222, 136, 136), (53, 123, 123), (170, 41, 41), (138, 20, 20), (134, 184, 184), (197, 73, 73), (47, 86, 86), (73, 35, 35), (145, 149, 149), (14, 70, 70), (232, 165, 165), (160, 158, 158), (54, 50, 50), (101, 77, 77), (183, 171, 171), (36, 74, 74), (19, 89, 89), (82, 129, 129), (147, 19, 19), (27, 102, 102), (12, 64, 64), (107, 153, 153), (176, 208, 208), (168, 102, 102)]

tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed('fastest')
position = tim.setpos(-200, -200)
t.colormode(255)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    random_color = random.choice(colors)  # Get a different color for each dot

    tim.dot(20, random_color)
    tim.penup()
    tim.forward(50)
    tim.pendown()
    if dot_count % 10 == 0:
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)  # Adjusted forward distance for the next row
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
