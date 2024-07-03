import discord
from discord.ext import commands
import asyncio
import json
import os
from Core.classes import Cog_Extensions

#==[Section for initialization]==#
with open("./basic_settings.json" , mode = 'r' , encoding='utf8') as setting_json:
    setting_file = json.load(setting_json)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '!' , intents=intents)
#==[Section for initialization]==#

#==[This is the section of commands for addressing the Cog modules]==#
def assurance(extension_name):
    return os.path.exists(f'.\\Cog_modules\\{extension_name}.py')

@bot.command()
@commands.is_owner()
async def unload(ctx , extension_name):
    if assurance(extension_name):
        extension_name = f'Cog_modules.{extension_name}'
        await bot.unload_extension(extension_name)
        await ctx.send('Unloading Extension successfully')
    else:
        await ctx.send('Failed to unload the extension')

@bot.command()
@commands.is_owner()
async def load(ctx , extension_name):
    if assurance(extension_name):
        extension_name = f'Cog_modules.{extension_name}'
        await bot.load_extension(extension_name)
        await ctx.send('Loading Extension successfully')
    else:
        await ctx.send('Failed to load the extension')

@bot.command()
@commands.is_owner()
async def reload(ctx , extension_name):
    if assurance(extension_name):
        extension_name = f'Cog_modules.{extension_name}'
        await bot.reload_extension(extension_name)
        await ctx.send('Reloading Extension successfully')
    else:
        await ctx.send('Failed to reload the extension')
#==[This is the section of commands for addressing the Cog modules]==#

#==[initializing bot]==#

@bot.event
async def on_ready():
    print(">> Bot is online <<")
    Cog_Extensions.load_response_json_file()
    await bot.tree.sync()

async def init_load():
    for filename in os.listdir('./Cog_modules'):
        if filename.endswith('.py'):
            await bot.load_extension(f'Cog_modules.{filename[:-3]}')

async def main():
    await init_load()
    await bot.start(setting_file["TOKEN"])

asyncio.run(main())
#==[initializing bot]==#