import os
import lyricsgenius

def connect():
	GENIUS_TOKEN = os.environ.get('GENIUS_TOKEN')
	GENIUS_TOKEN = 'MgALQlKRu6ZSuEVdf0Da29Ut5WdOJ-Xox6Cfi2L3nZZf9Uxs8dEbFD5sP2a4N2s5'
	genius  	 = lyricsgenius.Genius(GENIUS_TOKEN)
	return genius

def search(geniusSession, songName, songArtist):
	genius  = geniusSession
	request = genius.search_song(songName, songArtist, get_full_info=False)
	if request:
		rawLyrics 		= request.lyrics.split('\n')
		lines 			= [line for line in rawLyrics if '[' not in line and line != '']
		oneliner		= (" ").join(lines)
		displayLines 	= [oneliner[x:x+16].strip() for x in range(0,len(oneliner),16)]
		lineCount 		= len(displayLines)
		return {'lines'			: lines,
				'displayLines'	: displayLines,
				'lineCount'		: lineCount			
				}
	else:
		return False 


# import time
# import Spotify
# sp = Spotify.connect()
# currentSong = Spotify.currentSong(sp)

# songName	= currentSong['name']
# songArtist	= currentSong['artist']
# songPercent = currentSong['songPercent']

# lyrics = search(songName, songArtist)

# displayLines = lyrics['displayLines']
# lineCount	 = lyrics['lineCount']

# # for dLine in displayLines:
# # 	print(dLine)
# print(songPercent)
# print(lineCount)
# print((songPercent*lineCount))

# currentLine = int(songPercent*lineCount)
# print(currentLine)

# while currentLine < len(displayLines)-1:
# 	print(displayLines[currentLine])
# 	print(displayLines[currentLine+1])
# 	print('*'*18)
# 	currentLine += 1
	time.sleep(1)

