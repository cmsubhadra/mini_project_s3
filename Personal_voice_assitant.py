from email.mime import audio
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
    for i in range(5):
        print(i+1,news_article[i])
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
if __name__ == '__main__':
    wishme()
    speak("Iam your Personal Assistant Sudu, how can i help you lady! ")
    while True:
     query = takeCommand().lower()
    

     if 'wikipedia' in query:
            speak('What do you want to search on Wikipedia lady?')
            search_query = takeCommand().lower()
            results =search_on_wikipedia (search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing the info on the screen lady.")
            print(results)

     elif 'open google' in query:
      webbrowser.open('google.com')
     elif 'open youtube' in query:
        webbrowser.open('youtube.com')
     elif 'open stack overflow' in query:
        webbrowser.open('stackoverflow.com')
     elif 'play music' in query:
        music_dir='C:\\Users\\cmsub\\Music'
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
     elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}\n")
        speak("For your convenience, I am printing the time on the screen lady.")
        print("The time is"+strTime)
     elif 'joke' in query:
        joke=get_random_joke()
        speak(joke)
        speak("For your convenience, I am printing the joke  on the screen lady.")
        print("Joke is"+joke)
     elif 'camera' in query:
      open_camera()
     elif 'calculator' in query:
        open_calculator()
     elif 'news' in query:
        news()
     elif 'ip address' in query:
        ip_address = find_my_ip()
        speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen lady.')
        print(f'Your IP Address is {ip_address}')
     elif "weather" in query:
        search = "temperature in trivandrum"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"current {search} is {temp}")
        speak("For your convenience, I am printing it on the screen lady.")
        print("The temperature at trivandrum is:"+temp)
     elif "advice" in query:
            speak(f"Here's an advice for you, lady")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen lady.")
            print(advice)

    
     elif 'power off' in query:
        exit()


