from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

clientID = ""
client_secret = ""
redirect_URL = "http://example.com"

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope = scope,
        redirect_uri = redirect_URL,
        client_id = clientID,
        client_secret = client_secret,
        cache_path = "token.txt",
        username = "Adrian Nip"
    )
)

user_id = sp.current_user()["id"]

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

url = f"https://www.billboard.com/charts/hot-100/{year}"
#url = f"https://www.billboard.com/charts/hot-100/2000-04-27"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}


response = requests.get(url=url, headers = header)

billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)


song_uris = []
for song in song_names:
    result = sp.search(f"track: {song}", type='track', market=None)
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

# playlist_add_items(playlist_id, items, position=None)
# user_playlist_add_tracks(user, playlist_id, tracks, position=None)
# user_playlist_create(user, name, public=True, description='')

playlist = sp.user_playlist_create(user_id,f"{year} Top 100", public = None, description = f"Top 100 Songs of {year}")
sp.playlist_add_items(playlist_id = playlist["id"], items=song_uris)