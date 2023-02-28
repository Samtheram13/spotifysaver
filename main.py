import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#gets auth for accessing spotify api
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="b8406ed4ca20481889faf98255ed51a9",
                                                        client_secret="9507255eb988446c863fda4af6f9ee7e"))
UN = input('User ID:')                                                   

#list user playlists
dictPL = sp.user_playlists(user=UN, limit=50)

for x in dictPL["items"]:
	print(x["name"], x["id"])
 
ID = input("Enter Playlist ID:")
PI = sp.playlist_items(playlist_id=ID)


