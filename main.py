from email.policy import default
import discord
import os
import json
import dotenv
try:
    from decouple import config, UndefinedValueError   # for canary version token
except ModuleNotFoundError:
    pass                                               # not necessary for public version

env_values = dict(dotenv.dotenv_values(".env"))
bot = discord.Bot()
with open('admin.json') as fp:
    sc_guilds = json.load(fp)["slash_command_guilds"]

try:
    try:
        print('Primary source')
        bot_token = env_values["BOT_TOKEN"]
    except KeyError:
        print('Primary source failed, trying secondary source')
        bot_token = os.environ.get("BOT_TOKEN")
except TypeError:
    bot_token = os.environ.get("BOT_TOKEN")
    

for module in os.listdir('./cogs'):
    if module.endswith('.py'):
        bot.load_extension(f'cogs.{module[:-3]}')

bot.run(bot_token)