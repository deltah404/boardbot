import discord
import os
try:
    from decouple import config   # for canary version token
except ModuleNotFoundError:
    pass                          # not necessary for public version

bot = discord.Bot()
sc_guilds = [977514545746685992]

for module in os.listdir('./cogs'):
    if module.endswith('.py'):
        bot.load_extension(f'cogs.{module[:-3]}')

bot.run(os.getenv("BOT_TOKEN") or config("BOT_TOKEN"))
