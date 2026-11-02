from tkinter import *
import speech_recognition as sr

SCREEN = Tk()
SCREEN.title("TTS_PROGRAM")
SCREEN.geometry("700x400")
SCREEN.config(background="#d9d9d9")

def speechtotext():
    speech = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech.listen(source)
        try:
            text = speech.recognize_google(audio)
        except:
            text = "The Speech Recognizer Couldn't Recognize your Speech! Try Using A Different Microphone."
        speechbox.delete(1.0,END)
        speechbox.insert(END,text)

startbutton = Button(SCREEN,text="Start Recording 🔴",command=speechtotext)
startbutton.pack(side=LEFT)

speechbox = Text(SCREEN,width=300,height=300)
speechbox.pack(side=LEFT)

mainloop()