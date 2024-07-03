import discord
from discord.ext import commands
import json
import os

current_path = os.path.dirname(os.path.abspath(__file__))
response_json_path = os.path.join(current_path , 'response_of_commands')


class Cog_Extensions(commands.Cog):

    charactor_current_mode = '正常'
    dict_for_response_file = {}

    def __init__(self , bot):
        self.bot = bot

    @classmethod
    def change_charactor_mode(cls , mode):
        cls.charactor_current_mode = mode

    @classmethod
    def load_response_json_file(cls):
        json_files = os.listdir(response_json_path)
        #print(json_files)
        for file in json_files:
            with open(f'{response_json_path}\\{file}' , 'r' , encoding= 'utf-8') as temp_file:
                cls.dict_for_response_file[f'response_{file.split('_')[0]}'] = json.load(temp_file)

    @classmethod
    def get_response(cls , command_name):
        file_name = cls.__module__.split('.')[-1]
        try:
            return cls.dict_for_response_file[f'response_{file_name}'][command_name][cls.charactor_current_mode]
        except:
            return '0'

def setup(bot):
    bot.add_cog(Cog_Extensions(bot))
'''
要幹嘛?
首先我們要先建立兩個class method
一個為load_response_json_file
我們先把所有的response json檔都先讀起來

另一個為get_response
我們讀檔之後呢
讓各地的檔案前來呼叫這個方法
如此我們便能夠不用在每個指令檔案裡面with open response檔案
能夠直接從這邊丟回覆給他們
'''