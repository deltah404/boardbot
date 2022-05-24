import discord
import random
from main import sc_guilds
from discord.ext import commands

class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(guild_ids=sc_guilds)
    async def coinflip(self, ctx):
        await ctx.respond(f':coin: It\'s {random.choice(["heads","tails"])}!')

def setup(bot):
    bot.add_cog(Coinflip(bot)) 