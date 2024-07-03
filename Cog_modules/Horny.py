import discord
from discord.ext import commands
from discord import app_commands
from Core.classes import Cog_Extensions
import os
import json
import datetime

current_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_directory, 'json_file_for_cog_modules', 'Horny.json')

'''
try:
    with open(json_path , 'r' , encoding='utf-8') as Horny_jfile:
        h_jfile = json.load(Horny_jfile)
except:
    print('Failed to open the file')
'''

Websites = ['Hentai.net' , '紳士漫畫wnacg' , '禁漫天堂' , 'Pixiv']

class Horny(Cog_Extensions):

    with open(json_path , 'r' , encoding='utf-8') as Horny_jfile:
        h_jfile = json.load(Horny_jfile)

    def combine_link(self , webs , number):
        if "Pixiv-tag" == webs or "紳士漫畫wnacg" in webs:
            return f'{self.h_jfile[webs][0]}{number}{self.h_jfile[webs][1]}'
        else:
            return f'{self.h_jfile[webs]}{number}'

    @app_commands.command(name="horny" , description = '幫你找到神之語言所對應的漫畫或圖片')
    @app_commands.describe(number = '請輸入你的神之語言')
    async def horny(self , interaction: discord.Interaction , number : str):
        try:
            embed=discord.Embed(
                title='請選擇一個網站',
                description='溫馨提示:相同的神之語言在不同網站可能是不同的漫畫\n記得要開無痕再貼上網址喔',
                color=0xe6ca19,
                timestamp = datetime.datetime.now()
                )
            for webs in Websites:
                embed.add_field(name=webs , value= self.combine_link(webs , number), inline=False)
            embed.set_footer(text='Code by Genelee')
            await interaction.response.send_message(embed=embed , ephemeral =True)
        except:
            await interaction.response.send_message('Failed to activate the portal' , ephemeral = True)

        await interaction.response.defer(ephemeral=True)

    @app_commands.command(name="htag" , description= '幫你搜索含有此標籤的漫畫或圖片')
    @app_commands.describe(tag = '請輸入你的標籤')
    async def htag(self , interaction: discord.Interaction , tag : str):
        try:
            embed=discord.Embed(
                title='請選擇一個網站',
                description='溫馨提示:相同的標籤在不同網站可能出現不同的漫畫也可能不存在於某些網站\n記得要開無痕再貼上網址喔',
                color=0xe6ca19,
                timestamp = datetime.datetime.now()
                )
            for webs in Websites:
                embed.add_field(name=webs , value= self.combine_link(f'{webs}-tag' , tag), inline=False)
            embed.set_footer(text='Code by Genelee')
            await interaction.response.send_message(embed=embed , ephemeral =True)
        except:
            await interaction.response.send_message('Failed to activate the portal' , ephemeral = True)
        await interaction.response.defer(ephemeral=True)

async def setup(bot):
    await bot.add_cog(Horny(bot))