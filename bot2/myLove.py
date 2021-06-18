import nest_asyncio
import discord
from discord.ext import commands
import json
import os

#intents = discord.Intents.default()
#intents.members = True

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
nest_asyncio.apply()
#prefix 命令自首
bot2 = commands.Bot(command_prefix='-')  
#,intents = intents

@bot2.event
async def on_ready():
    print('Logged in as')
    print(bot2.user.name)
    print(bot2.user.id)
    print('--------------')
    


#ctx = context(上下文)


    
@bot2.command()
async def load(ctx, extension):
    bot2.load_extension(F'bgg.{extension}')
    await ctx.send(F'Loaded {extension} done')
    
@bot2.command()
async def unload(ctx, extension):
    bot2.unload_extension(F'bgg.{extension}')
    await ctx.send(F'UnLoaded {extension} done')
    
@bot2.command()
async def reload(ctx, extension):
    bot2.reload_extension(F'bgg.{extension}')
    await ctx.send(F'ReLoaded {extension} done')
    
    
for Filename in os.listdir('./bgg'):
    if Filename.endswith('.py'):
        bot2.load_extension(F'bgg.{Filename[:-3]}')
        
if __name__ == "__main__":
    bot2.run(jdata['TOKEN'])