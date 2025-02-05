from tkinter import *

def button_clicked():
    gg = mile.get()
    km = int(gg)*1.609344
    my_label.config(text=str(km))


window = Tk()
window.title("Mile to KM Converter")
window.minsize(height = 20, width = 20)

my_label = Label(text = "0")
my_label.grid(column= 1, row =1 )

is_eq = Label(text = "is equal to")
is_eq.grid(row= 1,column=0)
mile = Label(text= "mile")
mile.grid(column=2, row=0)

km = Label(text = "km")
km.grid(column=2, row= 1)

button = Button(text = "convert", command = button_clicked)
button.grid(column= 1, row = 2)

mile = Entry()
mile.grid(column= 1, row =0 )

window.mainloop()