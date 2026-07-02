from tkinter import *

SCREEN = Tk()
SCREEN.geometry("700x700")
SCREEN.config(background=("Green"))
barofscrolling = Scrollbar(SCREEN)
boxoflist = Listbox(SCREEN,yscrollcommand=barofscrolling.set)
for i in range(1500):
    boxoflist.insert(END,"Pottasium particle "+str(i+1))
boxoflist.pack(side=LEFT,fill=BOTH)
barofscrolling.pack(side=RIGHT,fill=Y)
barofscrolling.config(command=boxoflist.yview)
mainloop()