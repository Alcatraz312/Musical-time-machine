from bs4 import BeautifulSoup
import requests
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth


URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"
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
print(user_id)

#scraping top 100 songs from the billboard

year = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD : ")
billboard = requests.get(URL)

content = billboard.text

soup = BeautifulSoup(content, "html.parser")

movies = soup.find_all(name= "h3", id = "title-of-a-story")

for i in movies:
    print(i.getText())




