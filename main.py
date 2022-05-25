from email.policy import default
import discord
import os
import json
try:
    from decouple import config, UndefinedValueError   # for canary version token
except ModuleNotFoundError:
    pass                                               # not necessary for public version

bot = discord.Bot()
with open('admin.json') as fp:
    sc_guilds = json.load(fp)["slash_command_guilds"]

if ".env" not in os.listdir("."):
    bot_token = os.getenv("BOT_TOKEN")
else:
    bot_token = config("BOT_TOKEN", default=os.getenv("BOT_TOKEN"))   

for module in os.listdir('./cogs'):
    if module.endswith('.py'):
        bot.load_extension(f'cogs.{module[:-3]}')

bot.run(bot_token)