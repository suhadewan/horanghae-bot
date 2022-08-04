from ast import alias
from nextcord import Intents
from nextcord.ext import commands
import requests, json, random
import os

links = json.load(open("gifs.json"))
 
intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('Hello!')
    
@bot.command(name="gif", aliases=["horanghae"])
async def Gif(ctx):
    await ctx.send(random.choice(links[ctx.invoked_with]))
    
@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")
    
if __name__ == '__main__':
    bot.run(os.environ["DISCORD_TOKEN"])
    
