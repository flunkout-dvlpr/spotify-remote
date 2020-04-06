import json
import lcd
import Spotify 
import time
from gpiozero import Button

LCD = lcd.connect()

spotifySession = Spotify.connect()

play_button = Button(2)
previous_button = Button(3)
next_button = Button(4)
volumeUp_button = Button(17)
volumeDown_button = Button(27)
addToPlaylist_button = Button(22)

oldtime = time.time()
while True:

    if play_button.is_pressed:
        print("||>")
        print(json.dumps(Spotify.playback(spotifySession), indent=2))

    if previous_button.is_pressed:
        print("<<-")
        print(json.dumps(Spotify.previousSong(spotifySession), indent=2))

    if next_button.is_pressed:
        print("->>")
        print(json.dumps(Spotify.nextSong(spotifySession), indent=2))

    if volumeUp_button.is_pressed:
    	print("▲")
    	print(json.dumps(Spotify.volumeUp(spotifySession), indent=2))

    if volumeDown_button.is_pressed:
    	print("▼")
    	print(json.dumps(Spotify.volumeDown(spotifySession), indent=2))
    
    if addToPlaylist_button.is_pressed:
    	print("+")
    	print(json.dumps(Spotify.addToPlaylist(spotifySession), indent=2))
    	
    if (time.time() - oldtime) > 14:
    	print("15 Seconds have passed")
    	oldtime = time.time()
#    if tenSeconds:	
#     currentSong = Spotify.currentSong(spotifySession)
#     songName    = currentSong['name']
#     songArtist  = currentSong['artist']
#     lcd.displaySongInfo(LCD, songName, songArtist)
# else: