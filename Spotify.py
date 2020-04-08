import os
import json
import spotipy
from spotipy import util 

def connect():
	# token = util.prompt_for_user_token('julio_jobs', "user-read-currently-playing user-read-playback-state user-modify-playback-state playlist-modify-public" )
	# spotify = spotipy.Spotify(auth=token)	
    SPOTIPY_CLIENT_ID       = os.environ.get('SPOTIPY_CLIENT_ID')
    SPOTIPY_CLIENT_SECRET   = os.environ.get('SPOTIPY_CLIENT_SECRET')
    SPOTIPY_REDIRECT_URI    = os.environ.get('SPOTIPY_REDIRECT_URI')
    spotify = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(SPOTIPY_CLIENT_ID,
																SPOTIPY_CLIENT_SECRET,
																SPOTIPY_REDIRECT_URI,
																scope="user-read-currently-playing user-read-playback-state user-modify-playback-state playlist-modify-public",
																username='julio_jobs'))
    return spotify

def currentSong(spotifySession):
    spotify = spotifySession
    song  = spotify.current_user_playing_track()

    if song:
        songName      = song['item']['name'].split('(')[0].strip()
        songArtist    = [artist['name'] for artist in song['item']['artists']][0]
        songFeatures  = [artist['name'] for artist in song['item']['artists']][1:]

        if songFeatures != []:
            featuredArtist = (', ').join(songFeatures)
            featuredArtistHashTag = ('').join(['#'+artist.replace(' ', '') for artist in songFeatures])
            songInfo = '{} By {} ft. {}\n#{} {} \n@barz_bot'.format(songName, songArtist, featuredArtist, (songArtist).replace(' ', ''), featuredArtistHashTag)
        else:
            songInfo = '{} By {}\n#{} @barz_bot'.format(songName, songArtist, (songArtist).replace(' ', ''))

        return {'name'      : songName,
                'artist'    : songArtist,
                'features'  : songFeatures,
                'barzBot'   : songInfo 
               }
    else:
        return None

def playback(spotifySession):
    spotify = spotifySession
    spotifyState = spotify.current_playback()

    if spotifyState:
        playbackState = spotifyState['is_playing']

        if playbackState:
            spotify.pause_playback()
            return {'state': ["Pausing Yams :("]}
        else:
            spotify.start_playback()
            return {'state': ["Loading Yams!"]}
    else:
        devices = spotify.devices()
        if devices['devices']:          
            deviceID = devices['devices'][0]['id']
            deviceName = devices['devices'][0]['name']
            try:
                spotify.start_playback(device_id=deviceID)
                return {'state': ["Starting Up!"]}
            except:
                return {'state': ["Turn On Spotify!", "No Active Device"]}
        else:
            return {'state': ["Turn On Spotify!", "No Active Device"]}



def previousSong(spotifySession):
    spotify = spotifySession
    spotifyState = spotify.current_playback()

    if spotifyState:
        spotify.previous_track()
        return {'state': ["That Yam Go HARD", "RUN IT BACK!"]}
    else:
        return {'state': ["Turn On Spotify!"]}


def nextSong(spotifySession):
    spotify = spotifySession
    spotifyState = spotify.current_playback()

    if spotifyState:
        spotify.next_track()
        return {'state': ["Next Yam", "Coming Up!"]}
    else:
        return {'state': ["Turn On Spotify!"]}

def volumeUp(spotifySession):
    spotify = spotifySession
    spotifyState = spotify.current_playback()

    if spotifyState:
        volumePercent = spotifyState['device']['volume_percent']
        deviceType = spotifyState['device']['type']

        if deviceType == 'Computer':
            if volumePercent <= 95:
                updateVolume = volumePercent+5
                spotify.volume(volume_percent=updateVolume)
                return {'state': ["Cranking It Up!", "Volume @ {}%".format(updateVolume)]}

            elif volumePercent > 95:
                updateVolume = 100
                spotify.volume(volume_percent=updateVolume)
                return {'state': ["MAXED OUT SHESH!", "Volume @ {}".format(updateVolume)]}

        elif deviceType == 'Smartphone':
            return {'state': ["Can't control", "this device :("] }
    else:
        return {'state': ["Turn On Spotify!"]}


def volumeDown(spotifySession):
    spotify = spotifySession
    spotifyState = spotify.current_playback()

    if spotifyState:
        volumePercent = spotifyState['device']['volume_percent']
        deviceType = spotifyState['device']['type']

        if deviceType == 'Computer':    
            if volumePercent >= 5:
                updateVolume = volumePercent-5
                spotify.volume(volume_percent=updateVolume)
                return {'state': ["Down It Goes :(", "Volume @ {}%".format(updateVolume)]}

            elif volumePercent < 5:
                updateVolume = 0
                spotify.volume(volume_percent=updateVolume)
                return {'state': ["Is Like That :(", "Volume @ {}%".format(updateVolume)]}

        elif deviceType == 'Smartphone':
            return {'state': ["Can't control", "this device :("] }
    else:
        return {'state': ["Turn On Spotify!"]}

def addToPlaylist(spotifySession):
    spotify = spotifySession
    spotifyState = spotify.current_playback()

    if spotifyState:    
        currentSongName = spotifyState['item']['name'].split('(')[0].strip()
        currentSongURI = spotifyState['item']['uri']

        playlistSongs = spotify.user_playlist_tracks('julio_jobs', '5H89uOgCVGdDrCBg211Sio')
        playlistSongsURIs = [song['track']['uri'] for song in playlistSongs['items'] ] 


        if currentSongURI not in playlistSongsURIs:
            spotify.user_playlist_add_tracks('julio_jobs', '5H89uOgCVGdDrCBg211Sio', [currentSongURI] )
            return {'state': ["A Keeper! Adding", "To Playlist"]}
        else:
            return {'state': ["Already On The", "Playlist playa!"]}
    else:
        return {'state': ["Turn On Spotify!"]}
