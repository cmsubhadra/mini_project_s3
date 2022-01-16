import subprocess as sub
import requests
import pyttsx3
import datetime
from requests.models import Response
import wikipedia
import requests,json
import speech_recognition as sr
import webbrowser
import os
from pyttsx3 import engine
import weather
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#voices[0] for male and voices[1] for female voice
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',130)
def speak(audio):
    #say something which is written on the function speak()
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak(" it's a nice " +
                    str(weather.weather_description)+"out there")
        speak(f' ,its{hour} AM in the morming')
    elif(hour>=12 and hour<16):
        speak(f' ,its{hour} PM in the afternoon')
    else:
        speak(f' ,its{hour} PM in the evening')
    speak("I'am friday. sir,how can i help you")
def takeCommand():
    #take an audio input from the user and returns a string object
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold=0.6
        r.energy_threshold=300
        #r.dynamic_energy_threshold=False
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language="en-in")
        print("User said:",query)
    except Exception as e:
        #print(e)
        print("Say that again please....")
        return 'None'
    return query
def newsBBC():
    query_params={
        "source":"bbc-news",
        "sortBy":"top",
        "apikey":"a11ec5be4a174a388fc94a0ded2189d4"
    }
    main_url="http://newsapi.org/v1/articles"
    res=requests.get(main_url,params=query_params)
    open_bbc_page=res.json()
    article=open_bbc_page["articles"]
    results=[]
    for ar in article:
        results.append(ar["title"])
    for i in range(len(results)):
        print(i+1,results[i])
    speak(results[0:5])
if __name__ == '__main__':
    speak("BOSS")
    wishme()
    
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query=query.replace("wikipedia",' ')
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open google' in query:
            speak("opening Google....")
            webbrowser.open("google.com")
        elif 'play music' in query:
            speak("playing your favorite one  boss")
            music_dir='D:\\music\\'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "the time"  in query:
            now=datetime.datetime.now()
            current_time=now.strftime("%H:%M:%S")
            print("current_time=",current_time)
            speak(f'the time is {current_time}')
        elif 'open bench' in query:
            speak("opening workbench...")
            path="C:\\Program Files\\MySQL\\MySQL Workbench 6.3 CE\\MySQLWorkbench.exe"
            os.startfile(path)
        elif 'open note'in query:
            speak("opening notepad....")
            path="Notepad.exe"
            sub.Popen(path)
        elif 'open code' in query:
            speak("opening Visual Studio Code boss....")
            path="C:\\Users\\anandhu123\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'terminate' in query:
            speak("good bye Boss,Have a good day")
            break
        elif 'news' in query:
            newsBBC()
        elif 'shutdown' in query:
            speak("shutting Down...")
            os.system("shutdown /s /t 1")
        elif 'weather' in query:
            speak(" it's a nice " +
                    str(weather.weather_description)+"out there")
            speak(" Temperature outside is" +
                    str(weather.current_temperature) +"kelvin"
            "\n atmospheric pressure is = " +
                    str(weather.current_pressure) +"hba"
            "\n and the humidity is " +
                    str(weather.current_humidity)+"percentage")
        elif 'joke' in query:
            speak("why are cricket stadiums so cool? Because every seat has a fan in it")