import requests
from dotenv import load_dotenv
import os

load_dotenv()


headers = {
        'Content-Type': 'application/json',
        'Authorization': os.environ["TOKEN"]
    }

def set_status_without_emoji(status):
    data = '{"custom_status":{"text":"'+str(status)+'"}}'
    try:
        response = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, data=data)
    except:
        print("Cannot change the Discord status!")

def set_status(status, emoji):
    data = '{"custom_status":{"text":"'+str(status)+'", "emoji_name":"'+emoji+'"}}'
    try:
        response = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, data=data.encode('utf-8'))
    except:
        print("Cannot change the Discord status!")

def clear_status():
    data = '{"custom_status":null}'
    try:
        response = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, data=data)
    except:
        print("Cannot change the Discord status!")
