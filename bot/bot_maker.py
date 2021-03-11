import os
import sqlite3

from discord.ext import commands

from dotenv import load_dotenv

from database import inserts
from database import selects
from database import deletes
from database import updates

from bot import error_messages
from bot import util

TOKEN = ""
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


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
            await ctx.send(error_messages.INVALID_CATEGORY)
    except IndexError:
        await ctx.send(error_messages.ENTRY_LENGTH)


@bot.command(name="list-all")
async def list_all(ctx, table):
    try:
        results = selects.select_all(table)

        titles = results["titles"]
        title_string = " | "
        for title in titles:
            title_string += title + " | "
        await ctx.send(title_string)

        data = results["data"]
        for entry in data:
            entry_string = " | "
            for point in entry:
                entry_string += str(point) + " | "
            await ctx.send(entry_string)

    except sqlite3.OperationalError:
        await ctx.send(error_messages.INVALID_CATEGORY)


@bot.command(name="select")
async def select(ctx, table, *args):
    try:
        conditions = util.trim_args(*args)
        output = selects.select(table, conditions)
        await ctx.send(output)
    except IndexError:
        await ctx.send(error_messages.CONDITION_SYNTAX)
    except sqlite3.OperationalError:
        await ctx.send(error_messages.INVALID_CATEGORY)


@bot.command(name="delete-all")
async def delete_all(ctx, table):
    try:
        deletes.delete_all(table)
        await ctx.send("Successfully deleted all from: " + table)
    except sqlite3.OperationalError:
        await ctx.send(error_messages.INVALID_CATEGORY)


@bot.command(name="delete")
async def delete(ctx, table, *args):
    try:
        conditions = util.trim_args(*args)
        deletes.delete(table, conditions)
        await ctx.send("Deleted Successfully!")
    except IndexError:
        await ctx.send(error_messages.CONDITION_SYNTAX)
    except sqlite3.OperationalError:
        await ctx.send(error_messages.INVALID_CATEGORY)


@bot.command(name="edit")
async def edit(ctx, table, *args):
    try:
        conditions = util.trim_args(*args)
    except IndexError:
        await ctx.send(error_messages.CONDITION_SYNTAX)
    except sqlite3.OperationalError:
        await ctx.send(error_messages.INVALID_CATEGORY)


bot.run(TOKEN)

    

