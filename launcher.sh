#!/bin/bash
#launcher.sh

cd /
export SPOTIPY_CLIENT_ID='7035733de1f341139a9e38d75045cdfa'
export SPOTIPY_CLIENT_SECRET='0393e2acca9a4ad3a6385608b051e3eb'
export SPOTIPY_REDIRECT_URI='http://localhost/'
cd /
cd home/pi/Desktop/spotify-remote/remote_env
. bin/activate
cd /
cd home/pi/Desktop/spotify-remote
python3 remote.py