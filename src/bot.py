from discord.ext import commands
import discord

BOT_TOKEN = ""          # our token from discord here, need to hide it
CHANNEL_ID = ""         # server channel id here, need to figure out how to chat with the bot directly

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())   # command prefix is something we'll want to get rid of


# example bot actions
@bot.event
async def on_ready():
    print("Hi! ChatBot is ready.")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hi! ChatBot is ready.")

@bot.command()
async def hello(ctx):
    await ctx.send("Hey! This is a bot command response")

@bot.command()
async def add(ctx, *arr):
    result = 0
    for i in arr:
        result += int(i)
    await ctx.send(f"Result = {result}")

bot.run(BOT_TOKEN)