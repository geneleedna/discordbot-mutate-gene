import discord
from discord.ext import commands
from discord import app_commands
from Core.classes import Cog_Extensions
import json
import os

#==[setting some route]==#
'''
current_path = os.path.dirname(os.path.abspath(__file__))
json_files_for_command = os.path.join(current_path , 'json_file_for_cog_modules')
'''
#==[setting some route]==#

def is_owner():
    async def predicate(ctx):
        return await ctx.bot.is_owner(ctx.author)
    return commands.check(predicate)

class Admin(Cog_Extensions):

    @commands.command()
    @commands.is_owner()
    async def shutdown(self , ctx):
        #await ctx.send(response_jfile[self.shutdown.__name__][Cog_Extensions.charactor_current_mode])
        await ctx.send(self.get_response(ctx.command.name))
        await self.bot.close()

    @app_commands.command(name= '重新讀取反應json檔' , description= '如果對話json檔有更新就用吧(only Admin is accessible)')
    @is_owner()
    async def 重新讀取反映json檔(self , interaction: discord.Interaction):
        try:
            self.load_response_json_file()
            await interaction.response.send_message('Successfully reloaded the response json files!' , ephemeral = True)
        except:
            await interaction.response.send_message('Failed to reload the json files' , ephemeral = True)

    @commands.command()
    @commands.is_owner()
    async def change_name(self , ctx , new_name):
        self.bot.name_localization[ctx , new_name]

async def setup(bot):
    await bot.add_cog(Admin(bot))