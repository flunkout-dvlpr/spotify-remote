import json
import spotipy
from spotipy import util 

def connect():
	token = util.prompt_for_user_token('julio_jobs', "user-read-currently-playing user-read-playback-state user-modify-playback-state playlist-modify-public" )
	spotify = spotipy.Spotify(auth=token)
	return spotify

def previousSong():
	spotify = connect()
	spotify.previous_track()
	return {'state': "That Yam Go HARD, RUN IT BACK!"}


# print(json.dumps(previousSong(), indent=2))