import discord
from ext_operations import economy_manager as ecom
from discord.ext import commands

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def balance(self, ctx, user: discord.Option(discord.Member, "User", default="")):
        if user == "":
            user = ctx.author

        try:
            balance = ecom.get_economy()["users"][str(user.id)]
        except KeyError:
            balance = 0

        embed = discord.Embed(title=f"{user.name}'s Balance")
        embed.add_field(name="Coins", value=f':coin: {balance}', inline=False)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Economy(bot))