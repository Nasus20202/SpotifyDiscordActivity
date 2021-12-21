from dotenv import load_dotenv
import spotify
import nest_asyncio
import asyncio
import activity
import math
import signal
import sys

def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        activity.clear_status()
        sys.exit(0)
 
signal.signal(signal.SIGINT, handler)

load_dotenv()
nest_asyncio.apply()

notes = ['\U0001f3b5', '\U0001f3b6']

async def update_activity(timer):
    oldTimer = timer
    await asyncio.sleep(1)
    timer = spotify.get_milliseconds()
    if(math.fabs(oldTimer - timer) < 100):
        activity.clear_status()
    else:
        await set_artists_as_activity()
    oldTimer = timer
    await asyncio.sleep(1)
    timer = spotify.get_milliseconds()
    if(math.fabs(oldTimer - timer) < 100):
        activity.clear_status()
    else:
        await set_track_as_activity()
    return timer

async def thread():
    timer = spotify.get_milliseconds()
    while True:
        timer = await update_activity(timer)
        spotify.refresh_access_token()

async def set_track_as_activity():
    presence = spotify.get_current_track()
    if(presence != None):
        activity.set_status(presence, notes[0])
    else:
        activity.clear_status()
    

async def set_artists_as_activity():
    presence = spotify.get_current_artists()
    if(presence != None):
        activity.set_status(presence, notes[1])
    else:
        activity.clear_status()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
task = loop.create_task(thread())
try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass

