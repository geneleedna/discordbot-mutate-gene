import discord
from discord.ext import commands
import json
import random

with open('./defines.json', mode = 'r' , encoding = 'utf8') as defines:
    jsdata = json.load(defines)

from Core.classes import Cog_module

class Load(Cog_module):
    @commands.command()
#============================================================================================#    
    async def reload(self , ctx , extension):
        self.bot.reload_extension(f'cog.{extension}')
        await ctx.send(f'cog.{extension}已重新讀取')
#============================================================================================#    
    @commands.command()
    async def unload(self , ctx , extension):
        self.bot.unload_extension(f'cog.{extension}')
        await ctx.send(f'cog.{extension}已卸載')
#============================================================================================#    
    @commands.command()
    async def load(self , ctx , extension):
        self.bot.load_extension(f'cog.{extension}')
        await ctx.send(f'cog.{extension}已讀取')


async def setup(bot):
    await bot.add_cog(Load(bot))