import discord
import os

bot = discord.Bot()
bot_guilds = []

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    bot_guilds = [guild.id for guild in bot.guilds]

@bot.slash_command(guild_ids = bot_guilds)
async def ping(ctx):
    await ctx.respond('pong')

bot.run(os.getenv("BOT_TOKEN"))