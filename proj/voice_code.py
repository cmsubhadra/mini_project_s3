from email.mime import audio
from matplotlib.animation import PillowWriter
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
import subprocess as sp
from decouple import config
paths = {
    'calculator': "C:\\Windows\\System32\\calc.exe"
}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning Subhadra")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Subhadra")
    else:
        speak("Good evening Subhadra")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n")
    except Exception as e:
        print("Say that again please....")
        return 'None'
    return query
def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
def open_calculator():
    sp.Popen(paths['calculator'])


apikey = "6fcc5e3ff5664b808da9a24b7e947f8d"

def news():
    url =" https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=" + apikey
    news = requests.get(url).json()
    article=news["articles"]
    news_article=[]
    for arti in article:
        news_article.append(arti["title"])
    
    speak(news_article)
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

