import nest_asyncio
import discord
from discord.ext import commands
import json
import random
from C.core import Cog_Extension

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
nest_asyncio.apply()
class React(Cog_Extension):
    
    # @commands.command()
    # async def jpg(self,ctx):
    #     pic = discord.File(jdata['jpg'])
    #     await ctx.send(file=pic)
    
    @commands.command()
    async def 圖片(self,ctx):
        random_pic = random.choice(jdata['jpg'])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)
        
    @commands.Cog.listener()
    #endwiths <<<語詞後面包含
    #...'hihi' and msg.author != self.bot.user:
    async def on_message(self,msg):
        keyword = ['hihi','大家好呀','安安','哈囉']
        #if msg.content in keyword and...
        for key in keyword:
            if msg.content.find(key) != -1:
                await msg.channel.send('見了本宮也敢不行大禮')
                return
        for key in jdata.keys():
            if msg.content.find(key) != -1:
                await msg.channel.send(jdata[key])
    
        
def setup(bot):
    bot.add_cog(React(bot))