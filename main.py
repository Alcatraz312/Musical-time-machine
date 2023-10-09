from src.playlist import fetch_songs, create_playlist
from src.spotify import SpotifyInit
import json

date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD : ")  #taking input

creds = json.load(open('config.json'))
CLIENT_ID = creds['CLIENT_ID']
CLIENT_SECRET = creds['CLIENT_SECRET']
REDIRECT_URI = creds['REDIRECT_URI']
USERNAME = creds['USERNAME']


spotify = SpotifyInit(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI,USERNAME)
spotify.spotify_auth()
spotify.set_user()

list_of_songs = fetch_songs(date)
create_playlist(date, list_of_songs, spotify)