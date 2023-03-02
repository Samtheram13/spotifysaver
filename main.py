import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import cred
import csv
#0o3133j3p3nrq81uoex50m50h


def checkKey(dic, key):
	if key in dic.keys():
		return True
	else:
		return False


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
 client_id=cred.client_ID, client_secret=cred.client_SECRET))

userID = input("Welcome to spotify playlist seacher, what is your user ID? \n")

dictPL = sp.user_playlists(userID, limit=50)

plDIC = {}

for x in dictPL["items"]:
	plDIC[x["name"]] = x["id"]

print("Your available playlists are:")
for x in plDIC:
	print("-" + x)

print("-------------")

while (True):
	playlistSearch = input("Search for: ")
	if (checkKey(plDIC, playlistSearch)):
		break
	else:
		print("Could not be found, please try again")
		continue

# Select 4th index of plIDS for AlexWala Stream Music

dictTracks = sp.user_playlist_tracks(user="0o3133j3p3nrq81uoex50m50h",
                                     playlist_id=plDIC[playlistSearch],
                                     limit=100)

# Working the csv file

file = 'new.csv'
fields = ['trackName', 'artist']
rows = []
for y in dictTracks["items"]:
	rows.append([y["track"]["name"], y["track"]["artists"][0]["name"]])

print(rows)
with open(file, 'w') as csvfile:
	csvwriter = csv.writer(csvfile)

	csvwriter.writerow(fields)
	csvwriter.writerows(rows)
