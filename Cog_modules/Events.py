import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
from Core.classes import Cog_Extensions
import json
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_directory, 'json_file_for_cog_modules', 'Events.json')

'''
try:
    with open(json_path , 'r' , encoding='utf-8') as Events_jfile:
        e_jfile = json.load(Events_jfile)
except:
    print('Failed to open the file')
'''

class Events(Cog_Extensions):

    with open(json_path , 'r' , encoding='utf-8') as Events_jfile:
        e_jfile = json.load(Events_jfile)

    charactor_info = dict(e_jfile["人格"]) #這個是字典 專門放角色的介紹
    charactor_list = list(charactor_info.keys())#這個是放角色列表的串列
    # 你之後看到這上面那行可能會想為什麼要這樣寫，我們charactor_info放的是我們的角色列表和他們的介紹
    # 之後程式還會需要用到角色名稱列表，範圍型迴圈就會用到
    # 我們只需要名子就好不需要他們的介紹所以就把字典的key單獨抓出來變成一個串列啦

    @app_commands.command(name = 'check_current_mode' , description = '來看看現在機器人是什麼角色模式')
    async def check_current_mode(self , interaction : discord.Interaction):
        try:
            await interaction.response.send_message(f'現在是{Cog_Extensions.charactor_current_mode}模式')
        except:
            await interaction.response.send_message('Failed to show the current mode')

    @app_commands.command(name = 'change_mode' , description = '切換機器人的角色模式')
    @app_commands.describe(mode = '請選擇你想切換的模式')
    @app_commands.choices(mode = [Choice(name=option , value=option) for option in charactor_list])
    async def change_mode(self , interaction : discord.Interaction , mode : Choice[str]):
        try:
            Cog_Extensions.change_charactor_mode(mode.value)
            await interaction.response.send_message(f'成功切換到{Cog_Extensions.charactor_current_mode}模式')
        except:
            await interaction.response.send_message('Failed to change the mode')

    @app_commands.command(name = 'mode_list' , description = '來看看現在有哪些角色模式可選')
    async def mode_list(self , interaction : discord.Interaction):
        try:
            embed=discord.Embed(title="角色模式種類", color=0x109331)
            for mode in self.charactor_list:
                embed.add_field(name=mode , value='' , inline=False)
            embed.set_footer(text="Coded by Genelee")
            await interaction.response.send_message(embed=embed)
        except:
            await interaction.response.send_message('Failed to display the charactor mode list')

    

    @commands.Cog.listener()
    async def on_message(self , message):
        if message.author == self.bot.user:
            return
        
        response_list = dict(self.e_jfile[Cog_Extensions.charactor_current_mode])
        
        for trigger in response_list.keys():
            if trigger in message.content.lower():
                await message.channel.send(response_list[trigger])

async def setup(bot):
    await bot.add_cog(Events(bot))