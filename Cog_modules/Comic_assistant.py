import discord
from discord.ext import commands
from discord import app_commands
from Core.classes import Cog_Extensions
import docx
import os

class Comic_assistant(Cog_Extensions):

    pass

async def setup(bot):
    await bot.add_cog(Comic_assistant(bot))