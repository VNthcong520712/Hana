import os
from gtts import gTTS
import playsound
import pyttsx3

eng = pyttsx3.init()
voi = eng.getProperty("voices")
eng.setProperty("voice",voi[1].id)

def offline(text):
    eng.say(text)
    eng.runAndWait()

def doc(text):
    out = gTTS(text, lang="vi")
    print(out)
    out.save("out.mp3")
    playsound.playsound("out.mp3")
    os.remove("out.mp3")


if __name__ == "__main__":
    doc("hana xin chào")
    offline("xin chào")