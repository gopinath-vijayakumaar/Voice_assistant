from importlib.resources import path
import pyttsx3
import speech_recognition as sr
import webbrowser
import time

def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print(Query)
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
    return Query
    
def Speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def chrome():
    url= 'https://www.youtube.com/'
    webbrowser.open_new(url)


if __name__ == '__main__':
    while True:
        command = take_commands()
        if "stop" in command:
            Speak("Sure sir! as your wish, bai")
            break
        if "Chrome" in command:
            Speak("Opening sir")
            chrome()
