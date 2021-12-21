import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_current_spotify_info():
    response = requests.get("https://api.spotify.com/v1/me/player/currently-playing?market=PL", headers= {"Authorization" : "Bearer " + os.environ["SPOTIFY"]})
    if(response.status_code != 200):
        return [response.status_code, {}]
    return [response.status_code, response.json()]

def get_current_artists():
    data = get_current_spotify_info()
    if(data[0]!=200):
        return
    artists = ""
    first = True
    for artist in data[1]["item"]["artists"]:
        if(not first):
            artists = artists + ", "
        first = False
        artists = artists + artist["name"]
    return artists

def get_current_track():
    data = get_current_spotify_info()
    if(data[0]!=200):
        return
    return data[1]["item"]["name"]

def get_response_code():
    data = get_current_spotify_info()
    return data[0]