import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

TOKEN = "ODE4NjI0MTQ0MTE4Nzc1ODA5.YEaxJQ.L-WmR64YCcsjECV-a-a_pxaP-7k"
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name="yo")
async def yo(ctx):
    await ctx.send("yo")


bot.run(TOKEN)

    

