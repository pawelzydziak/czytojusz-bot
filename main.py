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
playlists = [
    'https://www.youtube.com/watch?v=60ItHLz5WEA&list=PLAGF5FkTzB70b3CZCPp6e_g3A9zeoM_RB',
    'https://www.youtube.com/watch?v=e7HBypw4lhY&list=PLgzTt0k8mXzHksBAyoa15hjvGBfwaZ2fY',
    'https://www.youtube.com/watch?v=gCYcHz2k5x0&list=PLw6eTMMKY24QLYfmrU2rB8x-lP5Fas2dY',
    'https://www.youtube.com/watch?v=7IXJbCm6hEE&list=PLrdP_rZoA4WWkjvl8BvySEVJygB6-8wJ9',
    'https://www.youtube.com/watch?v=YqeW9_5kURI&list=PLam08HY53eksdbkGH0OELhxU2H4X9jb8i',
    'https://www.youtube.com/watch?v=n2hJA78YuWw&list=PLKTnYvE7BJU1PCbSCVZB7S6VqVhEIwXC2',
    'https://www.youtube.com/watch?v=tgw1yEcWpTU&list=PLMxT09Pm9Fikb4YmESV1BPZzKd2V14DmF',
    'https://www.youtube.com/watch?v=k2C5TjS2sh4&list=PL88B28947A045885B',
    'https://www.youtube.com/watch?v=dHJo2QvGz0M&list=PL1UBuIKCO8yDjsBRQ56iEab5z7CC_DG4c',
    'https://www.youtube.com/watch?v=qOP8QiRmPsA&list=PL0pBC0ZavTJZX62Q3tiMbQsCaGuMuI4e-',
    'https://www.youtube.com/watch?v=duP4pPxZTgU&list=PL0pBC0ZavTJbUQx4azoqvGFFkcBPau30m',
    'https://www.youtube.com/watch?v=4BQLE_RrTSU&list=PLtbcfhkWj9EjYk4_jphC-O330K76Swh8H',
    'https://www.youtube.com/watch?v=Q91hydQRGyM&list=PL2MiU6VTSezliX7u1CeDcC6NlJB_C41K4',
    'https://www.youtube.com/watch?v=x9QKRpALphM&list=PLkqz3S84Tw-S4mNV8y83k5CyOYksn76sM'
]

gamelist = [
    'Civilization 5',
    'Civilization 6',
    'Huminkind',
    'Forza',
    'Divinity',
    'Unrailed!',
    'Battlebock Therate',
    'Ultimate Chicken',
    'Serious Sam',
    'Ets 2',
    'Age of Empires 2'
]

@bot.command(name='czytojusz', brief='Czego kurwa nie rozumisz?')
async def isThisNow(ctx):
    # channel = ctx.author.voice.channel
    # resp = 'Kurwa: https://www.reddit.com/r/discordapp/comments/a35txa/bots_setting_other_bots_commands/'
    fredCommand = ';;play ' + random.choice(playlists)
    # games = random.choices(gamelist, k=5)
    selectedGame = random.choice(gamelist)

    # await channel.connect() to sie nie musi dziac tak czy siak nie dziala kom bot->bot
    #te trzy awaity fes sztos
    await ctx.send('Tak, to się dzieje. Wejrzyj. Muzyczka i gierki:')
    await ctx.send(fredCommand)
    await ctx.send(f'Dzisiaj panowie gracie w: {selectedGame}.')

@bot.command(name='acid', brief='Fes ważne')
async def kc(ctx):
    embedVar = discord.Embed(title='MORDOOOOOO', color=0xfccdd, url='http://bigassmessage.com/30f3c')
    embedVar.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Love_Heart_SVG.svg/2258px-Love_Heart_SVG.svg.png")
    await ctx.send(embed=embedVar)
#
# @bot.command(name='d')
# async def helpCmd(ctx):
#     # helpTxt = f'Prefix: {ctx.command_prefix}'
#     # await ctx.send('Tak, to się dzieje. Wejrzyj. Muzyczka i gierki:')
#     # await ctx.send(fredCommand)
#     await ctx.send(ctx.help_command)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandError):
        await ctx.send('Nie ma takiej komendy zjebie.')

@bot.command(name='panowie')
async def panowie(ctx):
    await ctx.send(f'Bardzo ważne, {ctx.message.author.name} wzywa na wspaniałom pszygode. Bedom dupy. @everyone')

@bot.command(name='kajjoje')
async def kajjoje(ctx):
    await ctx.send(f'{socket.gethostname()}')
bot.run(TOKEN)
