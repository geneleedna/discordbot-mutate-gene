import discord
from discord.ext import commands
import json
import random

with open('./defines.json', mode = 'r' , encoding = 'utf8') as defines:
    jsdata = json.load(defines)

from Core.classes import Cog_module

class Comic(Cog_module):
    #your commands
    123456

async def setup(bot):
    await bot.add_cog(Comic(bot))