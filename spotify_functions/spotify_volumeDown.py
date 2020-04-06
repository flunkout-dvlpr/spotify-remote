import json
import spotipy
from spotipy import util 

def connect():
	token = util.prompt_for_user_token('julio_jobs', "user-read-currently-playing user-read-playback-state user-modify-playback-state playlist-modify-public" )
	spotify = spotipy.Spotify(auth=token)
	return spotify

def volumeDown():
	spotify = connect()
	getState = spotify.current_playback()
	volumePercent = getState['device']['volume_percent']
	
	if volumePercent >= 5:
		updateVolume = volumePercent-5
		spotify.volume(volume_percent=updateVolume)
		return {'state': "Turning It Down :( Volume @ {}%".format(updateVolume)}

	elif volumePercent < 5:
		updateVolume = 0
		spotify.volume(volume_percent=updateVolume)
		return {'state': "Is Like That :( Volume @ {}%".format(updateVolume)}