import json
import spotipy
from spotipy import util 

def connect():
	token = util.prompt_for_user_token('julio_jobs', "user-read-currently-playing user-read-playback-state user-modify-playback-state playlist-modify-public" )
	spotify = spotipy.Spotify(auth=token)
	return spotify

def currentSong():
	spotify = connect()
	song  = spotify.current_user_playing_track()
	songName	  = song['item']['name'].split('(')[0].strip()
	songArtist	  = [artist['name'] for artist in song['item']['artists']][0]
	songFeatures = [artist['name'] for artist in song['item']['artists']][1:]

	if songFeatures != []:
		featuredArtist = (', ').join(songFeatures)
		featuredArtistHashTag = ('').join(['#'+artist.replace(' ', '') for artist in songFeatures])
		songInfo = '{} By {} ft. {}\n#{} {} \n@barz_bot'.format(songName, songArtist, featuredArtist, (songArtist).replace(' ', ''), featuredArtistHashTag)
	else:
		songInfo = '{} By {}\n#{} @barz_bot'.format(songName, songArtist, (songArtist).replace(' ', ''))
	return {'name': songName,
			'artist': songArtist,
			'features': songFeatures,
			'info': songInfo }