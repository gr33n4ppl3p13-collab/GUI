from tkinter import *

SCREEN = Tk()
SCREEN.geometry("500x200")
SCREEN.config(background="Red")

enterlab = Label(SCREEN, text="Enter the temperature in °C")
enterbox = Entry(SCREEN, width=10)


def Convert():
    global enterbox
    fahrenheit = float(enterbox.get()) * 9 / 5 + 32
    outputtext.delete("1.0", END)
    outputtext.insert(END, fahrenheit)


convertbutton = Button(SCREEN, text="Convert", command=Convert)
outputlab = Label(SCREEN, text="Fahrenheit")
outputtext = Text(SCREEN, width=100, height=50)

enterlab.place(x=10, y=10)
enterbox.place(x=250, y=10)
convertbutton.place(x=400, y=10)
outputlab.place(x=10, y=100)
outputtext.place(x=10, y=150)

mainloop()