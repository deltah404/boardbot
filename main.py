from email.policy import default
import discord
import os
import json
from dotenv import load_dotenv
try:
    from decouple import config   # for canary version token
except ModuleNotFoundError:
    pass                          # not necessary for public version

bot = discord.Bot()
with open('admin.json') as fp:
    sc_guilds = json.load(fp)["slash_command_guilds"]

try:
    bot_token = BOT_TOKEN 
except NameError:
    load_dotenv()
    bot_token = os.getenv("BOT_TOKEN")

for module in os.listdir('./cogs'):
    if module.endswith('.py'):
        bot.load_extension(f'cogs.{module[:-3]}')

bot.run(bot_token)
