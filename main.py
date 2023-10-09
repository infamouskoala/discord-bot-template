import discord      # discord.py by Rapptz
from discord.ext import commands       #https://github.com/Rapptz/discord.py
from discord.client import *

prefix = "$" # bot prefix that u wanna use
token = "" # your discord bot token or user token or whatever ur using 
koala = commands.Bot(command_prefix=prefix, intents=discord.Intents.all()) # check the intents with developer portal

@koala.event
async def on_ready():   # on ready, the bot will print the following to the terminal
    print(f"-- BOT IS NOW ONLINE!--\nBot name: {koala.user}\nBot prefix: {prefix}")

@koala.command()
async def hello(ctx):             # basic command
    await ctx.reply(f"Hello <@{koala.author.id}>!")

# you can add more commands here

koala.run(token)
