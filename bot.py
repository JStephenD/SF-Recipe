import os

import discord
from discord.ext.commands import Bot

from resources import export as resources

from pprint import pformat

BOT_TOKEN = os.environ['BOT_TOKEN']
command_prefix = ('??')

bot = Bot(command_prefix=command_prefix)

recipes = {
    k: v for k, v in resources().items()
}

@bot.command()
async def raw(ctx, msg):
    pass

@bot.command()
async def nraw(ctx, *item, amt=1):
    item = '_'.join(i for i in item)
    await ctx.send(recipes[item](amt))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

if __name__ == '__main__':
    print('Initializing Bot')
    bot.run(BOT_TOKEN)