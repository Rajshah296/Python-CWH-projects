from datetime import datetime
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
def speak(audio):
    """This function enables Zira to speak"""
    engine.say(audio)
    engine.runAndWait()
    pass

def wishme():
    """This function is run at startup and wishes Good Morning, Good Afternoon or Good Evening to me"""
    hour = int(datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good Morning Raj !!")
    elif hour >=12 and hour < 17 :
        speak("Good afternoon Raj !!")
    else:
        speak("Good evening Raj !!")

    speak("Hi I am Zira, How may I help you?")

def takecommand():
    """It takes microphone input from the user and returns string output."""
    r = sr.Recognizer() 
    with sr.Microphone as source:
        print("Listening")
        r.pause_threshold = 1


def main() : 
    wishme()
if __name__ == '__main__' : 
    main()