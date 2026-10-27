import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import time
import json
r = sr.Recognizer()
engine=pyttsx3.init()
newsapi="d7c43a8d7e404b9591443b089ac20c99"
def speak_old(text):
    engine.say(text)
    engine.runAndWait()
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    # Initialize the mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")  # Replace with your file path

    # Set volume (0.0 to 1.0)
    pygame.mixer.music.set_volume(1.0)

    # Play the music
    pygame.mixer.music.play()

    print("Playing...")

    # Wait until the music finishes
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    print("Playback finished.")
    pygame.quit()
def aiprocess(command):


    user_question = input("Enter your question: ")

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.2",
            "messages": [
                {
                    "role": "system",
                    "content": "You are Jarvis, a helpful AI assistant. Give short and accurate answers."
                },
                {
                    "role": "user",
                    "content": user_question
                }
            ],
            "stream": False
        }
    )

    # print(response.json()["message"]["content"])
    reply = response.json()["message"]["content"]
    print(reply)
    speak(reply)
    # import os
# from openai import OpenAI

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif  "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif  "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()

        found = False

        for key in musiclibrary.music:
            if song in key:
                webbrowser.open(musiclibrary.music[key])
                found = True
                break

        if not found:
            print("Song not found")
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/everything?q=India&sortBy=publishedAt&language=en&apiKey={newsapi}")
        print("Status Code:", r.status_code)
        print(r.text)
        if r.status_code==200:
            data=r.json()
            print(data)
            if data["status"] == "ok":
                for article in data["articles"][:5]:
                    print(article["title"])
                    engine.say(article["title"])
                    engine.runAndWait()
            articles=data.get("articles",[])
            for article in articles:
                # engine.say(article['title'])
                # engine.runAndWait()
                speak(article['title'])
                # print(article['title'])
    else:
        #let open ai handles the request
        output=aiprocess(c)
        speak(output)

if __name__=="__main__":
    speak("initializing jarvis...")
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone(device_index=2) as source:
                print("Listening...")
                # Calibrate once for the current environment
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=3, phrase_time_limit=2)

            text = r.recognize_google(audio)
            print("You said:", text)
            if( text.lower()=="jarvis"):

                engine.say("Yes")

                with sr.Microphone(device_index=2) as source:
                    print("Jarvis Activated...")
                    audio = r.listen(source)

                command = r.recognize_google(audio)
                print("Command:", command)

                processcommand(command)

            if text.lower() == "exit":
                print("Goodbye!")
                break





        except sr.WaitTimeoutError:
            print("No speech detected.")

        except sr.UnknownValueError:
            print("Couldn't understand. Please speak clearly.")

        except sr.RequestError as e:
            print("Request Error:", e)

        except Exception as e:
            print("Error:", e)
