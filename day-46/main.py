from bs4 import BeautifulSoup
import requests

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

#url = f"https://www.billboard.com/charts/hot-100/{year}"
url = f"https://www.billboard.com/charts/hot-100/2000-04-27"
header = {}

response = requests.get(url)

billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")
print(soup)
# song_names = soup.find_all(id = "title-of-a-story", class_ = "c-title")
# print(song_names)