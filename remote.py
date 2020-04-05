import spotipy
import json
from spotipy import util 
from gpiozero import Button
from time import sleep
import spotify_playback as playback
import spotify_next as nextSong
import spotify_previous as previousSong

play_button = Button(2)
previous_button = Button(3)
next_button = Button(4)

while True:
    if play_button.is_pressed:
        print("> ||")
        print(json.dumps(playback.playback(), indent=2))

    if previous_button.is_pressed:
        print("<<-")
        print(json.dumps(spotify_previous.previousSong(), indent=2))

    if next_button.is_pressed:
        print("->>")
        print(json.dumps(spotify_next.nextSong(), indent=2))
    # else:
    #     print("Released")
    # sleep(1)