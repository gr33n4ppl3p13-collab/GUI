from tkinter import *
from tkinter import messagebox
import random
SCREEN = Tk()
screen_width = SCREEN.winfo_screenwidth()
screen_height = SCREEN.winfo_screenheight()
windowx = int(screen_width / 1.5)
windowy = int(screen_height / 1.5)
windowsize = str(windowx) + "x" + str(windowy)
SCREEN.geometry(windowsize)
SCREEN.config(background=("Green"))

thenumber = random.randint(0, 50)
welcome = Label(SCREEN, text="Welcome, to the NUMBER GUESSING GAME!",font=("Unispace-Bold",30))
welcome.place(x=windowx / 2 - windowx / 2.1,y=windowy / 100)

def popup():
    global namentry
    namevar = namentry.get()
    messagebox.showinfo("Popup.pop-up",message="Hello, "+ str(namevar) + ", And welcome, to the AMAZING NUMBER GUESSING GAME! (DON'T YOU DARE SAY TADC IS DEAD I WILL FIND YOU)")

label_x = windowx / 2 - windowx / 2.1
label_y = windowy / 5
namelab = Label(SCREEN, text="What's your name?",font=("Unispace-Bold",12))
namelab.place(x=label_x, y=label_y)
namentry = Entry(SCREEN)
namentry.place(x=label_x + 200, y=label_y)
nameton = Button(SCREEN,text="OK",command=popup)
nameton.place(x=label_x + 350, y=label_y)



mainloop()