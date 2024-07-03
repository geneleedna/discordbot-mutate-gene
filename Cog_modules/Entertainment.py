import discord
from discord.ext import commands
from Core.classes import Cog_Extensions
import random
import json
import os

#==[setting json file route]==#
current_directory = os.path.dirname(os.path.abspath(__file__))
response_json_path = os.path.join(current_directory, 'json_file_for_cog_modules', 'Entertainment_charactor_response.json')
#==[setting json file route]==#

#THIS IS A CONSTANT
PICTURE_ROUTE_OF_GROW = '..\\project_bot_comic_assistant\\Grow_Grow_pictures'

class Entertainment(Cog_Extensions):

    def random_select_file(self):
        #print(os.path.exists(PICTURE_ROUTE_OF_GROW))#assuring , please delete it after running successfully
        all_files = os.listdir(PICTURE_ROUTE_OF_GROW)
        return random.choice(all_files)

    @commands.command()
    async def 我要看果照(self , ctx):
        Grow_picture = PICTURE_ROUTE_OF_GROW + '\\' + self.random_select_file()
        Grow_picture = discord.File(Grow_picture)
        #print(Grow_picture)    #This is a testing code
        try:
            response = self.get_response(ctx.command.name)
            await ctx.send(response)
            #await ctx.send(response_jfile[self.我要看果照.__name__][Cog_Extensions.charactor_current_mode])
        except:
            await ctx.send('來了')
        await ctx.send(file=Grow_picture)

async def setup(bot):
    await bot.add_cog(Entertainment(bot))