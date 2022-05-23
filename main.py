import discord
import os
from decouple import config

bot = discord.Bot()
sc_guilds = [977514545746685992]

@bot.event
async def on_ready():
    print(':)')
    
@bot.slash_command(name='test', guild_ids=sc_guilds)
async def ping(ctx):
    await ctx.respond(f'yo {ctx.author.mention} your bot works')

bot.run(os.getenv("BOT_TOKEN") or config("BOT_TOKEN"))
