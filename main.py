import tkinter as tk
import simpleaudio as sa
import glob

import songs

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.choice = tk.StringVar(self)
        self.choice.set("The Wind - Cat Stevens.wav")
        self.song_chooser = tk.OptionMenu(self, self.choice, *glob.glob("audio/*.wav"))
        self.song_chooser.pack()

        self.play_song_button = tk.Button(self)
        self.play_song_button["text"] = "Play Song"
        self.play_song_button["command"] = self.play_song
        self.play_song_button.pack(side="top")

        self.stop_song_button = tk.Button(self)
        self.stop_song_button["text"] = "Stop Song"
        self.stop_song_button["command"] = self.stop_song
        self.stop_song_button.pack(side="top")

    def play_song(self):
        wave_obj = sa.WaveObject.from_wave_file(self.choice.get())
        play_obj = wave_obj.play()

    def stop_song(self):
        sa.stop_all()

root = tk.Tk()
root.title("AudioDensity")
app = App(master=root)
app.mainloop()
