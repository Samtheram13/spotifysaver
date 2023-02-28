import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#gets auth for accessing spotify api
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="9f77fac387634741a99fb710bc910565",
                                                        client_secret="f2f248c7799e4b0fb34a91f960001974"))
UN = input('User ID:')                                                   

#list user playlists
dictPL = sp.user_playlists(user=UN, limit=50)

for x in dictPL["items"]:
	print(x["name"], x["id"])
