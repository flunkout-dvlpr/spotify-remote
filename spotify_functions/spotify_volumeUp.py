import json
import spotipy
from spotipy import util 

def connect():
	token = util.prompt_for_user_token('julio_jobs', "user-read-currently-playing user-read-playback-state user-modify-playback-state playlist-modify-public" )
	spotify = spotipy.Spotify(auth=token)
	return spotify

def volumeUp():
	spotify = connect()
	getState = spotify.current_playback()
	deviceType = getState['device']['type']

	if deviceType == 'Computer':
		volumePercent = getState['device']['volume_percent']

		if volumePercent <= 95:
			updateVolume = volumePercent+5
			spotify.volume(volume_percent=updateVolume)
			return {'state': "Cranking It Up! Volume @ {}%".format(updateVolume)}

		elif volumePercent > 95:
			updateVolume = 100
			spotify.volume(volume_percent=updateVolume)
			return {'state': "MAXED OUT SHEESH! Volume @ {}".format(updateVolume)}
			
	elif deviceType == 'Smartphone':
		return {'state': "Sorry can't control this device" }
