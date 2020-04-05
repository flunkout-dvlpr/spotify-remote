import json
import spotipy
from time import sleep
from spotipy import util 
from gpiozero import Button

import spotify_playback as playback
import spotify_next as nextSong
import spotify_previous as previousSong
import spotify_volumeUp as volumeUp
import spotify_volumeDown as volumeDown

play_button = Button(2)
previous_button = Button(3)
next_button = Button(4)
volumeUp_button = Button(17)
volumeDown_button = Button(27)

while True:
    if play_button.is_pressed:
        print("> ||")
        print(json.dumps(playback.playback(), indent=2))

    if previous_button.is_pressed:
        print("<<-")
        print(json.dumps(previousSong.previousSong(), indent=2))

    if next_button.is_pressed:
        print("->>")
        print(json.dumps(nextSong.nextSong(), indent=2))

    if volumeUp_button.is_pressed:
    	print("▲")
    	print(json.dumps(volumeUp.volumeUp(), indent=2))
    if volumeDown_button.is_pressed:
    	print("▼")
		print(json.dumps(volumeDown_button.volumeDown(), indent=2))


    # else:
    #     print("Released")
    # sleep(1)