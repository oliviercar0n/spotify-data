import spotipy
import spotipy.util as util
import requests
import pandas as pd
import datetime
import json
import os

client_id = '###'
client_secret = '###'
redirect_uri = 'http://localhost:8080'

username = '###'
scope = 'user-read-recently-played'

try:
    token = util.prompt_for_user_token(username, scope, client_id = client_id, client_secret=client_secret,redirect_uri=redirect_uri)
except Exception as e:
    print(str(datetime.datetime.now()) + "   Token failed")
    print(e)
    
base_url = 'https://api.spotify.com/'
endpoint = 'v1/me/player/recently-played'
url = base_url + endpoint

params = {'limit':50}
headers = {'Authorization': 'Bearer {0}'.format(token)}
args = dict(params=params)

request_session = requests.Session()
response = request_session.request("GET",url,headers=headers, **args)

ts = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

with open(f'json/{ts}.json', 'w') as f:
    json.dump(response.json(),f)
