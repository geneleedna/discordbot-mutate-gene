import discord
from discord.ext import commands
import json
import random

with open('./defines.json', mode = 'r' , encoding = 'utf8') as defines:
    jsdata = json.load(defines)
with open('./pictures.json', mode = 'r' , encoding = 'utf8') as pictures:
    jspic = json.load(pictures)

from Core.classes import Cog_module

class Entertainment(Cog_module):
#============================================================================================#
    @commands.command()
    async def useless(self , ctx):
        await ctx.send("這是一個沒用的指令")
#============================================================================================#
    @commands.command()                    #發送圖片-杰哥的指令
    async def sephera(self , ctx):
        picture = discord.File(jspic["SEPHERA"])
        await ctx.send(file = picture)
#============================================================================================#

        
async def setup(bot):
    await bot.add_cog(Entertainment(bot))