import discord
from discord.ext import commands
import json
import random
import asyncio

with open('./defines.json', mode = 'r' , encoding = 'utf8') as defines:
    jsdata = json.load(defines)

from Core.classes import Cog_module

class events(Cog_module):
    @commands.Cog.listener()
    #當機器人完成啟動時
    async def on_ready(self):
        print('目前登入身份：', self.bot.user)
        Activity = discord.Game(name='Sinestrea')
        await self.bot.change_presence(status = discord.Status.idle, activity = Activity)
#============================================================================================# 
    @commands.Cog.listener()                                     #歡迎加入與離開
    async def on_memberjoin(self , member):                      #member join
        channel = self.bot.get_channel(1010795017452933142) #頻道:dc機器人測試
        await channel.send(f"{member}加入了!!")
    
    async def on_memberleave(self , member):                     #member leave
        channel = self.bot.get_channel(1037807615570358365) #頻道:dc機器人測試
        await channel.send(f"{member}離開了~")
#============================================================================================#
    @commands.Cog.listener()                                     #偵測訊息回話區#

    async def on_message(self , message):
    #排除自己的訊息，避免陷入無限循環
        if message.author == self.bot.user:
            return
    #如果包含 ()，機器人回傳 ()

        if '遜' in message.content:                      #遜
            await message.send_message(message.channel,random.choice(['真的是太遜了','就遜啊','真的很遜欸','是在遜幾點的']))
        

        if '爛' in message.content:                      #爛
            await message.channel.send(random.choice(['爛死了','也太爛了吧','好爛喔','爛透了']))
            
        if '基因很帥' in message.content:
            tmpmsg = await message.channel.send('你要確定欸')
            await asyncio.sleep(2)
            await message.delete()
            await asyncio.sleep(0.5)
            await tmpmsg.delete()
            

        if message.content.startswith('你很勇喔'):         #你很勇喔
            await message.channel.send('讓我看看!!!')
            
    #打什麼就說什麼                                        #這邊有個小技巧=>先接收字串然後用特殊語法將字串切成兩段然後裝進字串陣列裡
        if message.content.startswith('說'):              #要說的字串為空
            reply = message.content.split(" ",2)
            if len(reply) == 1:                           #要說的字串是有東西的=>發送訊息
                await message.channel.send("所以你要我說什麼哩")
            else:
                await message.channel.send(reply[1])

        if message.content == '抽獎':                      #抽獎
            await message.channel.send(random.choice(['||頭獎||','||中等獎||','||三等獎||','||吃屎喇你||']))

        #await self.bot.process_commands(message)



async def setup(bot):
    await bot.add_cog(events(bot))