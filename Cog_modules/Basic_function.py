import discord
from discord.ext import commands
from Core.classes import Cog_Extensions

class Basic_function(Cog_Extensions):

    @commands.command()
    async def ping(self , ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}ms')

async def setup(bot):
    await bot.add_cog(Basic_function(bot))