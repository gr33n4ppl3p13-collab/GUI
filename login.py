from tkinter import *
SCREEN = Tk()
SCREEN.title("LOGIN PAGE")
SCREEN.geometry("1000x1000")
SCREEN.config(background=("Green"))
usernamelab = Label(SCREEN,text="Username: ")
passwordlab = Label(SCREEN,text="Password: ")
usernamebox = Entry(SCREEN,width=15)
passwordbox = Entry(SCREEN,width=30,show="*")

usernamelab.place(x=10,y=10)
passwordlab.place(x=10,y=50)
usernamebox.place(x=100,y=10)
passwordbox.place(x=100,y=50)

loginbutton = Button(SCREEN,text="Log In",command=SCREEN.destroy)
loginbutton.place(x=10,y=100)
mainloop()