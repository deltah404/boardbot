import json
import requests
import os
import dotenv
from dotenv import load_dotenv
try:
    from decouple import config, UndefinedValueError
except ModuleNotFoundError:
    pass

env_values = dict(dotenv.dotenv_values(".env"))
gist_id = "214ea2b907d32934cb080917af3b2674"

load_dotenv()
gh_auth = os.getenv("GH_AUTH", env_values["C_GH_AUTH"])

def get_economy():
    return json.loads(requests.get(f'https://api.github.com/gists/{gist_id}').json()['files']['boardbot_economy.json']['content'])


def update_economy(updated_economy: list): 
    headers = {'Authorization': f'token {gh_auth}'}
    r = requests.patch(f'https://api.github.com/gists/{gist_id}', json={'files': {
                       'boardbot_economy.json': {"content": json.dumps(updated_economy)}}}, headers=headers)
    print(r.json())
