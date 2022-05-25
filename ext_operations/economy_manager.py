import json
import requests
import os
try:
    from decouple import config, UndefinedValueError
except ModuleNotFoundError:
    pass

gist_id = "214ea2b907d32934cb080917af3b2674"

try:
    gh_auth = config("GH_AUTH")
except UndefinedValueError:
    gh_auth = os.environ["GH_AUTH"]

def get_economy():
    return json.loads(requests.get(f'https://api.github.com/gists/{gist_id}').json()['files']['boardbot_economy.json']['content'])


def update_economy(updated_economy: list):
    headers = {'Authorization': f'token {gh_auth}'}
    r = requests.patch(f'https://api.github.com/gists/{gist_id}', json={'files': {
                       'boardbot_economy.json': {"content": json.dumps(updated_economy)}}}, headers=headers)
    print(r.json())
