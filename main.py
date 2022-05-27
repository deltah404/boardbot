import discord
import os
import json
from dotenv import load_dotenv
try:
    from decouple import config, UndefinedValueError   # for canary version token
except ModuleNotFoundError:
    pass                                               # not necessary for public version

load_dotenv()
try:
    bot_token = config("BOT_TOKEN", config("C_BOT_TOKEN"))
except UndefinedValueError:
    bot_token = config("BOT_TOKEN")

bot = discord.Bot()
with open('admin.json') as fp:
    sc_guilds = json.load(fp)["slash_command_guilds"]

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')

for module in os.listdir('./cogs'):
    if module.endswith('.py'):
        bot.load_extension(f'cogs.{module[:-3]}')

bot.run(bot_token)