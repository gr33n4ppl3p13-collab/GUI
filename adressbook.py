from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os

SCREEN = Tk()
SCREEN.title("Address Book")
SCREEN.geometry("720x520")
SCREEN.config(background="#d9d9d9")

Label(SCREEN, text="My Address Book", font=("Arial", 18)).place(x=20, y=12)

openbutton = Button(SCREEN, text="Open", width=12)
openbutton.place(x=470, y=12)



mainloop()
