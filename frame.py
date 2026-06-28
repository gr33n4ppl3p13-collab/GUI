from tkinter import *
from playsound3 import playsound
SCREEN = Tk()
SCREEN.geometry("1000x1000")
SCREEN.config(background=("Green"))
frame = Frame(SCREEN,width=200,height=200)
frame.place(x=300,y=300)
def play():
    playsound("i-am-steve.mp3")
button1 = Button(frame,text="This. Is a Button.",command=play)
button1.place(x=10,y=10)

mainloop()