import discord
import random
import json
from time import sleep
from ext_operations import economy_manager as ecom
from discord.ext import commands

with open('admin.json') as fp:
    sc_guilds = json.load(fp)["slash_command_guilds"]


def flip_coin(guess):
    result = random.choice(["Heads", "Tails"])
    if guess == result:
        return True
    else:
        return False


class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(guild_ids=sc_guilds)
    async def coinflip(self, ctx, bet: discord.Option(int)):
        if bet <= 0:
            return await ctx.respond(":coin: You have to bet at least :moneybag:1")
        conf = await ctx.channel.send(":coin: Hang on...")

        class MyView(discord.ui.View):
            @discord.ui.select(
                placeholder="Make a guess:",
                options=[
                    discord.SelectOption(
                        label="Heads"
                    ),
                    discord.SelectOption(
                        label="Tails"
                    )
                ]
            )
            async def select_callback(self, select, interaction):
                if interaction.user != ctx.author:
                    return
                select.disabled = True
                select.placeholder = select.values[0] + '!'
                await interaction.response.edit_message(view=self)

                if flip_coin(select.values[0]):
                    await ctx.respond(f':coin: Sweet! You won :moneybag:**{bet}**!')
                    e = ecom.get_economy()
                    e["users"][str(ctx.author.id)] += int(bet)
                    ecom.update_economy(e)
                else:
                    await ctx.respond(f':coin: Bad luck - you lost :moneybag:**{bet}**...')
                    e = ecom.get_economy()
                    e["users"][str(ctx.author.id)] -= int(bet)
                    ecom.update_economy(e)

        if str(ctx.author.id) not in ecom.get_economy()["users"].keys():
            ecom.new_account(ctx.author.id)
        if ecom.get_economy()["users"][str(ctx.author.id)] < int(bet):
            return await conf.edit(content=f':x: You don\'t have enough money!')
        else:
            await conf.delete()
            await ctx.respond(view=MyView())
        ecom.get_economy()


def setup(bot):
    bot.add_cog(Coinflip(bot))
