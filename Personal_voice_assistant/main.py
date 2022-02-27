#to make gui
from tkinter.ttk import *
from tkinter import*
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont,ImageTk
import PIL.Image
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from numpy import take

# To access Spotipy
import spotipy
# To View the API response
import json
# To open our song in our default browser
import webbrowser

from voice_code import *
import threading

decision_counter = 0
stop_threads = False


root = Tk()

class Convert:
    def __init__(self, master):
        self.master = master
        master.title("Single Button Event")
        master.geometry("1000x2000")
        master.configure(bg="white")

        # Demo model certificate
        model = PIL.Image.open("poweron.png")
        newsize = (600, 600)
        model = model.resize(newsize)
        IMG_STATUS = ImageTk.PhotoImage(model)

                
        #full window row configure
        master.grid_rowconfigure(0, weight=1)
   
        #full window column configure
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)

        
        #Fonts
        self.label_frame_font = font.Font(family="Helvetica",size=10,weight="bold")
        self.frame2_font = font.Font(family="Franklin Gothic Medium",size=10)

        # MENU SECTION STARTED #####################################################
        self.menu_section = Menu(master)                                                                 # menu started
        self.menu_section_file = Menu(self.menu_section,tearoff = 0)                          # file menu option
        self.menu_section_file.add_command(label="About")
        self.menu_section_file.add_command(label="close")
        self.menu_section_file.add_separator()                                                            #menu option seperator
        self.menu_section_file.add_command(label="Exit")
        master.config(menu = self.menu_section)                                                         # file menu configure with the menu_section
        self.menu_section.add_cascade(label="File", menu = self. menu_section_file)   #menu label

        #END MENU #####################################################################

        #labelled frames
        self.frame_left     =  LabelFrame(master,text="ON/OFF",labelanchor="n",bg="#34ebeb",bd=10,fg="black",font=self.label_frame_font)
        self.frame_right    =  LabelFrame(master,text="INFO",labelanchor="n",bg="#34ebeb",bd=10,fg="black",font=self.label_frame_font)

        #frame grids
        self.frame_left.grid(row=0,column=0,sticky="nsew")
        self.frame_right.grid(row=0,column=1,sticky="nsew")
        
        #frame for componants for first labeled frame  row configure  1
        self.frame_left.grid_rowconfigure(0, weight=1)
        self.frame_left.grid_rowconfigure(1, weight=1)
        self.frame_left.grid_rowconfigure(2, weight=1)
        self.frame_left.columnconfigure(0, weight=1)
        self.frame_left.columnconfigure(1, weight=1)
        self.frame_left.columnconfigure(2, weight=1)
        #componants for frame 1  
        self.frame2_btn = Button(self.frame_left,image=IMG_STATUS,text="Calculate",height = 380, width = 380,command=lambda:activate())
        self.frame2_btn.image=IMG_STATUS
        #componants grid for frame 1
        self.frame2_btn.grid(row=1,column=1)


        #frame for componants for first labeled frame  row configure  2
        self.frame_right.grid_rowconfigure(0, weight=1)   
        self.frame_right.columnconfigure(0, weight=1)
        #componants for frame 2
        self.scroll_text = ScrolledText(self.frame_right,bg="yellow",fg="black")
        #componants grid for frame 2
        self.scroll_text.grid(row=0,column=0)
                      
        self.scroll_text.insert(tk.INSERT,"\t\t\t------------INFO----------\n")
        import time
        #stop_threads = False

        #######################################

        def main_code():
            global stop_threads
            wishme()
            speak("Iam your Personal Assistant Sudu, how can i help you lady! ")
            while True:
                if stop_threads:
                    break
                query = takeCommand().lower()
    

                if 'open wikipedia' in query:
                    speak('What do you want to search on Wikipedia lady?')
                    search_query = takeCommand().lower()
                    results =search_on_wikipedia (search_query)
                    speak(f"According to Wikipedia, {results}")
                    speak("For your convenience, I am printing the info on the screen lady.")
                    self.scroll_text.insert(tk.INSERT,"\nAccording to wikipedia:"+results)

                elif 'open google' in query:
                    self.scroll_text.insert(tk.INSERT,"\n---OPENING GOOGLE---")
                    webbrowser.open('google.com')
                elif 'open youtube' in query:
                    self.scroll_text.insert(tk.INSERT,"\n---OPENING YOUTUBE---")
                    webbrowser.open('youtube.com')
                elif 'open stack overflow' in query:
                    self.scroll_text.insert(tk.INSERT,"\n---OPENING STACK OVERFLOW---")
                    webbrowser.open('stackoverflow.com')
                elif 'play music in system' in query:
                    music_dir='C:\\Users\\cmsub\\Music'
                    songs=os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif 'tell me the time' in query:
                    strTime=datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"The time is  {strTime}\n")
                    speak("For your convenience, I am printing the time on the screen lady.")
                    self.scroll_text.insert(tk.INSERT,"\nThe time is: "+strTime)
                elif 'tell me joke' in query:
                    joke=get_random_joke()
                    speak(joke)
                    speak("For your convenience, I am printing the joke  on the screen lady.")
                    self.scroll_text.insert(tk.INSERT,"\nJoke is:"+joke)
                elif 'open camera' in query:
                    self.scroll_text.insert(tk.INSERT,"\n---OPENING CAMERA---")
                    open_camera()
                elif 'open calculator' in query:
                    self.scroll_text.insert(tk.INSERT,"\n---OPENING CALCULATOR---")
                    open_calculator()
                elif 'latest news' in query:
                    self.scroll_text.insert(tk.INSERT,"\n"+f"Listen to the news....")
                    news()

                elif 'tell me ip address' in query:
                    ip_address = find_my_ip()
                    speak(f'Your IP Address is: {ip_address}.\n For your convenience, I am printing it on the screen lady.')
                    self.scroll_text.insert(tk.INSERT,"\n"+f'Your IP Address is {ip_address}')
                elif "report weather" in query:
                    speak('Of which location do you want to know the weather')
                    takeCommand()
                    search = " temperature in"+takeCommand().lower()
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current  temperature  is {temp}")
                    speak("For your convenience, I am printing it on the screen lady.")
                    self.scroll_text.insert(tk.INSERT,"\ntemperature is "+temp)
                elif "give me advice" in query:
                    speak(f"Here's an advice for you, lady")
                    advice = get_random_advice()
                    speak(advice)
                    speak("For your convenience, I am printing it on the screen lady.")
                    self.scroll_text.insert(tk.INSERT,"\nAdvice is: "+advice)

                elif 'play music in spotify' in query:
                    speak("which song do you want my lady?")
                    search_query = takeCommand().lower()
                    username = 'cmsubhu1999@gmail.com'
                    clientID = '43f4278964f64029a39cc5873eaf7612'
                    clientSecret = '405d7e800d8f4694a7d4c2af16f1e91d'
                    redirectURI = 'http://google.com/'
                    oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
                    token_dict = oauth_object.get_access_token()
                    token = token_dict['access_token']
                    spotifyObject = spotipy.Spotify(auth=token)
                    user = spotifyObject.current_user()
                    print(json.dumps(user,sort_keys=True, indent=4))
                    
                    
                        # Search for the Song.
                    searchResults = spotifyObject.search(search_query,1,0,"track")
                    # Get required data from JSON response.
                    tracks_dict = searchResults['tracks']
                    tracks_items = tracks_dict['items']
                    song = tracks_items[0]['external_urls']['spotify']
                    # Open the Song in Web Browser
                    webbrowser.open(song)
                    print('Song has opened in your browser.')

                elif 'power off' in query:
                    self.scroll_text.insert(tk.INSERT,"\n---POWER OFF---")
                    exit()
                                                           
                    
                         
                


        #######################################

      


        func_thread = threading.Thread(target = main_code)
 
        def activate():
            global decision_counter
            #global stop_threads

            if(decision_counter == 0):
                model = PIL.Image.open("mic.png")
                #self.scroll_text.insert(tk.INSERT,"\nListening...")
                decision_counter=1
                self.func_thread = threading.Thread(target = main_code)
                self.func_thread.start()
            else:
                model = PIL.Image.open("poweroff.png")
                self.scroll_text.insert(tk.INSERT,"\n!!! OFF !!!")
                decision_counter=0
                stop_threads = True
                #self.func_thread.join()
                #print("join success")
                
            newsize = (400, 400)
            model = model.resize(newsize)
            IMG_STATUS = ImageTk.PhotoImage(model)
            self.frame2_btn = Button(self.frame_left,image=IMG_STATUS,text="Calculate",height = 400, width = 400,command=lambda:activate())
            self.frame2_btn.image=IMG_STATUS
            self.frame2_btn.grid(row=1,column=1)
            
            




hack_gui = Convert(root)
root.mainloop()
