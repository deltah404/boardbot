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

load_dotenv()
gh_auth = os.getenv("GH_AUTH", os.getenv("C_GH_AUTH"))


def get_economy():
    return json.loads(requests.get(f'https://api.github.com/gists/214ea2b907d32934cb080917af3b2674', headers={"Authorization": f"token {gh_auth}"}).json()["files"]["boardbot_economy.json"]["content"])


def update_economy(updated_economy: list):
    headers = {'Authorization': f'token {gh_auth}'}
    r = requests.patch(f'https://api.github.com/gists/214ea2b907d32934cb080917af3b2674', json={'files': {
                       'boardbot_economy.json': {"content": json.dumps(updated_economy, indent=4)}}}, headers=headers)


def new_account(user_id):
    with open("admin.json") as fp:
        starting_balance = json.load(fp)["economy"]["starting_balance"]
    e = get_economy()
    e["users"][str(user_id)] = starting_balance
    update_economy(e)
    return starting_balance
