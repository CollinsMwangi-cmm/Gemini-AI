import google.generativeai as genai
import pyttsx3
import speech_recognition as sr


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


API_KEY ="#####"
genai.configure(api_key=API_KEY)


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
    response  = chat.send_message(user_input)
    speak( response.text)

