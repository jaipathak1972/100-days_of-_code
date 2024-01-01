from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None
input_text = []  # Create an empty string to store input text



# ---------------------------- TIMER RESET ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="LBreak", fg=PINK)
       

    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="SBreak", fg="Orange")
        
    else:
        count_down(work_sec)
        label.config(text="Work", fg=RED)
        store_input_text()  # Call the function to store input text
        print(input_text)

# Function to store input text in the list
def store_input_text():
    global input_text
    text = input_box.get("1.0", "end-1c")  # Get text from the Text widget
    input_text.append(text)  # Append the text to the list
    input_box.delete("1.0", "end")  # Clear the Text widget

    message = "This is what I have done in 25 min work :"
    with open("Day28/Daily_data.txt", mode="a", encoding="utf-8") as datafile:
        datafile.write(message + '\n')  # Write the message followed by a newline
        datafile.write(text +'\n' '\n')  # Write the input text followed by a newline

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps // 2):
            mark += "✓"
        label_tick.config(text=mark)

        # Bring the window to the front and maximize it during breaks
        if reps % 2 == 0:
            window.deiconify()
            window.lift()

# ---------------------------- RESET FUNCTION ------------------------------- #
def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
    label_tick.config(text="")
    store_input_text()
    print(input_text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
label.grid(row=0, column=1)

label_tick = Label(text="", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
label_tick.grid(row=4, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
apple_image = PhotoImage(file="Day28/tomato.png")  # Replace with your image file
canvas.create_image(100, 112, image=apple_image)
timer_text = canvas.create_text(100, 128, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

# Multiline input box to type something during breaks
input_box = Text(width=20, height=6 )
input_box.grid(row=3, column=1)


# Buttons
start_button = Button(text="Start", width=10, background=RED, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", width=10, background=RED, command=reset)
reset_button.grid(row=2, column=2)


window.mainloop()
