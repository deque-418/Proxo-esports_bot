import discord
from discord.ext import commands
from tabulate import tabulate
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Create an empty schedule list
schList = []

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def status(ctx):
    await ctx.send(f"{bot.user.name} is now online")

@bot.command()
async def addevent(ctx, event_name, event_time):
    # Add event to the schedule
    global schList  # Access the global schList
    schList.append([event_name, event_time])
    await ctx.send(f"Event '{event_name}' added to the schedule.")

@bot.command()
async def schedule(ctx):
    # Create a list of headers for the table
    headers = ["Event Name", "Event Time"]

    # Convert the schedule to a table string with a thin border
    table = tabulate(schList, headers=headers, tablefmt="fancy_grid")

    await ctx.send(f"Your schedule:\n```{table}```")



bot.run(os.getenv('TOKEN'))
