import spotipy
import json
from spotipy import util 
from gpiozero import Button
from time import sleep
import spotify_playback as playback
button = Button(2)

while True:
    if button.is_pressed:
        print("Pressed")
        print(json.dumps(playback.playback(), indent=2))

    else:
        print("Released")
    sleep(1)