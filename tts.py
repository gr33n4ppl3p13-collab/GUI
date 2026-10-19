from tkinter import *
from gtts import gTTS

SCREEN = Tk()
SCREEN.title("TTS_PROGRAM")
SCREEN.geometry("720x520")
SCREEN.config(background="#d9d9d9")

def tts():
    textt = textentry.get()
    convar = gTTS(text=textt,lang="en-us",slow=False)
    convar.save("ttsclip.ogg")


ttslable = Label(SCREEN,text="Text To Speech PROGRAM")
ttslable.place(x=10,y=10)

textlabel = Label(SCREEN, text="Enter text:")
textlabel.place(x=10,y=40)

textentry = Entry(SCREEN)
textentry.place(x=10,y=80)

submitbutton = Button(SCREEN, text="Submit",command=tts)
submitbutton.place(x=10,y=160)

mainloop()