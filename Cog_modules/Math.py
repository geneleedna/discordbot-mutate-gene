import discord
from discord.ext import commands
from Core.classes import Cog_Extensions
from discord.ui import Button , View
import json

class Math(Cog_Extensions):

    @commands.command()
    async def math(self , ctx):
        pass

async def setup(bot):
    await bot.add_cog(Math(bot))

'''
OK I wanna say something here to remind myself in the future
我希望我的數學程式碼可以這樣運作
首先打math他會跳出一個擁有許多按鈕和選項的介面
然後她會讓使用者能夠用手點擊想要計算的東西(比如說矩陣、三角函數等)
然後他就會在介面上面顯示結果
當我們不需要計算時按下x就可以離開介面了
'''