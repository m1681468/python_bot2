import nest_asyncio
import discord
from discord.ext import commands
import json
import random
from C.core import Cog_Extension

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
nest_asyncio.apply()

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel'])) 
        await channel.send(F'{member} join~')
        
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel'])) 
        await channel.send(F'{member} 888~')
        
def setup(bot):
    bot.add_cog(Event(bot))