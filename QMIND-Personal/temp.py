# testing file
from spotify_api_client import search, search_all, get
import csv


track = input("Name a song : ")

songID = search(track, 'track')
feat_csv = get(f'v1/audio-features/{songID}')

print(feat_csv)
dict_feat = csv.DictReader(feat_csv)

#for row in dict_feat:
#error    danceability = dict_feat['danceability']

#print(danceability)

