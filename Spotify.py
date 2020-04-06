import json
import spotipy
from spotipy import util 

def connect():
	token = util.prompt_for_user_token('julio_jobs', "user-read-currently-playing user-read-playback-state user-modify-playback-state playlist-modify-public" )
	spotify = spotipy.Spotify(auth=token)
	return spotify

def currentSong(spotifySession):
	spotify = spotifySession
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

def playback(spotifySession):
	spotify = spotifySession

	getState = spotify.current_playback()
	playbackState = getState['is_playing']

	if playbackState:
		spotify.pause_playback()
		return {'state': "Pausing Yams :("}
	else:
		spotify.start_playback()
		return {'state': "Loading Yams!"}

def previousSong(spotifySession):
	spotify = spotifySession
	spotify.previous_track()
	return {'state': "That Yam Go HARD, RUN IT BACK!"}

def nextSong(spotifySession):
	spotify = spotifySession
	spotify.next_track()
	return {'state': "Next Yam Coming Up!"}

def volumeUp(spotifySession):
	spotify = spotifySession
	getState = spotify.current_playback()
	volumePercent = getState['device']['volume_percent']

	if volumePercent <= 95:
		updateVolume = volumePercent+5
		spotify.volume(volume_percent=updateVolume)
		return {'state': "Cranking It Up! Volume @ {}%".format(updateVolume)}

	elif volumePercent > 95:
		updateVolume = 100
		spotify.volume(volume_percent=updateVolume)
		return {'state': "MAXED OUT SHEESH! Volume @ {}".format(updateVolume)}

def volumeDown(spotifySession):
	spotify = spotifySession
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

def addToPlaylist(spotifySession):
	spotify = spotifySession

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

