import requests
from bs4 import BeautifulSoup
from src.spotify import SpotifyInit
from pprint import pprint

url = "https://www.billboard.com/charts/hot-100/"

def fetch_songs(date:str, url:str=url):
    url_updated = url + date
    response = requests.get(url_updated)
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    songs = soup.select("li ul li h3")
    list_of_songs = [a.getText().strip for a in songs]
    return list_of_songs

def create_playlist(date:str, list_of_songs:list, obj:SpotifyInit):
    year = date.split('-')[0]
    song_uri = []
    skipped = 0

    for song in list_of_songs:
        result = obj.sp.search(q = f"track : {song} year : {year}", type= "track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uri.append(uri)
        except:
            skipped +=1

    playlist = obj.sp.user_playlist_create(user=obj.user_id, name = f"{year} Billboard 100", description= "test album", public= False)
    pprint(playlist)

    obj.sp.playlist_add_items(playlist_id= playlist["id"], items= song_uri)

    print(f"Playlist {year} created for {obj.user_id}")
    print(f"Skipped {skipped} songs as they arent available on spotify")            

