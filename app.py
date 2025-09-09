import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
import requests
import os
from dotenv import load_dotenv
import subprocess
from todoapp import add_task




load_dotenv()

def weather(city):
    API_KEY = os.getenv("WEATHER_API_KEY")
    URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q":city,
        "appid":API_KEY,
        "units":"metric"
    }
    response = requests.get(URL, params=params).json()
    
    if response["cod"] == 200:
        temp = response["main"]["temp"]
        humidity = response["main"]["humidity"]
        description = response["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with a humidity of {humidity}% and {description}."
    else:
        pass
    




def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        audio = r.listen(source)
        
        try:
            command = r.recognize_google(audio, language = "en-us")
            print("Bruno thinks you said: ", command)
            return command.lower()
        except Exception as e:
            print("Exception: ", str(e))
            return "None"
        

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    print("Gemini: ", text , "\n")
    engine.say(text)
    engine.runAndWait()



genai.configure(api_key=os.getenv("gemini_API_KEY"))


model = genai.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat(history=[
    {"role":"user", "parts": "From now on, you name is Bruno. You are a friendly, voice-powered assistant. "},
    {"role":"model", "parts": "Got it! I'll be Bruno from now on"}
])


print("Chat with Gemini! Type 'exit' to quit")
while True:
    user_input = take_command()
    if user_input.lower() == 'exit':
        break
    
    
    
    elif "weather" in user_input.lower():
        city = user_input.split("in")[-1].strip()
        weather_info = weather(city)
        speak(weather_info)
        continue
    
    elif "open calculator" in user_input.lower():
        subprocess.Popen('calc.exe')
        continue
    
    elif "open spotify" in user_input.lower():
        subprocess.Popen('spotify.exe')
        continue
    
    elif "add task" in user_input.lower():
        task = user_input.split("add task")[-1].strip()
        result = add_task(task)
        speak(result)
        continue
    
    response  = chat.send_message(user_input)
    speak( response.text)