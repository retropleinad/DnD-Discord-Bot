import os

import discord
from dotenv import load_dotenv

load_dotenv()
DISC_TOKEN = os.getenv("DISCORD_TOKEN")

disc = discord.Client()

