import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data= recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Not Understanding")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

    if sptext().lower() in "hi daniyal":
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name = "my name is daniyal"
                speechtx(name)
            elif "old are you" in data1:
                age = "I am 28 years old"
                speechtx(age)
            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "google" in data1:
                webbrowser.open("https://www.google.com/")
            elif "gmail" in data1:
                webbrowser.open("https://mail.google.com/mail/u/0/")
            elif "playlist" in data1:
                webbrowser.open("https://soundcloud.com/")
            elif "soundcloud" in data1:
                webbrowser.open("https://soundcloud.com/")
            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                speechtx(joke_1)
            elif "play song" in data1:
                add = "D:/python"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add, listsong[0]))
            elif "exit" in data1:
                speechtx("thank you")
                break
            time.sleep(20)
    else:
        print('thanks')