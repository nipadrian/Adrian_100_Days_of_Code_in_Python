from bs4 import BeautifulSoup
import requests

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

#url = f"https://www.billboard.com/charts/hot-100/{year}"
#url = f"https://www.billboard.com/charts/hot-100/2000-04-27"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + year

response = requests.get(url=url, headers = header)

billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)