import tkinter
import random

window = tkinter.Tk()
window.title("MY First GUI Program")
window.minsize(width=500  , height=300)


#lable
equal = tkinter.Label(text="IS EQUAL TO", font= ("Arial", 10,"bold"))
equal.grid(row=1,column=0)
zero = tkinter.Label(text="0", font= ("Arial", 10,"bold"))
zero.grid(row=1,column=1)
kilo = tkinter.Label(text="Km", font= ("Arial", 10,"bold"))
kilo.grid(row=1,column=2)
kilo = tkinter.Label(text="Miles", font= ("Arial",10,"bold"))
kilo.grid(row=0,column=2)



#entry

zero_entry=tkinter.Entry( width=8)
zero_entry.grid(row=0,column=1, )

def button_clicked():
    miles = int(zero_entry.get())
    kilometter = miles*1.689
    kilo.config(text=f"{kilometter}km")
#button 

button = tkinter.Button(text="Calculate",width=10,command= button_clicked)
button.grid(column=1,row=2)


window.mainloop()