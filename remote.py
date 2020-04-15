import json
import lcd
import time
import Spotify
import Genius
from gpiozero import Button

LCD = lcd.connect()
lcd.displayState(LCD, ["Please Wait", "Booting Up!"])
# time.sleep(60)


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
            songName    = currentSong['name']
            songArtist	= currentSong['artist']
            songPercent = currentSong['songPercent']
            lyrics      = Genius.search(geniusSession, songName, songArtist)
            if lyrics:
                displayLines = lyrics['displayLines']
                lineCount    = lyrics['lineCount']
                currentLine  = int(songPercent*lineCount)
                speed        = 1.20
                while currentLine >= 0 and currentLine < len(displayLines)-1 and showLyrics_button.is_pressed:
                    lcd.displayState(LCD, [displayLines[currentLine], displayLines[currentLine+1]])
                    
                    if previous_button.is_pressed and currentLine >= 1:
                        currentLine -= 1
                        time.sleep(.05)
                    elif next_button.is_pressed and currentLine < len(displayLines)-1:
                        currentLine += 1
                        time.sleep(.05)
                    else:                  
                        if volumeDown_button.is_pressed and speed >= 0.5:
                            speed -= .10
                        if volumeUp_button.is_pressed and speed < 1.75:
                            speed += .10
                        currentLine += 1
                        print(currentLine, speed)
                        time.sleep(speed)



    if (time.time() - oldtime) > 9:
    	print("10 Seconds have passed")
    	currentSong = Spotify.currentSong(spotifySession)
    	if currentSong:
	    	songName	= currentSong['name']
	    	songArtist	= currentSong['artist']
	    	lcd.displayState(LCD, [songName, songArtist])
    	oldtime = time.time()