from tkinter import *
import time
SCREEN = Tk()
SCREEN.geometry("140x30")
SCREEN.config(background=("Green"))

def displaytime():
    global timelab
    timetime = time.strftime("%H:%M:%S %p")
    timelab.config(text=timetime)
    timelab.after(1000,displaytime)

timelab = Label(SCREEN,text="",font=("Comic Sans MS",10))
timelab.place(x=5,y=5)
displaytime()

mainloop()