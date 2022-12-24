import requests
from dotenv import load_dotenv
import os

load_dotenv()

current_status = "status"

headers = {
        'Content-Type': 'application/json',
        'Authorization': os.environ["TOKEN"]
    }

def set_status_without_emoji(status):
    global current_status
    if(current_status == status):
        return
    current_status = status
    data = '{"custom_status":{"text":"'+str(status.replace('"', "'"))+'"}}'
    try:
        response = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, data=data, timeout=3)
    except:
        print("Cannot change the Discord status!")

def set_status(status, emoji):
    global current_status
    if(status == current_status):
        return
    current_status = status
    data = '{"custom_status":{"text":"'+str(status.replace('"', "'").replace("\\", "\\\\"))+'", "emoji_name":"'+emoji+'"}}'
    try:
        response = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, data=data.encode('utf-8'), timeout=3)
    except:
        print("Cannot change the Discord status!")

def clear_status():
    global current_status
    if(current_status == ""):
        return
    current_status = ""
    data = '{"custom_status":null}'
    try:
        response = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, data=data, timeout=3)
    except:
        print("Cannot change the Discord status!")
