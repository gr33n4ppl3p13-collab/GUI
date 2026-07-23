from tkinter import *
import tkinter.font
import random
SCREEN = Tk()
SCREEN.geometry("500x300")
SCREEN.config(background=("Green"))
playerscore = 0
npcscore = 0
options = [("Rock",0),("Paper",1),("Scissors",2)]

def npcwin():
    global npcscore, playerscore
    npcscore += 1 
    winning.config(text="Computer won.")
    npcscorelab.config(text="Computer Score: "+str(npcscore))
    mescorelab.config(text="Your score: "+str(playerscore))

def mewin():
    global npcscore, playerscore
    playerscore += 1 
    winning.config(text="You won.")
    npcscorelab.config(text="Computer Score: "+str(npcscore))
    mescorelab.config(text="Your score: "+str(playerscore))

def tie():
    global npcscore, playerscore
    winning.config(text="C'est a le Tie.")
    npcscorelab.config(text="Computer Score: "+str(npcscore))
    mescorelab.config(text="Your score: "+str(playerscore))

def npcthoughts():
    global options
    return random.choice(options)

def mychoice(input):
    global npcscore, playerscore
    npcchoice = npcthoughts()
    meselectlab.config(text="You Selected: "+input[0])
    npcselectlab.config(text="Computer Selected: "+npcchoice[0])
    if input==npcchoice:
        tie()
    if input[1]==0:
        if npcchoice[1]==1:
            npcwin()
        elif npcchoice[1]==2:
            mewin()
    if input[1]==1:
        if npcchoice[1]==0:
            mewin()
        if npcchoice[1]==2:
            npcwin()
    if input[1]==2:
        if npcchoice[1]==0:
            npcwin()
        if npcchoice[1]==1:
            mewin()

rps = Label(SCREEN,text="Rock Paper Scissors")
rps.place(x=200,y=10)
winning = Label(SCREEN,text="Let's Start the game.")
winning.place(x=200,y=50)
optionsl = Label(SCREEN,text="Your options")
optionsl.place(x=200,y=80)
rock = Button(SCREEN,text="rock",font=("Comic Sans MS",30),command=lambda:mychoice(options[0]))
paper  = Button(SCREEN,text="paper",font=("Comic Sans MS",30),command=lambda:mychoice(options[1]))
scissors = Button(SCREEN,text="scissors",font=("Comic Sans MS",30),command=lambda:mychoice(options[2]))
rock.place(x=10,y=120)
paper.place(x=150,y=120)
scissors.place(x=320,y=120)
scorelabel = Label(SCREEN,text="Score = ",font=("Comic Sans MS",18))
scorelabel.place(x= 10,y=230)
mescorelab = Label(SCREEN,text="Your score: ")
mescorelab.place(x=120,y=220)
npcscorelab = Label(SCREEN,text="Computer score: ")
npcscorelab.place(x=120,y=260)
meselectlab = Label(SCREEN,text="You Selected: ")
meselectlab.place(x=300,y=220)
npcselectlab = Label(SCREEN,text="Computer Selected: ")
npcselectlab.place(x=300,y=260)
mainloop()