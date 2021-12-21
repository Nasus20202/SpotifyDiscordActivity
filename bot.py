import discord
from dotenv import load_dotenv
import os
import spotify

load_dotenv()

print(spotify.get_response_code())
print(spotify.get_current_artists())
print(spotify.get_current_track())
print(spotify.get_album_covers())
print(spotify.get_progress())
print(spotify.get_duration())


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))


#client.run(os.environ["TOKEN"], bot=False)