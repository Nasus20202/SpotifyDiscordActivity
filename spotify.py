from asyncio.subprocess import Process
import threading
import os
import requests
from dotenv import load_dotenv
import nest_asyncio
import asyncio

load_dotenv()
nest_asyncio.apply()

def refresh_access_token():
    refresh_token = os.environ["SPOTIFY_REFRESH_TOKEN"]
    params = (
        ('refresh_token', refresh_token),
    )
    response = requests.get(os.environ["TOKEN_GENERATOR_SERVER"] + '?refresh_token=' + refresh_token)
    os.environ["SPOTIFY"] = response.json()["access_token"]

refresh_access_token()

def __milis_to_time__(miliseconds):
    minutes = miliseconds // 60000
    seconds = (miliseconds - minutes * 60000) // 1000
    time = ""
    if(minutes < 10):
        time = time + '0'
    time = time + str(minutes) + ":"
    if(seconds < 10):
        time = time + '0'
    time = time + str(seconds)
    return time

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

def get_album_covers():
    data = get_current_spotify_info()
    if(data[0]!=200):
        return
    images = []
    for image in data[1]["item"]["album"]["images"]:
        images.append(image["url"])
    return images

def get_milliseconds():
    data = get_current_spotify_info()
    if(data[0]!=200):
        return 0
    else:
        return data[1]["progress_ms"]

def get_progress():
    data = get_current_spotify_info()
    if(data[0]!=200):
        return
    return __milis_to_time__(data[1]["progress_ms"])

def get_duration():
    data = get_current_spotify_info()
    if(data[0]!=200):
        return
    return __milis_to_time__(data[1]["item"]["duration_ms"])
    

def get_response_code():
    data = get_current_spotify_info()
    return data[0]