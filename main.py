import simpleaudio as sa

song_url = "The Wind - Cat Stevens.wav"

wave_obj = sa.WaveObject.from_wave_file(song_url)
play_obj = wave_obj.play()
play_obj.wait_done()
