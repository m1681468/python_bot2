import nest_asyncio
import discord
from discord.ext import commands
nest_asyncio.apply()
class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot