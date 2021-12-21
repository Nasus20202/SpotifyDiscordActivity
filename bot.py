import discord
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
headers = {"Authorization" : "Bearer " + os.environ["SPOTIFY"]}

def get_current_spotify_info():
    response = requests.get("https://api.spotify.com/v1/me/player/currently-playing?market=PL", headers=headers)
    data = response.json()
    return data

data = get_current_spotify_info()

#print(json.dumps(data, indent=4))
print(data["item"]["artists"][0]["name"])


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))


#client.run(os.environ["TOKEN"], bot=False)