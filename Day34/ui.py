THEME_COLOR = "#375362"
from  tkinter import *
from quiz_brain import QuizBrain


class Interface():
    def __init__(self , quiz_brain : QuizBrain) -> None:
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzller")
        self.window.config( padx= 20 ,pady= 20 , bg= "blue")
        # self.lable1.config(text=f"Score : {self.quiz.score}" )
        self.lable1 = Label(text= "Score: 0", bg= "blue", fg= "white", font=("arial", 13, "bold"))
        self.lable1.grid(row=0,column=1,pady=30)


        self.canvas = Canvas(self.window, width=350, height=300, bg="white")
        self.question_text = self.canvas.create_text(175, 150, text= "heloo jai how are you ?", font=("arial", 20, "bold"), width=320)
        self.canvas.grid(row=1, column=0, columnspan=2 , padx=20,pady=50) 
        
        self.img1 = PhotoImage(file="Day34/images/false.png")
        self.button_false = Button(image= self.img1, bg= "blue", command= self.false_pressed)

        self.button_false.grid(row=2 , column=0) 
        self.img2 = PhotoImage(file="Day34/images/true.png")
        self.button_true = Button(image= self.img2, bg= "blue", command=self.true_pressed) 
        self.button_true.grid(row=2 , column=1) 

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg = "white")
        q_text =self.quiz.next_question()
        self.canvas.itemconfig(self.question_text , text = q_text)    
    
    def true_pressed(self):
        is_right =self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self , is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_question)