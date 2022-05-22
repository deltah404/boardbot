import discord
import os
from decouple import config

bot = discord.Bot()

@bot.event
async def on_ready():
    print(':)')
    
@bot.slash_command(guild_ids=[977514545746685992])
async def ping(ctx):
    await ctx.respond('pong')

bot.run(os.getenv("BOT_TOKEN") or config("BOT_TOKEN"))
