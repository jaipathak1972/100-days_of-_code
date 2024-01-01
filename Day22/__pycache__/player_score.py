from turtle import Turtle


class Score_board(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score= 0 
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto (-100 , 200)
        self.write(self.l_score , align= "center" , font=("courier", 50, "normal"))
        
        self.goto (100 , 200)
        self.write(self.r_score , align= "center" , font=("courier", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()
    def r_point(self):
        self.r_score += 1
        self.update_score()
    
    def mid_line(self):
        
        self.goto(0 , 400)
        self.setheading(270)
        self.hideturtle()
        self.color("white")
        self.width(0.5)

        for i  in range(20):
            self.forward(30)
            self.penup()
            self.forward(10)
            self.pendown()  
        self.update_score()      