from tkinter import *
SCREEN = Tk()
SCREEN.geometry("500x500")
SCREEN.config(background=("Green"))
enterlab = Label(SCREEN,text="Enter the weight in KG")
enterbox = Entry(SCREEN,width=10)

def Convert():
    global enterbox
    grams = float(enterbox.get())*1000
    pounds = float(enterbox.get())*2.20462
    ounce = float(enterbox.get())*35.274
    gramtext.delete("1.0",END)
    poundtext.delete("1.0",END)
    ouncetext.delete("1.0",END)
    gramtext.insert(END,grams)
    poundtext.insert(END,pounds)
    ouncetext.insert(END,ounce)

convertbutton = Button(SCREEN,text="Convert",command=Convert)
gramlab = Label(SCREEN,text="Gram")
Poundslab = Label(SCREEN,text="Pounds")
ouncelab = Label(SCREEN,text="Ounce")
gramtext = Text(SCREEN,width=100,height=50)
poundtext = Text(SCREEN,width=100,height=50)
ouncetext = Text(SCREEN,width=100,height=50)

enterlab.place(x=10,y=10)
enterbox.place(x=250,y=10)
convertbutton.place(x=400,y=10)
gramlab.place(x=00,y=100)
Poundslab.place(x=150,y=100)
ouncelab.place(x=300,y=100)
gramtext.place(x=0,y=150)
poundtext.place(x=150,y=150)
ouncetext.place(x=300,y=150)

mainloop()