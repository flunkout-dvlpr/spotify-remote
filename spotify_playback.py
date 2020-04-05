import json
import spotipy
from spotipy import util 

def connect():

	token = util.prompt_for_user_token('julio_jobs', "user-read-currently-playing user-read-playback-state user-modify-playback-state playlist-modify-public" )
	spotify = spotipy.Spotify(auth=token)
	return spotify


def playback():
	spotify = connect()

	getState = spotify.current_playback()
	playbackState = getState['is_playing']

	if playbackState:
		spotify.pause_playback()
		return {'state': "Pausing Yams :("}
	else:
		spotify.start_playback()
		return {'state': "Loading Yams!"}


# print(json.dumps(playback(), indent=2))