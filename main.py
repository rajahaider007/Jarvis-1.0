import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def commmand():
    content = " "
    while content == " ":
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


def main_process():
    while True:
        request = commmand().lower()

        if "hello" in request:
            speak("Welcome, How I can help you.")

        elif "play music" in request:
            speak("Playing Music....")
            song = random.randint(1, 3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/shorts/E_zCoppoTk8")
            elif song == 2 or song == 3:
                webbrowser.open("https://www.youtube.com/shorts/YSro73zQIao")

        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + str(now_time))

        elif "say date" in request:
            now_date = datetime.datetime.now().strftime("%d:%m")
            speak("Current date is " + str(now_date))

        elif "new task" in request:
            task = request.replace("new task ", "").strip()
            if task != "":
                speak("Adding task: " + task)
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")

        elif "speak task" in request:
            with open("todo.txt", "r") as file:
                speak("Work we have to do today is : " + file.read())

        elif "show work" in request:
            with open("todo.txt", "r") as file:
                tasks = file.read()
            notification.notify(title="Today's Work", message=tasks)

        elif "open" in request:
            query = request.replace("open ", "").strip()
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif "wikipedia" in request:
            request = request.replace("wikipedia ", "").strip()
            result = wikipedia.summary(request, sentences=2)
            speak(result)

        elif "open youtube" in request:
            webbrowser.open("https://www.youtube.com")

        elif "search google" in request:
            query = request.replace("search google ", "").strip()
            webbrowser.open("https://www.google.com/search?q=" + query)

        elif "send whatsapp" in request:
            try:
                # Default phone and message
                phone_number = "+923055298017"
                message = "Hi, how are you?"

                # Adjust for custom message in voice
                if "message" in request:
                    parts = request.split("message")
                    if len(parts) > 1:
                        message = parts[1].strip()

                now = datetime.datetime.now() + datetime.timedelta(minutes=2)
                hour = now.hour
                minute = now.minute

                speak("Sending your WhatsApp message in 2 minutes.")
                pwk.sendwhatmsg(phone_number, message, hour, minute, wait_time=10)
            except Exception as e:
                speak("Something went wrong while sending the WhatsApp message.")
                print(str(e))

        elif "send email" in request:
            pwk.send_mail(
                "janjuaalihaider786@gmail.com",
                user_config.gmail_password,
                "Sending Email from python",
                "Hello this is my email from my jarvis",
                "oppagli007@gmail.com",
            )


main_process()
