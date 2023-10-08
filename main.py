from bs4 import BeautifulSoup
import requests
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD : ")
URL = "https://www.billboard.com/charts/hot-100/" + date
CLIENT_ID = "3327e5f459d44dccaf9cf5041ac1fd4d"
CLIENT_SECRET = "1c50b1c4917046ab8e49ec56670b1e4a"

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


playlist = sp.user_playlist_create(user= user_id, name = "2020-02-02 Billboard 100", description= "test album", public= False)









    








