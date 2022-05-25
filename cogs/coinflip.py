import discord
import random

from numpy import flip
from ext_operations import economy_manager as ecom
from main import sc_guilds
from discord.ext import commands


def flip_coin(guess):
    result = random.choice(["heads", "tails"])
    if result == guess:
        return True
    else:
        return False


class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(guild_ids=sc_guilds)
    async def coinflip(self, ctx, bet):
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
                select.disabled = True
                await interaction.response.edit_message(view=self)
                if flip_coin(select.values[0]):
                    await ctx.respond(f':coin: Sweet! You won {bet}!')
                else:
                    await ctx.respond(f':coin: Bad luck - you lost {bet}...')

        await ctx.respond(view=MyView())


def setup(bot):
    bot.add_cog(Coinflip(bot))
