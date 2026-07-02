from tkinter import *
import calendar
SCREEN = Tk()
SCREEN.geometry("500x300")
SCREEN.config(background=("Green"))
clendar = Label(SCREEN,text="calendar",font=("Comic Sans MS",25,"bold"))
clendar.place(x=170,y=10)
entertheyear = Label(SCREEN,text="Enter the year.")
entertheyear.place(x=10,y=70)
entrytheyear = Entry(SCREEN)
entrytheyear.place(x=100,y=70)

def calender():
    global entrytheyear
    CALDISPLAY=Tk()
    CALDISPLAY.geometry("617x925")
    CALDISPLAY.config(background=("Green"))
    year = int(entrytheyear.get())
    calinfo = calendar.calendar(year)
    callabel = Label(CALDISPLAY,text=calinfo,font=("Comic Sans MS",13))
    callabel.place(x=0,y=0)

showcal = Button(SCREEN,text="Show the calendar?",command=calender)
showcal.place(x=200,y=250)

mainloop()