import simpleaudio as sa

song_url = "The Wind - Cat Stevens.wav"

def play_song():
    wave_obj = sa.WaveObject.from_wave_file(song_url)
    play_obj = wave_obj.play()

def stop_song():
    sa.stop_all()
