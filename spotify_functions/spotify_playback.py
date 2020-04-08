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

	if getState:
		playbackState = getState['is_playing']

		if playbackState:
			spotify.pause_playback()
			return {'state': "Pausing Yams :("}
		else:
			spotify.start_playback()
			return {'state': "Loading Yams!"}
	else:
		devices = spotify.devices()
		if devices['devices']:			
			deviceID = devices['devices'][0]['id']
			spotify.start_playback(device_id=deviceID)
		else:
			return {'state': "Turn On Spotify!"}
