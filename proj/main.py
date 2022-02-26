from tkinter.ttk import *
from tkinter import*
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont,ImageTk
import PIL.Image
from tkinter.scrolledtext import ScrolledText
import tkinter as tk

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
    

                if 'wikipedia' in query:
                    speak('What do you want to search on Wikipedia lady?')
                    search_query = takeCommand().lower()
                    results =search_on_wikipedia (search_query)
                    speak(f"According to Wikipedia, {results}")
                    speak("For your convenience, I am printing the info on the screen lady.")
                    #print(results)
                    self.scroll_text.insert(tk.INSERT,"\n"+results)

                elif 'open google' in query:
                    webbrowser.open('google.com')
                elif 'open youtube' in query:
                    webbrowser.open('youtube.com')
                elif 'open stack overflow' in query:
                    webbrowser.open('stackoverflow.com')
                elif 'play music' in query:
                    music_dir='C:\\Users\\cmsub\\Music'
                    songs=os.listdir(music_dir)
                    #print(songs)
                    #self.scroll_text.insert(tk.INSERT,"\n"+songs )
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif 'the time' in query:
                    strTime=datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"The time is {strTime}\n")
                    speak("For your convenience, I am printing the time on the screen lady.")
                    #print("The time is"+strTime)
                    self.scroll_text.insert(tk.INSERT,"\nThe time is:"+strTime)
                elif 'joke' in query:
                    joke=get_random_joke()
                    speak(joke)
                    speak("For your convenience, I am printing the joke  on the screen lady.")
                    #print("Joke is"+joke)
                    self.scroll_text.insert(tk.INSERT,"\nJoke is:"+joke)
                elif 'camera' in query:
                    self.scroll_text.insert(tk.INSERT,"\n---OPENING CAMERA---")
                    open_camera()
                elif 'calculator' in query:
                    self.scroll_text.insert(tk.INSERT,"\n---OPENING CALCULATOR---")
                    open_calculator()
                elif 'news' in query:
                    self.scroll_text.insert(tk.INSERT,"\n"+f"Listen to the news....")
                    news()

                elif 'ip address' in query:
                    ip_address = find_my_ip()
                    speak(f'Your IP Address is: {ip_address}.\n For your convenience, I am printing it on the screen lady.')
                    #print(f'Your IP Address is {ip_address}')
                    self.scroll_text.insert(tk.INSERT,"\n"+f'Your IP Address is {ip_address}')
                
                elif "advice" in query:
                    speak(f"Here's an advice for you, lady")
                    advice = get_random_advice()
                    speak(advice)
                    speak("For your convenience, I am printing it on the screen lady.")
                    #print(advice)
                    self.scroll_text.insert(tk.INSERT,"\n"+advice)
                elif "weather" in query:
                    search = "temperature in trivandrum"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current {search} is {temp}")
                    speak("For your convenience, I am printing it on the screen lady.")
                    #print("The temperature at trivandrum is:"+temp)
                    self.scroll_text.insert(tk.INSERT,"\nThe temperature at trivandrum is:"+temp)
    
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
