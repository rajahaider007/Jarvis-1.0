import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# speak("How are you ?")


def commmand():
    content = " "
    while content == " ":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        try:
            content = r.recognize_google(audio, language="en-in")
            print("You Said........... " + content)
        except Exception as e:
            print("Please try again... ")

        return content


while True:
    request = commmand()
    print(request)
