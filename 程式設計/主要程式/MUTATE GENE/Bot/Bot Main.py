#導入 Discord.py
import discord
import asyncio
import random
import datetime
import json
import os

with open('./defines.json', mode = 'r' , encoding = 'utf8') as defines:
    jsdata = json.load(defines)

from discord.ext import commands
#client 是我們與 Discord 連結的橋樑
bot=commands.Bot(command_prefix = '.',intents = discord.Intents.all())


#調用 event 函式庫


async def load_extensions():
    for Filename in os.listdir('./Commands'):
        if Filename.endswith('.py'):
            await bot.load_extension(f'Commands.{Filename[:-3]}')

async def main():
    async with bot:
        await load_extensions()
        await bot.start(jsdata['TOKEN'])

if __name__ == "__main__":
    asyncio.run(main()) #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面


#https://www.runoob.com/python/func-number-random.html
#https://ithelp.ithome.com.tw/articles/10235251
#https://www.runoob.com/python/python-lists.html    list
############################################################################################## this is a split patten
#============================================================================================#