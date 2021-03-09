import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

from database import inserts

TOKEN = ""
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name="yo")
async def yo(ctx):
    await ctx.send("Enter a number")
    num = await bot.wait_for("Message", timeout=30)
    await ctx.send(num)


@bot.command(name="animal")
async def animal(ctx, *args):
    for arg in args:
        await ctx.send(arg)


@bot.command(name="new")
async def new(ctx, table, *args):
    try:
        table = table.lower().strip()
        if table == "region":
            inserts.insert_region(name=args[0], description=args[1])
        elif table == "location":
            inserts.insert_location(name=args[0], description=args[1], region=args[2])
        elif table == "organization":
            inserts.insert_organization(name=args[0], description=args[1], region=args[2], headquarters=args[3])
        elif table == "class":
            inserts.insert_class(name=args[0], description=args[1], source=args[2], page=args[3])
        elif table == "player-characters":
            inserts.insert_pcs(player=args[0], name=args[1], description=args[2], alive=args[3], dnd_class=args[4],
                               origin=args[5], area=args[6])
        elif table == "npcs":
            inserts.insert_npcs(name=args[0], description=args[1], region=args[2], headquarters=args[3])
        elif table == "items":
            inserts.insert_item(name=args[0], description=args[1])
        elif table == "item-owner":
            pass
        else:
            await ctx.send("Please choose an acceptable category. Available categories are : "
                           "region, location, organization, class, player-characters, npcs, items, and item-owner")
    except IndexError:
        await ctx.send("Please enter the correct amount of information for the category.")


bot.run(TOKEN)

    

