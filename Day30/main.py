from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
#----------------------_----------------#
Data = pandas.read_csv(r"Day30\data\french_words.csv")
to_learn = Data.to_dict(orient="records")
current_Card = {}
def right_fun():
    global current_Card
    current_Card = random.choice(to_learn)
  
    canvas_main.itemconfig(card_title ,text = "French" ,)
    canvas_main.itemconfig(card_word , text =  current_Card["French"])
    Canvas.itemconfig(card_bg,image = front_side)
    window.after(3000, func= flip_card)

def flip_card():
  
    canvas_main.itemconfig(card_title ,text = "English" ,fill="white")
    canvas_main.itemconfig(card_word , text =  current_Card["English"],fill="white")
    canvas_main.itemconfig(card_bg, image =card_back)




 

#---------------------UI------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

window.after(3000, func= flip_card)

canvas_main = Canvas(height=526, width=820, bg=BACKGROUND_COLOR, highlightthickness=0)
front_side = PhotoImage(file="Day30/images/card_front.png")
card_back = PhotoImage(file= "Day30/images/card_back.png")
card_bg =canvas_main.create_image(425, 273, image=front_side)
card_title=canvas_main.create_text(420, 123, text="", fill="black", font=("arial", 35, "italic"))
card_word = canvas_main.create_text(420, 243, text="", fill="black", font=("asasa", 45, "bold"))
canvas_main.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

my_image1 = PhotoImage(file="Day30/images/wrong.png")
button1 = Button(image=my_image1, bg="white", highlightthickness=0, command=right_fun)
button1.grid(row=1, column=0, pady=10)

my_image2 = PhotoImage(file="Day30/images/right.png")
button2 = Button(image=my_image2, bg="white", highlightthickness=0, command=right_fun)
button2.grid(row=1, column=2, pady=10)
right_fun()
window.mainloop()
