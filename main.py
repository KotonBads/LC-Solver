import discord
import os
import json
from discord.ext import commands
from unscrambler import unscramble
from build_battle import solve

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please pass in all required arguments')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def help(ctx):
    help_embed = discord.Embed(colour = discord.Colour.blue())

    help_embed.set_author(name = 'Commands')
    help_embed.add_field(name = 'ping', value = 'Returns the bot\'s latency', inline = False)
    help_embed.add_field(name = 'flag', value = '!flag <2 Letter Country Code>', inline = False)
    help_embed.add_field(name = 'unscramble', value = '!unscramble <scrambled word>', inline = False)
    help_embed.add_field(name = 'fill_in_the_gaps [fitg, fill]', value = '!fitg <word with missing letters (_)>', inline = False)

    await ctx.send(embed = help_embed)

@bot.command()
async def flag(ctx, code):
    with open('./flags.json') as f:
        f = json.load(f)
    
    try:
        await ctx.send(f'{f[code.upper()]}')
    except:
        await ctx.send('Invalid Country Code')

@bot.command(aliases = ['unscramble'])
async def unscramble_(ctx, word):
    await ctx.send(unscramble(word))

@bot.command(aliases = ['fill', 'fitg'])
async def fill_in_the_gaps(ctx, gapped_word):
    await ctx.send(f"{solve(f'{gapped_word}')}")

bot.run(os.environ['LC_SOLVER_TOKEN'])