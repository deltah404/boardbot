import json
import requests
import os
try:
    from decouple import config
except ModuleNotFoundError:
    pass

gist_id = "214ea2b907d32934cb080917af3b2674"

def get_economy():
    return json.loads(requests.get(f'https://api.github.com/gists/{gist_id}').json()['files']['boardbot_economy.json']['content'])

try: gh_auth = config("GH_AUTH")
except: gh_auth = os.getenv("GH_AUTH") 

def update_economy(updated_economy: list):
    headers = {'Authorization': f'token {gh_auth}'}
    r = requests.patch(f'https://api.github.com/gists/{gist_id}', json={'files':{'boardbot_economy.json':{"content":json.dumps(updated_economy)}}}, headers=headers)
    print(r.json())