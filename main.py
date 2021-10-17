import discord
import os
import json
from discord.ext import commands
from unscrambler import unscramble

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please pass in all required arguments')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def flag(ctx, code):
    with open('LC Flag Solver/flags.json') as f:
        f = json.load(f)
    
    try:
        await ctx.send(f'{f[code.upper()]}')
    except:
        await ctx.send('Invalid Country Code')

@bot.command(aliases = ['unscramble'])
async def unscramble_(ctx, word):
    await ctx.send(unscramble(word))

bot.run(os.environ['LC_SOLVER_TOKEN'])