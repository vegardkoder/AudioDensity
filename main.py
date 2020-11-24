import tkinter as tk
import simpleaudio as sa

import songs

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.play_song_button = tk.Button(self)
        self.play_song_button["text"] = "Play Song"
        self.play_song_button["command"] = songs.play_song
        self.play_song_button.pack(side="top")

        self.stop_song_button = tk.Button(self)
        self.stop_song_button["text"] = "Stop Song"
        self.stop_song_button["command"] = songs.stop_song
        self.stop_song_button.pack(side="top")

root = tk.Tk()
app = App(master=root)
app.mainloop()
