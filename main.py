import speech_recognition as sr
import os
import webbrowser
import datetime
import random
import pyttsx3
from groq import Groq

# ================== CONFIG ==================
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# ================== VOICE ENGINE ==================
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

chatStr = ""

# ================== SPEAK ==================
def say(text):
    print("Jarvis:", text)
    try:
        engine.stop()  # stop previous speech
        for line in text.split("."):
            engine.say(line)
        engine.runAndWait()
    except Exception as e:
        print("Voice Error:", e)

# ================== STOP ==================
def stop_speech():
    engine.stop()
    print("Jarvis stopped")

# ================== CHAT ==================
def chat(query):
    global chatStr
    chatStr += f"User: {query}\n"

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are Jarvis AI assistant."},
                {"role": "user", "content": chatStr}
            ]
        )

        reply = response.choices[0].message.content
        chatStr += f"Jarvis: {reply}\n"

        say(reply)
        return reply

    except Exception as e:
        print("Error:", e)
        say("Something went wrong")

# ================== AI FILE ==================
def ai(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        text = response.choices[0].message.content

        if not os.path.exists("AI_Files"):
            os.mkdir("AI_Files")

        filename = f"AI_Files/{random.randint(1000,99999)}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)

        say("File saved successfully")

    except Exception as e:
        print("Error:", e)
        say("Error saving file")

# ================== VOICE INPUT ==================
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except:
            return ""

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User:", query)
        return query.lower()

    except Exception as e:
        print("Recognition Error:", e)
        return ""

# ================== MAIN ==================
if __name__ == '__main__':
    print("🚀 Starting Jarvis...")
    say("Hello, I am Jarvis. How can I help you?")

    while True:
        query = takeCommand()

        if query == "":
            continue

        # 🔥 STOP COMMAND
        if "stop" in query:
            stop_speech()
            continue

        # ===== WEBSITES =====
        elif "open youtube" in query:
            say("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            say("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open wikipedia" in query:
            say("Opening Wikipedia")
            webbrowser.open("https://www.wikipedia.com")

        # ===== MUSIC =====
        elif "play music" in query:
            path = "C:\\Users\\YourName\\Downloads\\song.mp3"
            if os.path.exists(path):
                os.startfile(path)
                say("Playing music")
            else:
                say("Music file not found")

        # ===== TIME =====
        elif "time" in query:
            now = datetime.datetime.now()
            say(f"The time is {now.hour} {now.minute}")

        # ===== APPS =====
        elif "open notepad" in query:
            os.system("start notepad")

        elif "open chrome" in query:
            os.system("start chrome")

        # ===== AI WRITE =====
        elif "write" in query:
            ai(query)

        # ===== RESET CHAT =====
        elif "reset chat" in query:
            chatStr = ""
            say("Chat reset")

        # ===== EXIT =====
        elif "exit" in query or "jarvis quit" in query:
            say("Goodbye")
            break

        # ===== DEFAULT AI =====
        else:
            chat(query)