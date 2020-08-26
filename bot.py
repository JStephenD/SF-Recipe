import os

import discord
from discord.ext.commands import Bot

from resources import export as resources
from technical_components import export as technical_components
from cargo_management import export as cargo_management

from pprint import pformat
from collections import defaultdict

BOT_TOKEN = os.environ['BOT_TOKEN']
command_prefix = ('??')

bot = Bot(command_prefix=command_prefix)

recipes = {}
recipes.update(resources())
recipes.update(technical_components())
recipes.update(cargo_management())

def clean(d):
    rv = defaultdict(int)
    for k, v in d.items():
        if isinstance(v, dict):
            for k, v in clean(v).items():
                rv[k] += v
        else:
            rv[k] += v
    return rv

def format_msg(d: dict):
    x = '```css'
    for k, v in d.items():
        x += f'\n{k}: {v}'
    x += '```'
    return x

def parse_msg(*msgs):
    item = ''
    amt = 0
    for msg in msgs:
        if msg.isdigit():
            amt += int(msg)
        else:
            item += msg
    return ('_'.join(item), amt)

@bot.command()
async def raw(ctx, msg):
    pass

@bot.command()
async def nraw(ctx, *msgs):
    print(msgs)
    # item, amt = parse_msg(msgs)
    # recipe_unclean = recipes[item](amt)
    # cleaned = clean(recipe_unclean)
    # formatted = format_msg(cleaned)
    # await ctx.send(formatted)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

if __name__ == '__main__':
    print('Initializing Bot')
    # recipe_unclean = recipes['hardened_glass'](17)
    # cleaned = clean(recipe_unclean)
    # formatted = format_msg(cleaned)
    # print(formatted)
    bot.run(BOT_TOKEN)