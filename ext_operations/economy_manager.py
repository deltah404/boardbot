import json
import requests
import os
import dotenv
try:
    from decouple import config, UndefinedValueError
except ModuleNotFoundError:
    pass

env_values = dict(dotenv.dotenv_values(".env"))
gist_id = "214ea2b907d32934cb080917af3b2674"

try:
    try:
        print('Primary source')
        gh_auth = env_values["GH_AUTH"]
    except KeyError:
        print('Primary source failed, trying secondary source')
        gh_auth = os.environ.get("GH_AUTH")
except TypeError:
    gh_auth = os.getenv("GH_AUTH")

def get_economy():
    return json.loads(requests.get(f'https://api.github.com/gists/{gist_id}').json()['files']['boardbot_economy.json']['content'])


def update_economy(updated_economy: list): 
    headers = {'Authorization': f'token {gh_auth}'}
    r = requests.patch(f'https://api.github.com/gists/{gist_id}', json={'files': {
                       'boardbot_economy.json': {"content": json.dumps(updated_economy)}}}, headers=headers)
    print(r.json())
