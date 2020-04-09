import os
import lyricsgenius

def connect():
	GENIUS_TOKEN = os.environ.get('GENIUS_TOKEN')
	GENIUS_TOKEN = 'MgALQlKRu6ZSuEVdf0Da29Ut5WdOJ-Xox6Cfi2L3nZZf9Uxs8dEbFD5sP2a4N2s5'
	genius  	 = lyricsgenius.Genius(GENIUS_TOKEN)
	return genius

def search(geniusSession, songName, songArtist):
	genius = connect()
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

