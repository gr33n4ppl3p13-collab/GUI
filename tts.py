from tkinter import *
from gtts import gTTS

speech = gTTS(text="Hello", lang="en")
speech.save("ttsclip.mp3")