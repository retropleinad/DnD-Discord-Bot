import os
import sqlite3

import discord
from discord.ext import commands

from dotenv import load_dotenv

from database import inserts
from database import selects
from database import deletes
from database import updates
from database import util as db_util

from bot import error_messages
from bot import util

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

# Messages that appear when the user hits !help
help_messages = {
    "new": "Insert !new followed by the type of item, then add in the entries."
           "For example: !new region Drydock \"the main city\"",
    "list-all": "Insert !list-all followed by the type of item. For example: !list-all region",
    "select": "Insert !select followed by the type of item and the descriptors for that item. "
              "Note that a space should not exist between descriptor category and value. "
              "For example: !select region name=Drydock",
    "delete-all": "Insert !delete-all followed by the category name to clear everything from that category. "
                  "For example: !delete-all region",
    "delete": "Insert !delete followed by the type of item and the descriptors for that item. "
              "Note that a space should not exist between descriptor category and value. "
              "For example: !delete region name=Drydock",
    "edit": "Insert !select followed by the type of item and the descriptors for that item. "
            "Note that a space should not exist between descriptor category and value. "
            "Insert a : between the old descriptors and the desired changes"
            "For example: !edit region name=Drydock : name=Dockdry",
    "sqlite": "Directly run an SQLite query. Type !sqlite then follow it with the query. "
              "For example: !sqlite SELECT * FROM regions"
}


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


# Used to add a new entry to a table
@bot.command(name="new", help=help_messages["new"])
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
            inserts.insert_owner(item=args[0], pc=args[1], npc=args[2], organization=args[3])
        else:
            await ctx.send(error_messages.INVALID_CATEGORY)
    except IndexError:
        await ctx.send(error_messages.ENTRY_LENGTH)


# List every entry in a table
@bot.command(name="list-all", help=help_messages["list-all"])
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
    except discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send(error_messages.INVALID_CATEGORY)


# Select an entry from a table
@bot.command(name="select", help=help_messages["select"])
async def select(ctx, table, *args):
    try:
        conditions = util.trim_args(args)
        output = selects.select(table, conditions)
        await ctx.send(output)
    except IndexError:
        await ctx.send(error_messages.CONDITION_SYNTAX)
    except sqlite3.OperationalError:
        await ctx.send(error_messages.INVALID_CATEGORY)
    except discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send(error_messages.INVALID_CATEGORY)


# Delete every entry in a table
@bot.command(name="delete-all", help=help_messages["delete-all"])
async def delete_all(ctx, table):
    try:
        deletes.delete_all(table)
        await ctx.send("Successfully deleted all from: " + table)
    except sqlite3.OperationalError:
        await ctx.send(error_messages.INVALID_CATEGORY)
    except discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send(error_messages.INVALID_CATEGORY)


# Delete a particular entry in a table
@bot.command(name="delete", help=help_messages["delete"])
async def delete(ctx, table, *args):
    try:
        conditions = util.trim_args(args)
        deletes.delete(table, conditions)
        await ctx.send("Deleted Successfully!")
    except IndexError:
        await ctx.send(error_messages.CONDITION_SYNTAX)
    except sqlite3.OperationalError:
        await ctx.send(error_messages.INVALID_CATEGORY)
    except discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send(error_messages.INVALID_CATEGORY)


# Edit an entry in a table
@bot.command(name="edit", help=help_messages["edit"])
async def edit(ctx, table, *args):
    try:
        entries = util.split_tuple(args, ":")
        conditions = util.trim_args(entries[0])
        changes = util.trim_args(entries[1])
        updates.update(table, changes=changes, conditions=conditions)
        await ctx.send("Changed data successfully!")
    except IndexError:
        await ctx.send(error_messages.CONDITION_SYNTAX)
    except sqlite3.OperationalError:
        await ctx.send(error_messages.INVALID_CATEGORY)
    except discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send(error_messages.INVALID_CATEGORY)


# Run an SQLite query from Discord
@bot.command(name="sqlite", help=help_messages["sqlite"])
async def sqlite(ctx, *args):
    query = ""
    for arg in args:
        query += arg
        query += " "
    try:
        db_util.commit_query(query)
        await ctx.send("Query operated successfully")
    except sqlite3.OperationalError:
        await ctx.send(error_messages.QUERY_SYNTAX)
    except discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send(error_messages.INVALID_CATEGORY)


bot.run(TOKEN)
