import discord
import json
from ext_operations import economy_manager as ecom
from discord.ext import commands

with open("admin.json") as fp:
    starting_balance = json.load(fp)["economy"]["starting_balance"]


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
        embed.add_field(
            name="Coins", value=f':moneybag: **{balance}**', inline=False)
        await ctx.respond(embed=embed)

    @discord.slash_command()
    async def give(self, ctx, user: discord.Option(discord.Member, "User", required=True), amount: int):
        e = ecom.get_economy()
        if str(ctx.author.id) not in e["users"].keys():
            bal = ecom.new_account(ctx.author.id)
            e = ecom.get_economy()
        else:
            bal = e["users"][str(ctx.author.id)]

        if bal < amount:
            return await ctx.respond(f':x: You don\'t have enough money!')
        elif amount <= 0:
            return await ctx.respond(f':x: You cannot send less than :moneybag: **1**')
        else:
            e["users"][str(ctx.author.id)] -= amount
            if str(user.id) not in e["users"].keys():
                ecom.new_account(user.id)
                e = ecom.get_economy()
            e["users"][str(user.id)] += amount
            ecom.update_economy(e)
            return await ctx.channel.send(f'Transferred :moneybag: from {ctx.author.mention} to {user.mention}')


def setup(bot):
    bot.add_cog(Economy(bot))
