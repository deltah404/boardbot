import json
import requests
import os
try:
    from decouple import config
except:
    pass

token = os.getenv("GH_AUTH") or config("GH_AUTH")
gist_id = "214ea2b907d32934cb080917af3b2674"

def get_economy():
    return json.loads(requests.get(f'https://api.github.com/gists/{gist_id}').json()['files']['boardbot_economy.json']['content'])

def update_economy(updated_economy: list):
    

    headers = {'Authorization': f'token {token}'}
    r = requests.patch(f'https://api.github.com/gists/{gist_id}', json={'files':{'boardbot_economy.json':{"content":json.dumps(updated_economy)}}}, headers=headers)
    print(r.json())