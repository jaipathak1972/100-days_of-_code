from turtle import Turtle, Screen
from Two_paddle import Paddle
from ball import Ball 
import time
from player_score import Score_board

screen = Screen()
screen.bgcolor("black")
screen.title("JAI's Ping Pong")
screen.setup(height= 600 ,  width= 800)
screen.tracer(0)

r_paddle =Paddle((370,0))
l_paddle =Paddle((-370,0))

screen.listen()
screen.onkeypress(r_paddle.upward,"Up")
screen.onkeypress(r_paddle.downward,"Down")
screen.onkeypress(l_paddle.upward,"w")
screen.onkeypress(l_paddle.downward,"s")

ball = Ball()
score = Score_board()
score.mid_line()

game_is_on = True
while game_is_on:
    
    time.sleep(0.08)
    ball.bounce()
    screen.update( )

    if  ball.ycor() < -260 or ball.ycor() > 280:
        ball.bouce_back()
        
    if ball.distance(r_paddle) < 70 and ball.xcor() == 350:
        ball.paddle_bounce()
        
    if ball.distance(l_paddle) < 70 and ball.xcor() == -350:
        ball.paddle_bounce()
    
    if ball.xcor() > 370 :
        score.l_point()
        ball.reset_position()
        
    if ball.xcor() < -370 :
        score.r_point()
        ball.reset_position()

    





   








screen.exitonclick()
