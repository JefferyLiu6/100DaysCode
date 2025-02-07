from tkinter import *
WHITE =  "#FFFFFF"
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pwd_gen():
    input_3.insert(0,"123")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pwd():
    a = input_1.get()
    b = input_2.get()
    c = input_3.get()
    out = f"\n{a} | {b} | {c}"
    f = open("./Day29/output.txt", "a")
    f.write(out)
    f.close()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passwork Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file="Day29/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=1)

Website =  Label(bg="white", text="Website:", justify="center")
Website.grid(column = 0, row = 2)

EmU =  Label(bg="white", text="Email/Username:",justify="center")
EmU.grid(column = 0, row = 3)

pwd = Label(bg="white", text="Password:",justify="center")
pwd.grid(column = 0, row = 4)

input_1 = Entry(bg="white", width = 35)
input_1.grid(column=1, row=2, columnspan=2)
input_1.focus()

input_2 = Entry(bg="white", width = 35)
input_2.grid(column=1, row=3, columnspan=2)
input_2.focus()
input_2.insert(0, "abc@gmail.com")

input_3 = Entry(bg="white", width = 17)
input_3.grid(column=1, row=4, columnspan=1)
input_3.focus()

button1 = Button(bg="white", text="Generate Password", command= pwd_gen)
button1.grid(column=2, row=4, columnspan=1)

button2 = Button(bg="white", width=36, text = "Add", command= save_pwd )
button2.grid(column=1, row=5, columnspan=2)

window.mainloop()
