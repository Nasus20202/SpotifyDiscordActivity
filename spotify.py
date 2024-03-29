import asyncio
import os
import requests
from dotenv import load_dotenv

load_dotenv()

async def refresh_access_token():
    refresh_token = os.environ["SPOTIFY_REFRESH_TOKEN"]
    params = (
        ('refresh_token', refresh_token),
    )
    try:
        response = requests.get(os.environ["TOKEN_GENERATOR_SERVER"] + '?refresh_token=' + refresh_token, timeout=3)
        os.environ["SPOTIFY"] = response.json()["access_token"]
        print("New token generated")
    except:
        print("Cannot refresh the token!")
        await asyncio.sleep(1)
        await refresh_access_token()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
task = loop.create_task(refresh_access_token())
try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass

def __milis_to_time__(miliseconds):
    minutes = miliseconds // 60000
    seconds = round((miliseconds - minutes * 60000) / 1000)
    time = ""
    if(minutes < 10):
        time = time + '0'
    time = time + str(minutes) + ":"
    if(seconds < 10):
        time = time + '0'
    time = time + str(seconds)
    return time

def get_current_spotify_info():
    try:
        response = requests.get("https://api.spotify.com/v1/me/player/currently-playing?market=PL", headers= {"Authorization" : "Bearer " + os.environ["SPOTIFY"]}, timeout=3)
    except:
        print("Cannot get data from Spotify API")
        return [404]
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

def get_album_name():
    data = get_current_spotify_info()
    if(data[0]!=200):
        return
    return data[1]["item"]["album"]["name"]

def get_milliseconds():
    data = get_current_spotify_info()
    if(data[0]!=200):
        return -1
    else:
        return data[1]["progress_ms"]

def get_duration_millis():
    data = get_current_spotify_info()
    if(data[0]!=200):
        return -1
    else:
        return data[1]["item"]["duration_ms"]

def get_progress():
    data = get_current_spotify_info()
    if(data[0]!=200):
        return -1
    return __milis_to_time__(data[1]["progress_ms"])

def get_duration():
    data = get_current_spotify_info()
    if(data[0]!=200):
        return -1
    return __milis_to_time__(data[1]["item"]["duration_ms"])
    

def get_response_code():
    data = get_current_spotify_info()
    return data[0]