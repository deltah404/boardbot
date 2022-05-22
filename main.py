import discord
import os
from decouple import config

bot = discord.Bot()
sc_guilds = [977514545746685992]

@bot.event
async def on_ready():
    print(':)')
    
@bot.slash_command(guild_ids=sc_guilds)
async def ping(ctx):
    await ctx.respond('pong')

bot.run(os.getenv("BOT_TOKEN") or config("BOT_TOKEN"))
