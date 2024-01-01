from turtle import Turtle , Screen

class Score(Turtle):
    def __init__(self) -> None:
            

        super().__init__()
        self.clear()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(-50, 260)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='left', font=('Arial', 15, 'normal'))
    
    def increase_Score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='left', font=('Arial', 15, 'normal'))


    def reset(self):
        if self.score > self.high_score:
            self.high_score= self.score
        self.score = 0
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align='left', font=('Arial', 15, 'normal'))


    # def game_over(self):
    #     self.goto(-50,0)
    #     self.write("GAME OVER" , align="left" ,font=('Arial', 15, 'normal') )
   


