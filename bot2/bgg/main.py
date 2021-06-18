import nest_asyncio
import discord
from discord.ext import commands
from C.core import Cog_Extension
nest_asyncio.apply()
class Main(Cog_Extension):
           
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('4在哈囉?')
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("hihi")
        
    # @commands.command()
    # async def clean(self, ctx, num: int):
    #     await ctx.channel.purge(limit=num+1)
        
def setup(bot):
    bot.add_cog(Main(bot))