#!/usr/bin/env python3
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import socket

## na komende join, dowiedziec sie jak interacja bot do bota, losowanie random.choice z listy linkow, niech losuje 5 gier z listy gier i podaje linka
# playlisty z pliku, gry z pliku, poszukac jakiegos whilspinera z api??
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix='??')


@bot.command(name='czytojusz', brief='Czego kurwa nie rozumisz?')
async def isThisNow(ctx):
    # https://www.reddit.com/r/discordapp/comments/a35txa/bots_setting_other_bots_commands/'
    fredCommand = ';;play ' + random.choice(list(open('links.txt')))
    selectedGame = random.choice(list(open('games.txt')))

    await ctx.send(f'Tak, to się dzieje. Wejrzyj. Muzyczka i gierki:\n\n{fredCommand}\nDzisiaj panowie gracie w: {selectedGame}')


@bot.command(name='acid', brief='Fes ważne')
async def kc(ctx):
    embedVar = discord.Embed(title='MORDOOOOOO', color=0xfccdd, url='http://bigassmessage.com/30f3c')
    embedVar.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Love_Heart_SVG.svg/2258px-Love_Heart_SVG.svg.png")
    await ctx.send(embed=embedVar)


@bot.command(name='panowie', brief='Przed wyruszeniem w drogę należy zebrać drużynę.')
async def panowie(ctx):
    await ctx.send(f'Bardzo ważne, {ctx.message.author.name} wzywa na wspaniałom pszygode. Bedom dupy. @everyone')


@bot.command(name='kajjoje', brief='Gdzie odpalony')
async def kajjoje(ctx):
    await ctx.send(f'{socket.gethostname()}')


bot.run(TOKEN)
