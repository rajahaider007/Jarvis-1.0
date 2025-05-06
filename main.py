import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150) 

def speak(command):
    engine.say(command)
    engine.runAndWait()
speak("How are you ?")