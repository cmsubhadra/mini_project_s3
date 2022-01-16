import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
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


if __name__ == '__main__':
    wishme()
    speak("Iam your Personal Assistant Sudu, how can i help you lady! ")
while True:
    query = takeCommand().lower()
    if 'wikipedia' in query:
       speak("Searching wikipedia...")
       query.replace("Wikipedia"," ")
       results=wikipedia.summary(query,sentences=4)
       speak("According to wikipedia")
       print (results)
       speak(results)
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
    elif 'open mongoDB compass' in query:
        path="C:\\Users\cmsub\AppData\Local\MongoDBCompass\MongoDBCompass.exe"
        os.startfile(path)
    elif 'stop' in query:
        exit()
