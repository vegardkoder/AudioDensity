import tkinter as tk
import simpleaudio as sa
import glob
import random

import songs

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.song_list = []
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.choice = tk.StringVar(self)
        self.choice.set("audio\The Wind - Cat Stevens.wav")
        self.song_chooser = tk.OptionMenu(self, self.choice, *glob.glob("audio/*.wav"))
        self.song_chooser.pack()

        self.play_song_button = tk.Button(self)
        self.play_song_button["text"] = "Play Song"
        self.play_song_button["command"] = self.play_song
        self.play_song_button.pack(side="top")

        self.next_song_button = tk.Button(self)
        self.next_song_button["text"] = "Next Song"
        self.next_song_button["command"] = self.next_song
        self.next_song_button.pack(side="top")

        self.random_song_button = tk.Button(self)
        self.random_song_button["text"] = "Random Song"
        self.random_song_button["command"] = self.random_song
        self.random_song_button.pack(side="top")

        self.stop_song_button = tk.Button(self)
        self.stop_song_button["text"] = "Stop Song"
        self.stop_song_button["command"] = self.stop_song
        self.stop_song_button.pack(side="top")

    def play_song(self):
        self.song_list.extend(glob.glob("audio/*.wav"))
        sa.stop_all()
        wave_obj = sa.WaveObject.from_wave_file(self.choice.get())
        wave_obj.play()

    def next_song(self):
        if self.song_list != []:
            self.song_list.remove(self.choice.get())
            random.shuffle(self.song_list)
            sa.stop_all()
            wave_obj = sa.WaveObject.from_wave_file(self.song_list[0])
            self.song_list.pop()
            wave_obj.play()
        else:
            print("You have not choosen a song yet")

    def random_song(self):
        self.song_list.extend(glob.glob("audio/*.wav"))
        random.shuffle(self.song_list)
        sa.stop_all()
        for song in self.song_list:
            wave_obj = sa.WaveObject.from_wave_file(song)
            self.song_list.pop()
            play_obj = wave_obj.play()
            play_obj.wait_done()

    def stop_song(self):
        sa.stop_all()

root = tk.Tk()
root.title("AudioDensity")
app = App(master=root)
app.mainloop()
