import pyttsx3
import datetime
engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning, sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon, Sir")
    else:
        speak("Good Evening, sir")
    speak("Have a Good Day!")
if __name__ == "__main__":
    # speak("This is an assistant")
    wishMe()
