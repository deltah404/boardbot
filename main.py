from email.policy import default
import discord
import os
import json
from dotenv import load_dotenv
try:
    from decouple import config, UndefinedValueError   # for canary version token
except ModuleNotFoundError:
    pass                                               # not necessary for public version

bot = discord.Bot()
with open('admin.json') as fp:
    sc_guilds = json.load(fp)["slash_command_guilds"]

try:
    bot_token = BOT_TOKEN()
except KeyError:
    bot_token = config("BOT_TOKEN")
    

for module in os.listdir('./cogs'):
    if module.endswith('.py'):
        bot.load_extension(f'cogs.{module[:-3]}')

print(str(bot_token))
