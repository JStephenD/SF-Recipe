import os

import discord
from discord.ext.commands import Bot

from resources import export as resources
from technical_components import export as technical_components

from pprint import pformat
from collections import defaultdict

BOT_TOKEN = os.environ['BOT_TOKEN']
command_prefix = ('??')

bot = Bot(command_prefix=command_prefix)

recipes = {}
recipes.update(resources.items())
recipes.update(technical_components.items())
# recipes = {
#     k: v for k, v in resources().items(),
#     k: v for k, v in technical_components().items()
# }

def clean(d):
    rv = defaultdict(int)
    for k, v in d.items():
        if isinstance(v, dict):
            for k, v in clean(v).items():
                rv[k] = v
        else:
            rv[k] += v
    return rv

def format_msg(d: dict):
    x = '```css'
    for k, v in d.items():
        x += f'\n{k}: {v}'
    x += '```'
    return x

def parse_msg(*msg):
    pass

@bot.command()
async def raw(ctx, msg):
    pass

@bot.command()
async def nraw(ctx, *item, amt=1):
    item = '_'.join(i for i in item)
    recipe_unclean = recipes[item](amt)
    cleaned = clean(recipe_unclean)
    formatted = format_msg(cleaned)
    await ctx.send(formatted)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

if __name__ == '__main__':
    print('Initializing Bot')
    bot.run(BOT_TOKEN)