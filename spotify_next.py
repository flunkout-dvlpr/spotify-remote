import json
import spotipy
from spotipy import util 

def connect():
	token = util.prompt_for_user_token('julio_jobs', "user-read-currently-playing user-read-playback-state user-modify-playback-state playlist-modify-public" )
	spotify = spotipy.Spotify(auth=token)
	return spotify

def nextSong():
	spotify = connect()
	spotify.next_track()
	return {'state': "Next Yam Coming Up!"}


# print(json.dumps(nextSong(), indent=2))


