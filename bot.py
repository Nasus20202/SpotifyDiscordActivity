import discord
from dotenv import load_dotenv
import os
import spotify
import threading
import asyncio

load_dotenv()

print(spotify.get_response_code())
print(spotify.get_current_artists())
print(spotify.get_current_track())
print(spotify.get_album_covers())
print(spotify.get_progress())
print(spotify.get_duration())

client = discord.Client()

async def update_activity():
    await set_track_as_activity()
    await asyncio.sleep(10)
    await set_artists_as_activity()
    await asyncio.sleep(10)

async def thread():
    while True:
        await update_activity()

async def set_track_as_activity():
    presence = spotify.get_current_track()
    if(presence == None):
        await client.change_presence(None)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=presence))

async def set_artists_as_activity():
    presence = spotify.get_current_artists()
    if(presence == None):
        await client.change_presence(None)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=presence))

@client.event
async def on_ready():
    print('Logged into Discord as {0.user}'.format(client))
    loop = asyncio.get_event_loop()
    
    task = loop.create_task(thread())
    try:
        loop.run_until_complete(task)
    except asyncio.CancelledError:
        pass



client.run(os.environ["TOKEN"], bot=False)
