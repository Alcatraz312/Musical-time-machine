from bs4 import BeautifulSoup
import requests
from pprint import pprint

year = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD : ")

billboard = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/")

content = billboard.text

soup = BeautifulSoup(content, "html.parser")

movies = soup.find_all(name= "h3", id = "title-of-a-story")

for i in movies:
    print(i.getText())
    



