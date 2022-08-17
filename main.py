from email.quoprimime import header_decode
import requests
import random
import time
import os
import json
import base64

with open('config.json') as f:
    config = json.load(f)

token = config.get("token")

while True:
    os.system('title D1MOD STATUS CHANGER')
    time.sleep(10)
    headers = {{"authorization": token}, json=content}
    status = ['BY D1MOD', 'D1MOD STAUS CHANGER', 'Hello World', 'Chone Kure Sag']#Bade Xow Shte Bo Zya Ka
    pay = {"custom_status":{"text":(random.choice(status))}}
    d1mod_api = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=pay)
    
