from turtle import Turtle

class Paddle(Turtle):
    def __init__(self , position) -> None:
        super().__init__()
        
        self.paddle = Turtle()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid= 4,  stretch_len= 0.8)
        self.goto(position)
    
    def upward(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
        
    def downward(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

            