import requests
from dotenv import load_dotenv
import os

load_dotenv()

cookies = {
    '__dcfduid': '78bca417cd6f263ec54aae00be5850eb',
    '__sdcfduid': 'c699f7a01e3211eca5a2c57b522a4a13beb34ed2f673956221ea7bdb703fd426751cda7dd5f3ac0feed84be08eae4ec1',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Tue+Dec+21+2021+12%3A46%3A10+GMT%2B0100+(czas+%C5%9Brodkowoeuropejski+standardowy)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0&AwaitingReconsent=false&geolocation=PL%3B22',
    'OptanonAlertBoxClosed': '2021-11-30T16:44:24.524Z',
    'locale': 'en-GB',
}

headers = {
        #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Accept': '*/*',
        'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Authorization': os.environ["TOKEN"],
        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJwbCIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk1LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTUuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk1LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3LnRhZWhhdHlwZXMuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cudGFlaGF0eXBlcy5jb20iLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA4ODA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        'X-Discord-Locale': 'en-GB',
        'X-Debug-Options': 'bugReporterEnabled',
        'Origin': 'https://discord.com',
        'Alt-Used': 'discord.com',
        'Connection': 'keep-alive',
        'Referer': 'https://discord.com/channels/556568090624786460/789086564500111410',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'DNT': '1',
        'Sec-GPC': '1',
        'TE': 'trailers',
    }

def set_status(status):
    data = '{"custom_status":{"text":"'+str(status)+'"}}'
    try:
        response = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, cookies=cookies, data=data)
    except:
        print("Cannot change the Discord status!")

def set_status(status, emoji):
    data = '{"custom_status":{"text":"'+str(status)+'", "emoji_name":"'+emoji+'"}}'
    try:
        response = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, cookies=cookies, data=data.encode('utf-8'))
    except:
        print("Cannot change the Discord status!")

def clear_status():
    data = '{"custom_status":null}'
    try:
        response = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, cookies=cookies, data=data)
    except:
        print("Cannot change the Discord status!")
