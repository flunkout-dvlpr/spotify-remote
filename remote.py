import json
import lcd
import time
import Spotify
import Genius
from gpiozero import Button

LCD = lcd.connect()
lcd.displayState(LCD, ["Please Wait", "Booting Up!"])
time.sleep(60)


spotifySession = Spotify.connect()
geniusSession  = Genius.connect()

play_button 			= Button(2)
previous_button 		= Button(3)
next_button 			= Button(4)
volumeUp_button 		= Button(17)
volumeDown_button 		= Button(27)
addToPlaylist_button 	= Button(22)
showLyrics_button		= Button(18)


oldtime = time.time()
while True:

    if play_button.is_pressed:
    	response = Spotify.playback(spotifySession)
    	lcd.displayState(LCD, response['state'])
        #print("||>")
        #print(json.dumps(Spotify.playback(spotifySession), indent=2))

    if previous_button.is_pressed:
    	response = Spotify.previousSong(spotifySession)
    	lcd.displayState(LCD, response['state'])
        #print("<<-")
        #print(json.dumps(Spotify.previousSong(spotifySession), indent=2))

    if next_button.is_pressed:
    	response = Spotify.nextSong(spotifySession)
    	lcd.displayState(LCD, response['state'])
        # print("->>")
        # print(json.dumps(Spotify.nextSong(spotifySession), indent=2))

    if volumeUp_button.is_pressed:
    	response = Spotify.volumeUp(spotifySession)
    	lcd.displayState(LCD, response['state'])
    	# print("▲")
    	# print(json.dumps(Spotify.volumeUp(spotifySession), indent=2))

    if volumeDown_button.is_pressed:
    	response = Spotify.volumeDown(spotifySession)
    	lcd.displayState(LCD, response['state'])
    	# print("▼")
    	# print(json.dumps(Spotify.volumeDown(spotifySession), indent=2))
    
    if addToPlaylist_button.is_pressed:
    	response = Spotify.addToPlaylist(spotifySession)
    	lcd.displayState(LCD, response['state'])
    	# print("+")
    	# print(json.dumps(Spotify.addToPlaylist(spotifySession), indent=2))

    while showLyrics_button.is_pressed:   	
    	currentSong = Spotify.currentSong(spotifySession)
    	if currentSong:
	    	songName	= currentSong['name']
	    	songArtist	= currentSong['artist']
	    	lyrics 		= Genius.search(geniusSession, songName, songArtist)
	    	if lyrics:
	    		displayLines = lyrics['displayLines']
	    		for lineNumber in range(0, len(displayLines)-1):
	    			lcd.displayState(LCD, [displayLines[lineNumber], displayLines[lineNumber+1]])
	    			#time.sleep(1.5)



    if (time.time() - oldtime) > 9:
    	print("10 Seconds have passed")
    	currentSong = Spotify.currentSong(spotifySession)
    	if currentSong:
	    	songName	= currentSong['name']
	    	songArtist	= currentSong['artist']
	    	lcd.displayState(LCD, [songName, songArtist])
    	oldtime = time.time()