from bs4 import BeautifulSoup
import requests
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from client import CLIENT_ID, CLIENT_SECRET    #gitignored 

date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD : ")
URL = "https://www.billboard.com/charts/hot-100/" + date
CLIENT_ID = CLIENT_ID
CLIENT_SECRET = CLIENT_SECRET

#spotify authentication

auth = SpotifyOAuth(client_id= CLIENT_ID, client_secret= CLIENT_SECRET,
                    redirect_uri= "http://example.com",
                    scope= "playlist-modify-private",
                    show_dialog= True,
                    cache_path = "token.txt",
                    username= "VSR")

sp = spotipy.Spotify(auth_manager= auth)

user_id = sp.current_user()["id"]

#scraping top 100 songs from the billboard

billboard = requests.get(URL)

content = billboard.text

soup = BeautifulSoup(content, "html.parser")

songs = soup.select("li ul li h3")
list_of_songs = []

#creating a list of song uris

for i in songs:
    a = i.getText()
    list_of_songs.append(a.strip())
    
year = date.split("-")[0]
song_uri = []
skipped = 0

for song in list_of_songs:
    result = sp.search(q = f"track : {song} year : {year}", type= "track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)

    except IndexError:
        skipped +=1 

#creating a playlist and adding songs to it

playlist = sp.user_playlist_create(user= user_id, name = f"{date} Billboard 100", description= "test album", public= False)
pprint(playlist)

sp.playlist_add_items(playlist_id= playlist["id"], items= song_uri)

print(f"Skipped {skipped} songs as they arent available on spotify")









    








