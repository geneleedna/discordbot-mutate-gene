import discord
from discord.ext import commands
import json
import random

with open('./defines.json', mode = 'r' , encoding = 'utf8') as defines:
    jsdata = json.load(defines)

from Core.classes import Cog_module

class Tools(Cog_module):
#============================================================================================#
    @commands.command()
    async def spamming(self , ctx , spam , times):
        for i in range(0,int(times),1):
            await ctx.send(str(spam))
#============================================================================================#
    @commands.command()
    async def choose(self , ctx , options):
        answer = options.split(" ")
        index = random.randint(0,len(answer-1))
        await ctx.send(f'就選{answer[index]}吧~')
#============================================================================================#
    @commands.command()
    async def sort(self, ctx , stuffs):
        answer = stuffs.split(" ")
        await ctx.send(f'{(random.shuffle(int(answer),1))}如何?')
#============================================================================================#
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')
#============================================================================================#

async def setup(bot):
    await bot.add_cog(Tools(bot))