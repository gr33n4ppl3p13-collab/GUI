from tkinter import *
from tkinter.ttk import *
import time
import random
SCREEN = Tk()
SCREEN.geometry("700x700")
SCREEN.config(background=("Green"))
loadingbar = Progressbar(SCREEN,orient=HORIZONTAL,length=480)
loadingbar.place(x=110,y=400)
def loading():
    global loadingbar
    loadingbar["value"]=0
    SCREEN.update_idletasks()
    while loadingbar["value"] < 100:
        loadpercent = loadingbar["value"]
        loadextra = random.randint(0,14)
        loadingbar["value"]=loadpercent + loadextra
        SCREEN.update_idletasks()
        time.sleep(0.5)
    if loadingbar["value"] > 100:
        loadingbar["value"] = 100
        SCREEN.update_idletasks()
startload = Button(SCREEN,text="Start",command=loading)
startload.place(x=310,y=350)
spinningbox = Spinbox(SCREEN,from_=0,to=100)
spinningbox.place(x=310,y=300)
mainloop()