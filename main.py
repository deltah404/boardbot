import discord
import os
try:
    from decouple import config, UndefinedValueError   # for canary version token
except ModuleNotFoundError:
    pass                                               # not necessary for public version

bot = discord.Bot()
sc_guilds = [977514545746685992]

try:
    bot_token = config("BOT_TOKEN")
except UndefinedValueError:
    bot_token = os.getenv("BOT_TOKEN")

for module in os.listdir('./cogs'):
    if module.endswith('.py'):
        bot.load_extension(f'cogs.{module[:-3]}')

bot.run(bot_token)
