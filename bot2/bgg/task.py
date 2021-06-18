import nest_asyncio
import discord
from discord.ext import commands
from C.core import Cog_Extension
import json, asyncio, datetime
nest_asyncio.apply()

class Task(Cog_Extension):
     def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
        
    #     async def interval():
    #         await self.bot.wait_until_ready()
    #         self.channel = self.bot.get_channel(852963746656944168)
    #         while not self.bot.is_closed():
    #             await self.channel.send("QQ I'm running!")
    #             await asyncio.sleep(5) #單位 秒
        
    #     self.bg_task = self.bot.loop.creat_task(interval())
                
        
    # @commands.command()
    # async def set_channel(self, ctx, ch: int):
    #     self.channel = self.bot.get_channel(ch)
    #     await ctx.send(f'set channel: {self.channel.mention}')
def setup(bot):
    bot.add_cog(Task(bot))