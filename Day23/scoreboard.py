from turtle import Turtle
FONT = ("Courier", 14, "bold")
FONTs = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        
        self.level = 1
        
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-260, 260)
        self.updae_scoreboad()    
    def updae_scoreboad(self):
        self.clear()
        self.write(f"level {self.level}", align= "left" , font = FONT)
        

    def increase_level (self):

        self.level += 1
        self.updae_scoreboad()

    def game_over(self):
            self.goto(0,0)
            self.write(f"Game Over At {self.level}", align= "center" , font = FONTs)

