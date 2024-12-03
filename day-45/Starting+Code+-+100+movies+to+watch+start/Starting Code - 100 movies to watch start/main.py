import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
#print(soup)

all_movies = soup.find_all(name = "h3", class_ = "title")
print(all_movies)


# for movie in all_movies:
#     text = movie.getText()
#     print(text)

movie_titles = [movie.getText() for movie in all_movies]
movies = (movie_titles[::-1])
print(movies)

with open("movies.txt",mode = "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

