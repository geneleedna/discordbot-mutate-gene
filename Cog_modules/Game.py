import discord
from discord.ext import commands
from discord import app_commands
from Core.classes import Cog_Extensions
import time
import random

class game_nAnB():

    def __init__(self):
        pass




class Game(Cog_Extensions):
    
    @app_commands.command(name= 'nanb遊戲' , description= '猜四位數遊戲')
    async def nAnB遊戲(self , interaction : discord.Interaction):
        pass

async def setup(bot):
    await bot.add_cog(Game(bot))