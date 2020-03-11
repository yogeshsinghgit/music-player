from tkinter import *
from tkinter import filedialog
import os
import pygame

""" my name is yogesh singh , Admin og instagram page dynamic_codeing ....
 you can follow me on github and instagram for more amazing python projects ..."""

"""directory = input("Where is your music located?")
maybe add an option to change music directory"""



class MusicPlayer:
    def __init__(self,root):
        self.root = root
        self.root.title("Music-Player")
        self.root.geometry("1024x600")
        self.root.resizable(0,0)
        # initializing pygame constructor ....
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable

        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()
        # unpause and pause
        self.unpause = True




        # making widgrts of music player

        # title frame
        track_frame = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        track_frame.place(x=0,y=0,width=1024,height=100)

        # Inserting Song Track Label
        songtrack = Label(track_frame, textvariable=self.track, width=15, font=("times new roman", 20, "bold"),
                          bg="grey", fg="gold")
        songtrack.place(x=0,y=5,width=1000,height=35)
        # Inserting Status Label
        trackstatus = Label(track_frame, textvariable=self.status, font=("times new roman", 15, "bold"), bg="grey",fg="gold")
        trackstatus.place(x=900,y=35,width=100,height=25)

        # Creating Button Frame
        buttonframe = LabelFrame(self.root, text="Control Panel", font=("times new roman", 15, "bold"), bg="grey",
                                 fg="white", bd=5, relief=GROOVE)
        buttonframe.place(x=0, y=100, width=1024, height=200)
        # Inserting Play Button
        playbtn = Button(buttonframe, text="PLAY", command=self.playsong, width=6, height=1,
                         font=("times new roman", 12, "bold"), fg="navyblue", bg="gold").place(x=5,y=5)
        # Inserting Pause Button
        self.pausebtn = Button(buttonframe, text="PAUSE", command=self.pausesong, width=10, height=1,
                         font=("times new roman", 12, "bold"), fg="navyblue", bg="gold")
        self.pausebtn.place(x=460,y=5)

        # Inserting Stop Button
        stopbtn = Button(buttonframe, text="STOP", command=self.stopsong, width=6, height=1,
                         font=("times new roman", 12, "bold"), fg="navyblue", bg="gold").place(x=947,y=5)
        # inserting volume slider ...

        self.scale = Scale(buttonframe,orient='horizontal', from_=0, to=100, command=self.setvolume,length =1000,relief = GROOVE,bg='grey',troughcolor="gold",
                      fg="Gold",sliderlength=10,width=15)
        self.scale.set(50)
        self.scale.place(x=5,y=75)

        # Creating Playlist Frame
        songsframe = LabelFrame(self.root, text="Song Playlist", font=("times new roman", 15, "bold"), bg="grey",
                                fg="white", bd=5, relief=GROOVE)
        songsframe.place(x=0, y=300, width=1024, height=300)

                # Inserting Open Button
        openbtn = Button(songsframe, text="Open", command=self.open, width=6, height=1,
                         font=("times new roman", 14, "bold"), fg="navyblue", bg="gold").pack(side=BOTTOM)

        # Inserting scrollbar
        scrol_y = Scrollbar(songsframe, orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=SINGLE,
                                font=("times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE)
        self.playlist.place(x=512, y=0, width=500, height=575)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

        # Changing Directory for fetching Songs
        os.chdir("C:\\Users\\brannon.harper\\Music")
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
            if track.endswith('.mp3'):
                self.playlist.insert(END, track)

        # Defining Play Song Function
    def playsong(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.set_volume(0.1)
        #print(pygame.mixer.music.get_volume())
        pygame.mixer.music.play(-1)

    def setvolume(self,val):
        pygame.mixer.music.set_volume(int(val)/1000)

    def stopsong(self):
        # Displaying Status
        self.status.set("-Stopped")
        # Stopped Song
        pygame.mixer.music.stop()

    def pausesong(self):
        if(self.unpause):
            # Displaying Status
            self.status.set("-Paused")
            self.pausebtn['text'] = "Unpause"
            # Paused Song
            pygame.mixer.music.pause()
            self.unpause = False
        else:
            # Displaying Status
            self.status.set("-Playing")
            self.pausebtn['text'] = "Pause"
            # Playing back Song
            pygame.mixer.music.unpause()
            self.unpause=True
    def open(self):
        path = filedialog.askdirectory()
        # Changing Directory for fetching Songs
        os.chdir(path)

        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        self.playlist.delete(0,END)
        for track in songtracks:
            if track.endswith('.mp3'):
                self.playlist.insert(END, track)




# Creating TK Container
root = Tk()
# Passing Root to MusicPlayer Class
MusicPlayer(root)
# Root Window Looping
root.mainloop()
