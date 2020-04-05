import json
import spotipy
from spotipy import util 

def connect():
	token = util.prompt_for_user_token('julio_jobs', "user-read-currently-playing user-read-playback-state user-modify-playback-state playlist-modify-public" )
	spotify = spotipy.Spotify(auth=token)
	return spotify

def addToPlaylist():
	spotify = connect()

	getState = spotify.current_playback()
	currentSongName = getState['item']['name'].split('(')[0].strip()
	currentSongURI = getState['item']['uri']

	playlistSongs = spotify.user_playlist_tracks('julio_jobs', '5H89uOgCVGdDrCBg211Sio')
	playlistSongsURIs = [song['track']['uri'] for song in playlistSongs['items'] ] 


	if currentSongURI not in playlistSongsURIs:
		spotify.user_playlist_add_tracks('julio_jobs', '5H89uOgCVGdDrCBg211Sio', [currentSongURI] )
		return {'state': " '{}', Is Definitely A Keeper! Adding To Playlist".format(currentSongName)}
	else:
		return {'state': " '{}', Already On The Playlist Playa!".format(currentSongName)}

# print(json.dumps(addToPlaylist(), indent=2))