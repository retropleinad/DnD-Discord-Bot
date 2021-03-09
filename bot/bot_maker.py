import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

TOKEN = ""
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name="yo")
async def yo(ctx):
    await ctx.send("Enter a number")
    test = bot.wait_for("message", timeout=30)
    await ctx.send(test)

bot.run(TOKEN)

    

