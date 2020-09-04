import discord
import random
import re
import giphy_client
import aiohttp
import requests
import termcolor
import os
import youtube_dl
import sys
import time
import asyncio
import sqlite3
import discord
import json
from discord.ext.commands import Bot
from discord.ext import commands
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from discord.voice_client import VoiceClient
from giphy_client.rest import ApiException
from discord.ext import commands
from pathlib import Path


client = commands.Bot(command_prefix='k ')
id = client.get_guild(681262466650734596)
ROLE = "1 poloski"
class style:
   BOLD = '\033[1m'
   END = '\033[0m'

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('DRINKING KOMPOT AND LISTENING TO HARD BASS [k kolbaser]'))
    print("Bot is ready, blyat")
    print(f'Kolbaser is in {len(client.guilds)} servers')
    channel = client.get_channel(681262467229155476)
    await channel.send('Hello Blyat')

players = {}





@client.command()
async def cmds(ctx):
    embed = discord.Embed(
        title='***Kolbaser***\n**Commands**',
        description='Current commands as of July 1, 2020',
        colour=0xdd16d9
    )

    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/690305523903758612/a79176bd0251eb2df75c143f016238ee.png?size=256')
    embed.set_author(name='KOLBASER',icon_url='https://cdn.discordapp.com/avatars/690305523903758612/6c2dfebc0f2dc4345840909ee5b68338.png?size=1024')

    embed.add_field(name='`k kolbaser`', value='Prints Kolbaser information', inline=False)
    embed.add_field(name='`k cmds`', value='Prints all commands', inline=False)
    embed.add_field(name='`k math_info`', value='Displays commands that use math to formulate and answer', inline=False)
    embed.add_field(name='`k vocab`', value='Trigger words for Kolbaser', inline=False)
    embed.add_field(name='`k userinfo`', value='Discord user information command', inline=False)
    embed.add_field(name='`k name`', value='Changes your username', inline=False)
    embed.add_field(name='`k music_info`', value='Opens a music menu', inline=False)
    embed.add_field(name='`k slav_info`', value='Prints information/overview on slavic country of your choosing', inline=False)
    embed.add_field(name='`k roulette`', value='Initiates a game of Russian Roulette', inline=False)
    embed.add_field(name='`k kolbasa`', value='Prints a picture of kolbasa', inline=False)
    embed.add_field(name='`k meme`', value='Prints a meme', inline=False)
    embed.add_field(name='`k flbp`', value='FLBP', inline=False)
    embed.add_field(name='`k russia`', value='idek', inline=False)
    embed.add_field(name='`k tpb`', value='Trailer Park Boys quote dispenser', inline=False)
    embed.add_field(name='`k joke`', value='Fetches a joke from the bot', inline=False)
    embed.add_field(name='`k ask`', value='Ask away!', inline=False)
    embed.add_field(name='`k hack [@user]`', value='Hacks a user and prints random information about mentioned user', inline=False)
    embed.add_field(name='`k av [@user]`', value='Enlarges and prints user avatars', inline=False)
    embed.add_field(name='`k say [msg]`', value='Makes the bot say something', inline=False)
    embed.add_field(name='`k ping`', value='Pings the bot and returns the latency', inline=False)
    embed.add_field(name='`k count [msg]`', value='Counts how many arguments there are', inline=False)
    embed.add_field(name='`k servers`', value='Returns the number of servers Kolbaser is in', inline=False)
    embed.add_field(name='`k spam [msg] [int]`', value='Spam command ', inline=False)
    embed.add_field(name='`k jack`', value='Snipe command[does not work]', inline=False)
    await ctx.send(embed=embed)

#Commands in order of embed above
#Public Commands:

@client.command()
async def kolbaser(ctx):
    embed = discord.Embed(
        title = '***I Am Kolbaser***',
        description = 'Eastern European slang: A person who dances to hardbass music.\n Polish and Russian Language: Sausage maker.\n Бочка Басс Колбасер',
        colour = 0xdd16d9

    )

    embed.set_footer(text='*Created by HydroFlouric#6979,\n Special thanks to alekos#5235 and The_Storm135#8326*')
    embed.set_image(url='https://cdn.discordapp.com/attachments/693639674841006101/700129506773565520/kolbaser.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/690305523903758612/6c2dfebc0f2dc4345840909ee5b68338.png?size=1024')
    embed.add_field(name='Enlightening video', value='https://www.youtube.com/watch?v=VLW1ieY4Izw', inline=False)
    embed.add_field(name='Commands for public use', value='`k cmds, k vocab`', inline=False)
    embed.add_field(name='KGB & Overlord commands', value='`k specinfo`', inline=False)
    embed.add_field(name='Kolbaser support server link:', value='`https://discord.gg/HH6YQ9F`', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def userinfo(ctx, member: discord.Member):
    roles = [role for role in member.roles]

    embed = discord.Embed(
    title = '***Kolbaser***\n**User Information**',
    colour = 0xdd16d9
    )
    embed.set_author(name=f'User Information - {member}')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author.mention}', icon_url=ctx.author.avatar_url)

    embed.add_field(name='Discord Username:', value=f'{member.display_name}', inline=False)
    embed.add_field(name='Discord User Discriminator:', value=f'{member.discriminator}', inline=False)
    embed.add_field(name='Discord User ID:', value=f'{member.id}', inline=False)

    embed.add_field(name='Account Creation Date:', value=f'{member.created_at.strftime("%A, %B %#d, %Y, %H:%M UTC")}', inline=False)
    embed.add_field(name=f'Joined {ctx.guild} at:', value=f'{member.joined_at.strftime("%A, %B %#d, %Y, %H:%M UTC")}', inline=False)

    embed.add_field(name=f'Roles ({len(roles)})', value=" ".join([role.mention for role in roles]))

    await ctx.send(embed=embed)

@client.command()
async def math_info(ctx):
    embed = discord.Embed(
        title = '***Kolbaser***\nMath',
        description = 'Conduct complex equations to formulate an answer based off of your input',
        colour = 0xdd16d9

    )

    embed.add_field(name='`k temperature_info`', value='Temperature Converter Information', inline=False)
    embed.add_field(name='`k temperature`', value='Temperature Converter', inline=False)
    embed.add_field(name='`k alcoholcontent_info`', value='BAC Calculator Information')
    embed.add_field(name='`k alcohol_content`', value='Blood Alcohol Content Calcultor', inline=False)
    embed.add_field(name='`k math add, sub, multi, div`', value="Conduct math equations with 2 inputs", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def vocab(ctx):
    embed = discord.Embed(
        title = '***Kolbaser***',
        description = 'Trigger words for Kolbaser',
        colour = 0xdd16d9

    )

    embed.add_field(name='`hello`', value='Prints a random greeting from Kolbaser', inline=False)
    embed.add_field(name='`yo`', value='Yo yo yo!', inline=False)
    embed.add_field(name='`lahey`', value='TPB fans out there, this one is for you!', inline=False)
    embed.add_field(name='`randy`', value='RANDY!!!', inline=False)
    embed.add_field(name='`russian underground`', value='prints a random response from Kolabser', inline=False)
    embed.add_field(name='`fortnite`', value='Say this and Kolbaser denounces you', inline=False)
    embed.add_field(name='`minecraft`', value='*Ourcraft*', inline=False)
    embed.add_field(name='`cyka`', value='Prints a random retort from Kolbaser', inline=False)
    embed.add_field(name='`420`', value='Smoke it!', inline=False)
    embed.add_field(name='`69`', value="Kolbaser's favorite number", inline=False)
    embed.add_field(name='`shit`', value='Prints a random retort from Kolbaser', inline=False)
    embed.add_field(name='`blyat`', value='Cyka Blyat!', inline=False)
    embed.add_field(name='`kompot`', value='Makes Kolbaser happy', inline=False)
    embed.add_field(name='`fuck off & fuck you`', value='Makes Kolbaser angry', inline=False)
    embed.add_field(name='`hardbass`', value='Kolbaser loves hardbass', inline=False)
    embed.add_field(name='`cheeki`', value='cheeki breeki i v damke!', inline=False)
    embed.add_field(name='`nwa`', value='Long Live NWA!', inline=False)
    embed.add_field(name='`kolbasar`', value='Bochka Bass Kolbaser', inline=False)
    embed.add_field(name='`pidoras`', value="Don't say this!", inline=False)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def music_info(ctx):
    embed = discord.Embed(
    title = '***Kolbaser***\n**Music Menu**',
    description = '[music menu]',
    colour = 0xdd16d9
    )

    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/690305523903758612/a79176bd0251eb2df75c143f016238ee.png?size=256')
    embed.set_author(name='KOLBASER',icon_url='https://cdn.discordapp.com/avatars/690305523903758612/6c2dfebc0f2dc4345840909ee5b68338.png?size=1024')

    embed.add_field(name='How to use', value='`k music [genre] [artist]`', inline=False)
    embed.add_field(name='Example', value='`k music hardbass djb`', inline=False)
    embed.add_field(name="Supported Genre's and Artists", value='`k musics` for information', inline=False)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def slav_info(ctx):
    embed = discord.Embed(
    title = '***Kolbaser***\nSlavic Country Information',
    colour = 0xdd16d9
    )

    embed.add_field(name='Description', value='This will allow you to search up the information/stats on any slavic country', inline=False)
    embed.add_field(name='How to use', value='`k slav russia`', inline=False)
    embed.add_field(name='Supported Countries:', value='Russia\nBelarus\nUkraine\nCzech Republic\nPoland\nSlovakia\nBosnia\nBulgaria\nCroatia\nMacedonia\nMontenegro\nSerbia\nSlovenia', inline=False)
    await ctx.send(embed=embed)
@client.command(pass_context=True)
async def slav(ctx, c: str):
    if c == 'russia':
        await asyncio.sleep(.6)
        embed = discord.Embed(
        title = f'***Kolbaser***\nSlavic Country Information',
        description = f'**Country**:`{c}`',
        colour = 0xdd16d9
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/693639674841006101/726956479327765105/1200px-Flag_of_Russia.svg.png')
        embed.add_field(name=f'{c}'.upper(), value='*Capital:* **Moscow**\n~\n*Population:* **144.5 million**\n~\n*Current president:* **Vladimir Putin**\n~\n*Currency:* **Russian Ruble**\n~\n*Government:* **Federal Republic**\n~\n*Language:* **Russian**\n~\n*Current Nuclear Weapon stockpile:* **6,500 total**\n~\n*Weather:* **warm to hot dry summers and (very) cold winters with temperatures of -30°C and lower and sometimes heavy snowfall.**')
        await ctx.send(embed=embed)
    elif c == 'belarus':
        await asyncio.sleep(.6)
        embed = discord.Embed(
        title = f'***Kolbaser***\nSlavic Country Information',
        description = f'**Country**:`{c}`',
        colour = 0xdd16d9
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/699655178818814013/726960050303664178/Flag-Belarus.jpg')
        embed.add_field(name=f'{c}'.upper(), value='*Slavic Group:* **East Slavs**\n~\n*Capital:* **Minsk**\n~\n*Population:* **9.485 million**\n~\n*Current president:* **Alexander Lukashenko**\n~\n*Currency:* **Belarusian Ruble**\n~\n*Government:* **Republic**\n~\n*Language:* **Belarusian**\n~\n*Current Nuclear Weapon stockpile:* **[none]**\n~\n*Weather:* **Continental**')
        await ctx.send(embed=embed)
    elif c == 'ukraine':
        await asyncio.sleep(.6)
        embed = discord.Embed(
        title = f'***Kolbaser***\nSlavic Country Information',
        description = f'**Country**:`{c}`',
        colour = 0xdd16d9
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/699655178818814013/726968016906223656/2000px-Flag_of_Ukraine.svg.png')
        embed.add_field(name=f'{c}'.upper(), value='*Slavic Group:* **East Slavs**\n~\n*Capital:* **Kiev**\n~\n*Population:* **41.98 million**\n~\n*Current president:* **Volodymyr Zelensky**\n~\n*Currency:* **Ukrainian Hryvnia**\n~\n*Government:* **President-Parliamentary Republic**\n~\n*Language:* **Ukrainian**\n~\n*Current Nuclear Weapon stockpile:* **3,000+**\n~\n*Weather:* **Continental**')
        await ctx.send(embed=embed)
    elif c == 'czech':
        await asyncio.sleep(.6)
        embed = discord.Embed(
        title = f'***Kolbaser***\nSlavic Country Information',
        description = f'**Country**:`{c}`',
        colour = 0xdd16d9
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/699655178818814013/726971987477659709/Flag-Czech-Republic.jpg')
        embed.add_field(name=f'{c}'.upper(), value='*Slavic Group:* **West Slavs**\n~\n*Capital:* **Prague**\n~\n*Population:* **10.69 million**\n~\n*Current president:* **Miloš Zeman**\n~\n*Currency:* **Czech Koruna**\n~\n*Government:* ** Unitary Parliamentary Constitutional Republic**\n~\n*Language:* **Czech**\n~\n*Current Nuclear Weapon stockpile:* **[none]**\n~\n*Weather:* **Moderately Continental**')
        await ctx.send(embed=embed)
    elif c == 'poland':
        await asyncio.sleep(.6)
        embed = discord.Embed(
        title = f'***Kolbaser***\nSlavic Country Information',
        description = f'**Country**:`{c}`',
        colour = 0xdd16d9
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/699655178818814013/726973635268575242/Flag-Poland.jpg')
        embed.add_field(name=f'{c}'.upper(), value='*Slavic Group:* **West Slavs**\n~\n*Capital:* **Warsaw**\n~\n*Population:* **37.97 million**\n~\n*Current president:* **Andrzej Duda**\n~\n*Currency:* **Polish Złoty**\n~\n*Government:* **Republic**\n~\n*Language:* **Polish**\n~\n*Current Nuclear Weapon stockpile:* **[none]**\n~\n*Weather:* **Continental**')
        await ctx.send(embed=embed)
    elif c == 'slovakia':
        await asyncio.sleep(.6)
        embed = discord.Embed(
        title = f'***Kolbaser***\nSlavic Country Information',
        description = f'**Country**:`{c}`',
        colour = 0xdd16d9
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/699655178818814013/726975627944656976/2000px-Flag_of_Slovakia.svg.png')
        embed.add_field(name=f'{c}'.upper(), value='*Slavic Group:* **West Slavs**\n~\n*Capital:* **Bratislava**\n~\n*Population:* **5.458 million**\n~\n*Current president:* **Zuzana Čaputová**\n~\n*Currency:* **Euro**\n~\n*Government:* **Parliamentary Representative Democratic Republic**\n~\n*Language:* **Slovak**\n~\n*Current Nuclear Weapon stockpile:* **[none]**\n~\n*Weather:* **Moderately Continental**')
        await ctx.send(embed=embed)
    elif c == 'bosnia':
        await asyncio.sleep(.6)
        embed = discord.Embed(
        title = f'***Kolbaser***\nSlavic Country Information',
        description = f'**Country**:`{c}`',
        colour = 0xdd16d9
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/699655178818814013/726978177314062376/1200px-Flag_of_Bosnia_and_Herzegovina.svg.png')
        embed.add_field(name=f'{c}'.upper(), value='*Slavic Group:* **South Slavs**\n~\n*Capital:* **Sarajevo**\n~\n*Population:* **3.324 million**\n~\n*Current president:* **Milorad Dodik**\n~\n*Currency:* **Bosnian Mark**\n~\n*Government:* **Republic-Parliamentary System**\n~\n*Language:* **Bosnian**\n~\n*Current Nuclear Weapon stockpile:* **[none]**\n~\n*Weather:* **Mediterranean**')
        await ctx.send(embed=embed)
    elif c == 'bulgaria':
        await asyncio.sleep(.6)
        embed = discord.Embed(
        title = f'***Kolbaser***\nSlavic Country Information',
        description = f'**Country**:`{c}`',
        colour = 0xdd16d9
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/699655178818814013/727653685462827119/bulgaria-flag__74380.1575479012.jpg')
        embed.add_field(name=f'{c}'.upper(), value='*Slavic Group:* **South Slavs**\n~\n*Capital:* **Sofia**\n~\n*Population:* **7 million**\n~\n*Current president/prime minister:* **Bokyo Borissov**\n~\n*Currency:* **Bulgarian Lev**\n~\n*Government:* **Republic**\n~\n*Language:* **Bulgarian**\n~\n*Current Nuclear Weapon stockpile:* **46?**\n~\n*Weather:* **Continental**')
        await ctx.send(embed=embed)
    elif c == 'croatia':
        await asyncio.sleep(.6)
        embed = discord.Embed(
        title = f'***Kolbaser***\nSlavic Country Information',
        description = f'**Country**:`{c}`',
        colour = 0xdd16d9
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/693639674841006101/727654624407847032/1200px-Croatia_Flag.svg.png')
        embed.add_field(name=f'{c}'.upper(), value='*Slavic Group:* **South Slavs**\n~\n*Capital:* **Zagreb**\n~\n*Population:* **4.076 million**\n~\n*Current president:* **Zoran Milanović**\n~\n*Currency:* **Croatian Kuna**\n~\n*Government:* **Republic**\n~\n*Language:* **Croatian**\n~\n*Current Nuclear Weapon stockpile:* **15,850**\n~\n*Weather:* **Continental**')
        await ctx.send(embed=embed)
    elif c == 'macedonia':
        await asyncio.sleep(.6)
        embed = discord.Embed(
        title = f'***Kolbaser***\nSlavic Country Information',
        description = f'**Country**:`{c}`',
        colour = 0xdd16d9
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/699655178818814013/727666954340532244/1920px-Flag_of_North_Macedonia.svg.png')
        embed.add_field(name=f'{c}'.upper(), value='*Slavic Group:* **South Slavs**\n~\n*Capital:* **Skopje**\n~\n*Population:* **2.077 million**\n~\n*Current president:* **Stevo Pendarovski**\n~\n*Currency:* **Macedonian Denar**\n~\n*Government:* **Parliamentary-Republic**\n~\n*Language:* **Macedonian**\n~\n*Current Nuclear Weapon stockpile:* **N/A**\n~\n*Weather:* **Continental**')
        await ctx.send(embed=embed)
    elif c == 'montenegro':
        await asyncio.sleep(.6)
        embed = discord.Embed(
        title = f'***Kolbaser***\nSlavic Country Information',
        description = f'**Country**:`{c}`',
        colour = 0xdd16d9
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/699655178818814013/728014845630480514/me-flag.jpg')
        embed.add_field(name=f'{c}'.upper(), value='*Slavic Group:* **South Slavs**\n~\n*Capital:* **Podgorica**\n~\n*Population:* **622,359 thousand**\n~\n*Current president:* **Milo Đukanović**\n~\n*Currency:* **Euro**\n~\n*Government:* **Parliamentary-Republic**\n~\n*Language:* **Montenegrin**\n~\n*Current Nuclear Weapon stockpile:* **N/A**\n~\n*Weather:* **Mediterranean**')
        await ctx.send(embed=embed)
    elif c == 'serbia':
        await asyncio.sleep(.6)
        embed = discord.Embed(
        title = f'***Kolbaser***\nSlavic Country Information',
        description = f'**Country**:`{c}`',
        colour = 0xdd16d9
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/699655178818814013/728015071300812990/1200px-Flag_of_Serbia.svg.png')
        embed.add_field(name=f'{c}'.upper(), value='*Slavic Group:* **South Slavs**\n~\n*Capital:* **Belgrade**\n~\n*Population:* **6.982 million**\n~\n*Current president:* **Aleksandar Vučić**\n~\n*Currency:* **Serbian Dinar**\n~\n*Government:* **Parliamentary-Republic**\n~\n*Language:* **Serbian**\n~\n*Current Nuclear Weapon stockpile:* **[none]**\n~\n*Weather:* **Moderately Continental**')
        await ctx.send(embed=embed)
    elif c == 'slovenia':
        await asyncio.sleep(.6)
        embed = discord.Embed(
        title = f'***Kolbaser***\nSlavic Country Information',
        description = f'**Country**:`{c}`',
        colour = 0xdd16d9
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/699655178818814013/728015350414966875/1920px-Flag_of_Slovenia.svg.png')
        embed.add_field(name=f'{c}'.upper(), value='*Slavic Group:* **South Slavs**\n~\n*Capital:* **Ljubljana**\n~\n*Population:* **2.081 million**\n~\n*Current president:* **Borut Pahor**\n~\n*Currency:* **Euro**\n~\n*Government:* **Parliamentary-Republic**\n~\n*Language:* **Slovenian**\n~\n*Current Nuclear Weapon stockpile:* **[none]**\n~\n*Weather:* **Moderately Continental**')
        await ctx.send(embed=embed)

@client.command(pass_context=True)
async def musics(ctx):
    embed = discord.Embed(
    title = '***Kolbaser***\nMusic Information',
    colour = 0xdd16d9
    )
    embed.add_field(name='Hardbass Artists:', value='XS Project = xsp\nDJ Blyatman = djb\nHard Bass School = hbs\nUamee = u\nGopnik McBlyat = gmb\nRussian Village Boys = rvb\nSrpskibass = srpb\nHard Bass Crew = hbc\n[more coming soon!]', inline=False)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def music(ctx, genre: str, artist: str):
    await ctx.send(f'{ctx.author.mention} Getting song....')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)
    if genre == 'hardbass' and artist == 'xsp':
        xsps = ["Vodovorot\nhttps://www.youtube.com/watch?v=XwOOt0XRqqk",
               "Meanwhile in Russia\nhttps://www.youtube.com/watch?v=AyDi8kI9gp0",
               "Bochka, Bass, Kolbaser\nhttps://www.youtube.com/watch?v=r5uzc3U8Qhc",
               "Red Roubles\nhttps://www.youtube.com/watch?v=j7B4ACeXBHU",
               "Hardstyle Melody\nhttps://www.youtube.com/watch?v=xcNIBdKadVw",
               "Louder\nhttps://www.youtube.com/watch?v=3fEg1r6SH9Q",
               "Gagarin\nhttps://www.youtube.com/watch?v=gxVvv1cCAWY",
               "Grozny\nhttps://www.youtube.com/watch?v=d6qnsOrI070",
               "Fat Albert\nhttps://www.youtube.com/watch?v=TrAcFEtbTYk",
               "Pumping Storm\nhttps://www.youtube.com/watch?v=XajIiJs6uFs",
               "Russia is Rave\nhttps://www.youtube.com/watch?v=Ac4dKqrs6QQ",
               "Hard Bass Star\nhttps://www.youtube.com/watch?v=yAxWl72m2fc",
               "Gormonalno\nhttps://www.youtube.com/watch?v=Gh9huqRMaqw",
               "Squat\nhttps://www.youtube.com/watch?v=PdlcTpu6_ME",
               "Bass Experiment\nhttps://www.youtube.com/watch?v=Fd2Beu3GN3k",
               "Counter Strike\nhttps://www.youtube.com/watch?v=ZH60JNzeGpA",
               "Amphorobot\nhttps://www.youtube.com/watch?v=m3O2BH91LZk",
               "Balalaika\nhttps://www.youtube.com/watch?v=_k9Wcvn5Vg8",
               "Escobar\nhttps://www.youtube.com/watch?v=nY_SUw7yB-M",
               "Raz\nhttps://www.youtube.com/watch?v=ebARcPtYlUA",
               "Cocaine\nhttps://www.youtube.com/watch?v=eUSa9Mqa-dA",
               "Able to Love\nhttps://www.youtube.com/watch?v=IgE-e_gYGdg",
               "1 Oak\nhttps://www.youtube.com/watch?v=mcOFmtsxtyA",
               "Kolbasa\nhttps://www.youtube.com/watch?v=zw4Ui6SsFOs",
               "Turbulence\nhttps://www.youtube.com/watch?v=EzhuEyS-tFU",
               "Narkobaroni\nhttps://www.youtube.com/watch?v=aNPbdD53yJM",
               "Acid Trip\nhttps://www.youtube.com/watch?v=_A7IxRTFd6E",
               "Pumping Storm\nhttps://www.youtube.com/watch?v=XajIiJs6uFs",
               "Molot\nhttps://www.youtube.com/watch?v=x1Qqf6xNano",
               "BDSM\nhttps://www.youtube.com/watch?v=kbUV7w5r-uY",
               "Monstro\nhttps://www.youtube.com/watch?v=CVOfGMEkLho",
               "Bass Experiment\nhttps://www.youtube.com/watch?v=Fd2Beu3GN3k",
               "Reshaet Pump\nhttps://www.youtube.com/watch?v=6JppwWlVFUA",
               "Na Kolbasu\nhttps://www.youtube.com/watch?v=XbEndM4IJsQ",
               "Порошочек\nhttps://www.youtube.com/watch?v=8tpn4nd6wXo",
               "Bad Romance Remix\nhttps://www.youtube.com/watch?v=TrO0YkdkOLY",
               "DJ\nhttps://www.youtube.com/watch?v=j92ZDFmpkuM",
               "Voda\nhttps://www.youtube.com/watch?v=3UQZlhmtWL4",
               "Life is Pump\nhttps://www.youtube.com/watch?v=19NSNYNN0-8",
               "Kukuruzina\nhttps://www.youtube.com/watch?v=Elw5fHKcRNI",
               "Pilesosy\nhttps://www.youtube.com/watch?v=Qe1rfase8VQ",
               "July\nhttps://www.youtube.com/watch?v=j5S1zEiLnmo",
               "Zhelezno\nhttps://www.youtube.com/watch?v=1y8589IMbhw",
               "Ne Stoi\nhttps://www.youtube.com/watch?v=b82UFCmTXRI",
               "Na Kolesah\nhttps://www.youtube.com/watch?v=FP2q2Dph2E0",
               "Deadheads\nhttps://www.youtube.com/watch?v=WT4gN6veRMY"]
        await ctx.send('Getting song.....')
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(

        title = f'***Kolbaser***\n**XS Project**',
        description = f'{random.choice(xsps)}',
        colour = 0xdd16d9
        )
        await ctx.send(embed=embed)
        return

    elif genre == 'hardbass' and artist == 'djb':
        djbs = ["Slav King\nhttps://www.youtube.com/watch?v=QIjKijhv1OU",
                "Gopnik\nhttps://www.youtube.com/watch?v=2tch4J_pP9o",
                "Cyka Blyat\nhttps://www.youtube.com/watch?v=056HFwR5CW0",
                "Generation Hardbass\nhttps://www.youtube.com/watch?v=Ph4MUCD90Yo",
                "Instababe\nhttps://www.youtube.com/watch?v=7114Ojew1ZM&list=RDiobUHYGlUlY&index=11",
                "Tsar Bomb\nhttps://www.youtube.com/watch?v=JsCfAmCpVrE",
                "Kalashnikov\nhttps://www.youtube.com/watch?v=fIRD6_e1ElQ",
                "Babushka\nhttps://www.youtube.com/watch?v=1ZM1Yz7f4Lk",
                "Boris\nhttps://www.youtube.com/watch?v=5v32Eb_OSuY",
                "Kompot\nhttps://www.youtube.com/watch?v=fksEkuGPXzI",
                "Balalaika\nhttps://www.youtube.com/watch?v=ze_94FDyzPw",
                "Chernobyl\nhttps://www.youtube.com/watch?v=5YSH-0DRXJU",
                "Russian Express\nhttps://www.youtube.com/watch?v=rg2v6DEwL9A",
                "Stalin\nhttps://www.youtube.com/watch?v=IjsyGXKb8M8",
                "Send Nukes\nhttps://www.youtube.com/watch?v=kXQ1vHHzmXA",
                "Donk Kong\nhttps://www.youtube.com/watch?v=DEU9dqB0Wo4&list=PLir6QRYQ2ody6rCnN_bs_KmmnADeHpdd1&index=4&t=0s",
                "Slav\nhttps://www.youtube.com/watch?v=er0Unn8Ch9I&list=PLir6QRYQ2ody6rCnN_bs_KmmnADeHpdd1&index=33",
                "Supreme Gopnik\nhttps://www.youtube.com/watch?v=1dWG2MfG6Vw&list=PLir6QRYQ2ody6rCnN_bs_KmmnADeHpdd1&index=34",
                "Black Volga\nhttps://www.youtube.com/watch?v=Ep_uOynv7jo",
                "Blitzkrieg\nhttps://www.youtube.com/watch?v=o9ul0l4xXrA",
                "How We Party\nhttps://www.youtube.com/watch?v=agV86_dFVOE",
                "Gopboss\nhttps://www.youtube.com/watch?v=tJM396aUdkc",
                "Lunapark\nhttps://www.youtube.com/watch?v=mDQl89xMyWo",
                "District Gop\nhttps://www.youtube.com/watch?v=KUnmrhhCltQ",
                "Peirogi\nhttps://www.youtube.com/watch?v=wqeJEySfkmg",
                "Kosmos\nhttps://www.youtube.com/watch?v=Dyq-JW8Km50",
                "Visegrad 4\nhttps://www.youtube.com/watch?v=boIqkpXREQY",
                "Our Sound\nhttps://www.youtube.com/watch?v=oMGvuiZfS_o",
                "Kamaz\nhttps://www.youtube.com/watch?v=dzTAPY4uEYE",
                "SLAVIC NAMES\nhttps://www.youtube.com/watch?v=OZa2pFjvyAc",
                "Moonraker\nhttps://www.youtube.com/watch?v=msZWpG1jHxg",
                "Sputnik\nhttps://www.youtube.com/watch?v=H5oEUZOHUH4",
                "Cocaina\nhttps://www.youtube.com/watch?v=_9nIJYR7xTU",
                "Shutdown\nhttps://www.youtube.com/watch?v=F-3qQ9HIc3o",
                "Eastern Bloc\nhttps://www.youtube.com/watch?v=7MqS263kA84",
                "Duga\nhttps://www.youtube.com/watch?v=Cif2mT6g7ws",
                "Slav Brothers\nhttps://www.youtube.com/watch?v=tBvMJuWsyUQ",
                "Tetris\nhttps://www.youtube.com/watch?v=7gSS4h47rLU",
                "Arvelaus\nhttps://www.youtube.com/watch?v=-DupUxNt7k8",
                "Sapsan\nhttps://www.youtube.com/watch?v=q3sOu52Uk_M",
                "Molotov\nhttps://www.youtube.com/watch?v=tzVNzhp9oBI",
                "Night in Pripyat\nhttps://www.youtube.com/watch?v=SyX2fzZKDkc",
                "Blast\nhttps://www.youtube.com/watch?v=pORLuviX-Qg"]
        await ctx.send('Getting song.....')
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(

        title = f'***Kolbaser***\n**DJ Blyatman**',
        description = f'{random.choice(djbs)}',
        colour = 0xdd16d9
        )
        await ctx.send(embed=embed)
        return

    elif genre == 'hardbass' and artist == 'hbs':
        hbss = ["Narkotik Kal\nhttps://www.youtube.com/watch?v=fro6je9L5kg",
                "Nash Gimn\nhttps://www.youtube.com/watch?v=BTKZ_VwUcO8",
                "Narkoman\nhttps://www.youtube.com/watch?v=RBfrfSNX6ts",
                "Opa Blja\nhttps://www.youtube.com/watch?v=IY8TLY7gY0Q",
                "Sex, Kvass, Hardbass\nhttps://www.youtube.com/watch?v=6CwFkWHCqa4",
                "Ljutyj Hardbass\nhttps://www.youtube.com/watch?v=cVSRoOG7Fig",
                "Slav\nhttps://www.youtube.com/watch?v=nraKxjjY2Ks",
                "Tancuj Hardbass\nhttps://www.youtube.com/watch?v=N0IuN1_R2q8",
                "Gop FM\nhttps://www.youtube.com/watch?v=btwOYJs7QsU",
                "V Kashu\nhttps://www.youtube.com/watch?v=DAGw3dUztKU",
                "Nikolaj Hardbaskov\nhttps://www.youtube.com/watch?v=ICtwICj7p6c",
                "Russian Undergroun\nhttps://www.youtube.com/watch?v=qZn6qEKiy1I",
                "SPB Hardcore\nhttps://www.youtube.com/watch?v=W1dknwtkneQ",
                "Western Spy\nhttps://www.youtube.com/watch?v=Rk3Y79LO-JM",
                "228\nhttps://www.youtube.com/watch?v=HdEzvnK-N-o",
                "Gribniki Rossii\nhttps://www.youtube.com/watch?v=qfxNrOZqc3A",
                "Sportpit\nhttps://www.youtube.com/watch?v=eP68VAflkmU",
                "Y.K.P\nhttps://www.youtube.com/watch?v=lvHDTLmw1-0",
                "Pump-Shlah\nhttps://www.youtube.com/watch?v=jeXqtsMrv6o",
                "Bratan\nhttps://www.youtube.com/watch?v=Qu0z9jwTJ3k",
                "Russians Choose ADIDAS\nhttps://www.youtube.com/watch?v=CLXXW68W4zw",
                "Olya Bomzh\nhttps://www.youtube.com/watch?v=4ofOYoSMOZs",
                "Zakladki\nhttps://www.youtube.com/watch?v=IP_eXGtgLTo",
                "Vice City\nhttps://www.youtube.com/watch?v=XqkQkxQUzII",
                "Area 51\nhttps://www.youtube.com/watch?v=lvGeG21UX70",
                "Most Wanted\nhttps://www.youtube.com/watch?v=qev_jgN0grI",
                "Opa Blja Remix\nhttps://www.youtube.com/watch?v=7G4UbaMoSLw"]
        await ctx.send('Getting song.....')
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(

        title = f'***Kolbaser***\n**Hard Bass School**',
        description = f'{random.choice(hbss)}',
        colour = 0xdd16d9
        )
        await ctx.send(embed=embed)
        return

    elif genre == 'hardbass' and artist == 'u':
        us = ["High Quality Nahui\nhttps://www.youtube.com/watch?v=Z4NzClCMmNc",
                      "Kopeika\nhttps://www.youtube.com/watch?v=7PPNxYtgz0Q",
                      "IL-76\nhttps://www.youtube.com/watch?v=Y_-QonjPdUo",
                      "Tracksuit\nhttps://www.youtube.com/watch?v=kiZnmnPkKX4",
                      "Pripyat at Night\nhttps://www.youtube.com/watch?v=E8vPf_g-NrA",
                      "Protivogaz\nhttps://www.youtube.com/watch?v=2TA9_1OwRoU",
                      "Protivogaz Remix\nhttps://www.youtube.com/watch?v=dM2f0_K8nLI",
                      "Out of Kvass\nhttps://www.youtube.com/watch?v=7kiNUCkB1PU",
                      "Makarov\nhttps://www.youtube.com/watch?v=4CYLoj_sSqU",
                      "Gopnik Interntional\nhttps://www.youtube.com/watch?v=MhYLi3737Qw",
                      "Rush B\nhttps://www.youtube.com/watch?v=xBhCaCuGJYM",
                      "Town Called Cyka Blyat\nhttps://www.youtube.com/watch?v=dhmfosCx4sI",
                      "Perestroik\nhttps://www.youtube.com/watch?v=gg9HC-hkIfQ",
                      "Davai Patsani\nhttps://www.youtube.com/watch?v=2exqMAl1Pbk",
                      "October\nhttps://www.youtube.com/watch?v=j5kqniGM3X4",
                      "Squatvia\nhttps://www.youtube.com/watch?v=3ZWYb3I5Tss",
                      "The Sausage\nhttps://www.youtube.com/watch?v=-v3a1-8pASM",
                      "Lada\nhttps://www.youtube.com/watch?v=4xei2-cW9eo",
                      "Halva\nhttps://www.youtube.com/watch?v=oLoT0dm88zU",
                      "AKM\nhttps://www.youtube.com/watch?v=QPSl5Z247Q0",
                      "Gamer Gopnik\nhttps://www.youtube.com/watch?v=iq9ClfJ8tqY",
                      "Monkey Business 2019\nhttps://www.youtube.com/watch?v=W4z8YrG28ys",
                      "Gop Stop\nhttps://www.youtube.com/watch?v=9fn4Zdy0mwY",
                      "Bass Boi\nhttps://www.youtube.com/watch?v=tbayNy9Dg-g",
                      "Gopota is Helpful\https://www.youtube.com/watch?v=bDaA0WtWrQ8",
                      "The Duck\nhttps://www.youtube.com/watch?v=HO2EWBrypTU",
                      "Robotnik\nhttps://www.youtube.com/watch?v=36I5wxJGurw",
                      "Zaraza\nhttps://www.youtube.com/watch?v=B0DN1Vd3VM4",
                      "House of the Rising Blin\nhttps://www.youtube.com/watch?v=3bXU6qlU0aQ",
                      "Slavic Nitrous\nhttps://www.youtube.com/watch?v=hV-AyjRDZek"]
        await ctx.send('Getting song.....')
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(

        title = f'***Kolbaser***\n**Uamee**',
        description = f'{random.choice(us)}',
        colour = 0xdd16d9
        )
        await ctx.send(embed=embed)
        return

    elif genre == 'hardbass' and artist == 'gmb':
        gmbs = ["Snakes in Tracksuits\nhttps://www.youtube.com/watch?v=LEjqfOKiGWE",
                "Cheeki Breeki Revolt\nhttps://www.youtube.com/watch?v=qQvwxmsRM64",
                "Murka\nhttps://www.youtube.com/watch?v=vwHXf9Hp5L4",
                "Negative Phase\nhttps://www.youtube.com/watch?v=PNLu4VlDYjU",
                "Bombjack\nhttps://www.youtube.com/watch?v=f24Ui6GDkmI",
                "Monolith\nhttps://www.youtube.com/watch?v=iznlpplO_6A",
                "Skytelaget 2017\nhttps://www.youtube.com/watch?v=ooV1ixzgu5c",
                "Hardbass Industry\nhttps://www.youtube.com/watch?v=gWfv-dOhzKE",
                "Szpion Detector\nhttps://www.youtube.com/watch?v=7qC2vAqTE2E",
                "Drug Test\nhttps://www.youtube.com/watch?v=erbG3Lg_8po",
                "Donkbringer\nhttps://www.youtube.com/watch?v=XdtPAxfbbUE",
                "Pumping Frenzy\nhttps://www.youtube.com/watch?v=5QbQpwsMgvE",
                "Journey\nhttps://www.youtube.com/watch?v=4RtWx62z1OU",
                "Breakout\nhttps://www.youtube.com/watch?v=7Jvph8tBCew",
                "Cyberpunk\nhttps://www.youtube.com/watch?v=3n2_sZayYoQ",
                "Tesla 2017\nhttps://www.youtube.com/watch?v=6EJYW6HDbIM",
                "Wicked Noise\nhttps://www.youtube.com/watch?v=_Y0FTz9YBtk",
                "UFO\nhttps://www.youtube.com/watch?v=CjlI-sYRkEU",
                "Polski Rave\nhttps://www.youtube.com/watch?v=YIp1cN-yI50",
                "Supreme Memebass Gavno\nhttps://www.youtube.com/watch?v=IFnmdbk2WC4",
                "Hot Stuff\nhttps://www.youtube.com/watch?v=X0V8ygIEEbY",
                "Clear Sky\nhttps://www.youtube.com/watch?v=d0KT4U7N2s4",
                "BLAST OFF\nhttps://www.youtube.com/watch?v=Awq9UveX_Cc",
                "Driller\nhttps://www.youtube.com/watch?v=n2M86BlglOY"]
        await ctx.send('Getting song.....')
        await asyncio.sleep(2)
        embed = discord.Embed(

        title = f'***Kolbaser***\n**Gopnik McBlyat**',
        description = f'{random.choice(gmbs)}',
        colour = 0xdd16d9
        )
        await ctx.send(embed=embed)
        return

    elif genre == 'hardbass' and artist == 'rvb':
        rvbs = ["Adidas\nhttps://www.youtube.com/watch?v=LNuVDtUUmd4",
                "Suckcess\nhttps://www.youtube.com/watch?v=o5JxFkcVQAM",
                "Dashcam\nhttps://www.youtube.com/watch?v=laxng4LI4S4",
                "Snollerboys\nhttps://www.youtube.com/watch?v=jaXBeVtwxxg",
                "Putindabass\nhttps://www.youtube.com/watch?v=ZLaOStTmRkw",
                "Run Away\nhttps://www.youtube.com/watch?v=rwJgYXwn5zQ",
                "Headbang\nhttps://www.youtube.com/watch?v=q4JNa8TNf5I",
                "Made in Russia\nhttps://www.youtube.com/watch?v=mtsv9ezc_pQ",
                "Cyka Blyat\nhttps://www.youtube.com/watch?v=NqM032dnPtk",
                "Razjebasser\nhttps://www.youtube.com/watch?v=yWt3Ko2R1Vg",
                "Ez Katka\nhttps://www.youtube.com/watch?v=J3k54wDsjP4",
                "Hangout\nhttps://www.youtube.com/watch?v=LedbTFjlZA0",
                "Instababe\nhttps://www.youtube.com/watch?v=7114Ojew1ZM",
                "Elephant's Dick\nhttps://www.youtube.com/watch?v=n6X7EeWmt90",
                "Don't Touch Yourself\nhttps://www.youtube.com/watch?v=WlQgvdkXTzY",
                "Cold Love\nhttps://www.youtube.com/watch?v=P758gY3jIJ4",
                "Forever Drunk\nhttps://www.youtube.com/watch?v=geVs-qVwp7s",
                "Ciao\nhttps://www.youtube.com/watch?v=SdiShYWUTCU",
                "Fuck that Shit\nhttps://www.youtube.com/watch?v=mg6skt8Y2mA"]
        await ctx.send('Getting song.....')
        await asyncio.sleep(2)
        embed = discord.Embed(

        title = f'***Kolbaser***\n**Russian Village Boys**',
        description = f'{random.choice(rvbs)}',
        colour = 0xdd16d9
        )
        await ctx.send(embed=embed)
        return

    elif genre == 'hardbass' and artist == 'srpb':
        sbs = ["The Srpski Style\nhttps://www.youtube.com/watch?v=Ogk1wISQOTA",
                   "Hardbass Generation\nhttps://www.youtube.com/watch?v=7h7sxT7E5C8&app=desktop",
                   "SlavBass\nhttps://www.youtube.com/watch?v=lOq5bPkauLY",
                   "The Wild Gopnik\nhttps://www.youtube.com/watch?v=-_A947Omw_k",
                   "Atomic Bomb\nhttps://www.youtube.com/watch?v=SP3DPY5KAlc",
                   "Hardbass Knight\nhttps://www.youtube.com/watch?v=Xbd9yaQ3RH4",
                   "Vodka Party\nhttps://www.youtube.com/watch?v=E81GMx37v3k",
                   "Combat\nhttps://www.youtube.com/watch?v=74WKRXA8nJ8",
                   "Your Mum GAY\nhttps://www.youtube.com/watch?v=YQmbyviVpGs",
                   "Fuckin' Bass\nhttps://www.youtube.com/watch?v=nGCHJPm0u-A",
                   "Land of the Donk\nhttps://www.youtube.com/watch?v=mOMcPFbz290&list=PLmjRPycy9f2_r0ekfmaYnJSF-hC2XoXyM&index=4",
                   "Danger Zone\nhttps://www.youtube.com/watch?v=leJvZktJ9sM&list=PLmjRPycy9f2_r0ekfmaYnJSF-hC2XoXyM&index=5",
                   "Hardbass Family\nhttps://www.youtube.com/watch?v=mcqGUaDLb0I&list=PLmjRPycy9f2_r0ekfmaYnJSF-hC2XoXyM&index=9",
                   "Donk Attack\nhttps://www.youtube.com/watch?v=BR0k4QPGzzk&list=PLmjRPycy9f2_r0ekfmaYnJSF-hC2XoXyM&index=15",
                   "Gopnik Refugee\nhttps://www.youtube.com/watch?v=p7a7VG2Ob18&list=PLmjRPycy9f2_r0ekfmaYnJSF-hC2XoXyM&index=63",
                   "KvassBass\nhttps://www.youtube.com/watch?v=WjbNqecpHO4&list=PLmjRPycy9f2_r0ekfmaYnJSF-hC2XoXyM&index=61",
                   "Pumping Attack\nhttps://www.youtube.com/watch?v=OHN5b6LoXGE&list=PLmjRPycy9f2_r0ekfmaYnJSF-hC2XoXyM&index=52"]
        await ctx.send('Getting song.....')
        await asyncio.sleep(2)
        embed = discord.Embed(

        title = f'***Kolbaser***\n**SrpskiBass**',
        description = f'{random.choice(sbs)}',
        colour = 0xdd16d9
        )
        await ctx.send(embed=embed)
        return

    elif genre == 'hardbass' and artist == 'hbc':
        hbcs = ["Zhestyanschiki - Bass\nhttps://www.youtube.com/watch?v=WLn84aeUxa8",
                "DJ Rentgen - Adrenaline\nhttps://www.youtube.com/watch?v=UbY_hU_DZDE",
                "DJ Rentgen - Final Destination\nhttps://www.youtube.com/watch?v=ci1kjqVMCvg",
                "DJ Rentgen - Mania\nhttps://www.youtube.com/watch?v=e4SSU2vTRso",
                "DJ Rentgen - FLASHBACK\nhttps://www.youtube.com/watch?v=TPcnDckx_t0",
                "DJ Rentgen - That's Funny\nhttps://www.youtube.com/watch?v=24r5VfDn3kw",
                "DJ Rentgen - Bass Fly\nhttps://www.youtube.com/watch?v=6rPe-ZL8tVM",
                "SPB Hard Bass Mafia - Drug Abuse\nhttps://www.youtube.com/watch?v=0_yuadETnt8",
                "SPB Hard Bass Mafia - Pum Pum\nhttps://www.youtube.com/watch?v=rtzodXMtPKE",
                "SiQuas - Las Hidroterapias\nhttps://www.youtube.com/watch?v=771cFe8mDtg",
                "UsDexx DJ's - Full Spectrum\nhttps://www.youtube.com/watch?v=ozatBXgZbaA",
                "HARDBOSS - Kolbaser's Anthem\nhttps://www.youtube.com/watch?v=2w6BzikX7gE",
                "Zhestyanschiki - Fuck You\nhttps://www.youtube.com/watch?v=Mzpp55V3Ctk",
                "UsDexx DJ's - Fucking Hard Bass\nhttps://www.youtube.com/watch?v=ihxEoULpQb0",
                "Sonic Mine - Fiesta Fatal\nhttps://www.youtube.com/watch?v=r1G28evWSWA",
                "Sonic Mine - Hard Bass Attack\nhttps://www.youtube.com/watch?v=9mGyRI73T6w",
                "Dr Poky - Dark Style 2\nhttps://www.youtube.com/watch?v=rCCBh9z5ER8",
                "UsDexx DJ's - Hymn\nhttps://www.youtube.com/watch?v=hn5m-LhZslU",
                "Zhestyanschiki - Party Alarm\nhttps://www.youtube.com/watch?v=NGcSJZ10c2U",
                "UsDexx DJ's - Bumping-Hardbass\nhttps://www.youtube.com/watch?v=ihp7yzcHLE0",
                "DBC - Breaking Donk\nhttps://www.youtube.com/watch?v=fXn-XrU6Nq0",
                "Zhestyanschiki - Upload\nhttps://www.youtube.com/watch?v=aNyIhGrhVhw",
                "Dr Poky - Kamikaze\nhttps://www.youtube.com/watch?v=NHGRLAinGcU",
                "SPB Hard Bass Mafia - Вот это бля\nhttps://www.youtube.com/watch?v=u03FCkDYUn0",
                "SPB Hard Bass Mafia - Без названия\nhttps://www.youtube.com/watch?v=lsKeFWAGZuw",
                "SPB Hard Bass Mafia & Hard Bass School - Anthem 2012\nhttps://www.youtube.com/watch?v=MKTBFodByho",
                "Sonic Mine - Hot Times\nhttps://www.youtube.com/watch?v=oqpTgPDIG-M",
                "Zhestyanschiki - Hard Pump\nhttps://www.youtube.com/watch?v=iyQyo_jEEq8",
                "Zhestyanschiki - Pumping Power\nhttps://www.youtube.com/watch?v=K0eec0KTQpU",
                "Darktosh - Speedway\nhttps://www.youtube.com/watch?v=Dm2q5WHSe3U",
                "Just Motion - The Rite\nhttps://www.youtube.com/watch?v=VM4CEnjFHSQ",
                "DJ Rentgen - Island Storm\nhttps://www.youtube.com/watch?v=wM0jatC1GdU",
                "Kolbaser Project - Skorost Ferum Kolbasa\nhttps://www.youtube.com/watch?v=P_Eb0VO9-dQ"]
        await ctx.send('Getting song.....')
        await asyncio.sleep(2)
        embed = discord.Embed(

        title = f'***Kolbaser***\nHard Bass Crew',
        description = f'{random.choice(hbcs)}',
        colour = 0xdd16d9
        )
        await ctx.send(embed=embed)
        return

    elif genre == 'hiphop' and artist == 'nwa':
        niggaz = ["Fuck Tha Police\nhttps://www.youtube.com/watch?v=c5fts7bj-so",
                  "Straight Outta Compton\nhttps://www.youtube.com/watch?v=TMZi25Pq3T8",
                  "Dope Man\nhttps://www.youtube.com/watch?v=umUHR1JlT_c",
                  "Gangsta Gangsta\nhttps://www.youtube.com/watch?v=KHaOul8gVVc",
                  "Chin Check\nhttps://www.youtube.com/watch?v=9vAmKdgrLf8",
                  "Alwayz Into Somethin'\nhttps://www.youtube.com/watch?v=RxAEXUyGM94",
                  "100 Miles and Runnin'\nhttps://www.youtube.com/watch?v=hgUeO1hokh8",
                  "Appetite for Destruction\nhttps://www.youtube.com/watch?v=P-wP2jUBlcE",
                  "Real Niggaz\nhttps://www.youtube.com/watch?v=-7sQ35MUdOY",
                  "Boyz-N-Tha-Hood\nhttps://www.youtube.com/watch?v=VJp7eJx4RkE",
                  "Real Niggaz Don't Die\nhttps://www.youtube.com/watch?v=FhUS55CbyJA",
                  "If It Ain't Ruff\nhttps://www.youtube.com/watch?v=3h2XHm3iFxo",
                  "I Ain't Tha 1\nhttps://www.youtube.com/watch?v=STtwzLVAa1s",
                  "Findum Fuckum & Flee\nhttps://www.youtube.com/watch?v=GLXT5kgelDw",
                  "One Less Bitch\nhttps://www.youtube.com/watch?v=IQxf4odCz9A",
                  "Approach To Danger\nhttps://www.youtube.com/watch?v=rTdCZK2e3o0",
                  "The Dayz of Wayback\nhttps://www.youtube.com/watch?v=wtEpF01DNAM"]
        await ctx.send('Getting song.....')
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(

        title = f'***Kolbaser***\n**N.W.A**',
        description = f'{random.choice(niggaz)}',
        colour = 0xdd16d9
        )
        await ctx.send(embed=embed)
        return

@client.command(pass_context=True)
async def roulette(ctx):
    await ctx.send(f'You have started a game of Russian Roulette! {ctx.author.mention}\nType `k spin` to play!')
    @client.command(pass_context=True)
    async def spin(ctx):
        await ctx.send(f'Spinning...')
        await asyncio.sleep(3.2)
        await ctx.channel.purge(limit=1)
        await ctx.send('Ready when you are cyka\nType `k fire`')
        @client.command(pass_context=True)
        async def fire(ctx):
            responses = ["Safe!",
                        "Close one",
                        "You are a very lucky guy",
                        "Miss!",
                        "**BANG!**",
                        "Oof, you just took a bullet to the head",
                        "You got scared and moved, so the bullet only grazed you",
                        "**BOOM** HEADSHOT!",
                        "Aw shit, you got your blood all over my new shoes!",
                        "R.I.P",
                        "Lucky you, the gun jammed",
                        "I will send flowers and my sincerest condolences to your family",
                        "You lucky fuck",
                        "The bullet went straight through your temple, killing you instantly"]

            await asyncio.sleep(1.5)
            await ctx.channel.send(f'{random.choice(responses)} {ctx.author.mention}\nType `k spin` to play again!')

def get_kolbasa():
    my_path3 = r'C:\Users\HF\Pictures\Kolbasa\png'
    filename = random.choice([os.path.join(my_path3,name) for name in os.listdir(my_path3)])
    return filename
@client.command()
async def kolbasa(ctx):
    kpic = get_kolbasa()
    await asyncio.sleep(.2)
    await ctx.send('***Kolbaser***\nKolbasa')
    await ctx.send(file=discord.File(kpic))

def get_meme_image():
    my_path = r'C:\Users\HF\Pictures\SlavMemes\SonaMemes'
    filename = random.choice([os.path.join(my_path,name) for name in os.listdir(my_path)])
    return filename
@client.command(pass_context=True)
async def meme(ctx):
    meme = get_meme_image()
    await asyncio.sleep(.2)
    await ctx.send('***Kolbaser***\nMeme')
    await ctx.send(file=discord.File(meme))

def get_boob_image():
    my_path1 = r'C:\Users\HF\Desktop\F Files\F9\Penumbra\Penumbra 2020 OUTDATED\Penumbra-Chive'
    filename = random.choice([os.path.join(my_path1,name) for name in os.listdir(my_path1)])
    return filename
@client.command(pass_context=True)
async def flbp(ctx):
    flbp = get_boob_image()
    await asyncio.sleep(.2)
    await ctx.send('***Kolbaser***\nFLBP')
    await ctx.send(file=discord.File(flbp))

def get_russia_shit():
    mp69 = r'C:\Users\HF\Videos\Russia shit'
    filename = random.choice([os.path.join(mp69,name) for name in os.listdir(mp69)])
    return filename
@client.command(pass_context=True)
async def russia(ctx):
    russia = get_russia_shit()
    await asyncio.sleep(.2)
    await ctx.send('***Kolbaser***\n***RUSSIA!***')
    await ctx.send(file=discord.File(russia))

def get_video():
    my_path5 = r'C:\Users\HF\Videos\funny vids'
    filename5 = random.choice([os.path.join(my_path5,name) for name in os.listdir(my_path5)])
    return filename5
@client.command(pass_context=True)
async def vid(ctx):
    fv = get_video()
    await asyncio.sleep(.2)
    await ctx.send('***Kolbaser***\nVideo')
    await ctx.send(file=discord.File(fv))

@client.command(pass_context=True)
async def tpb(ctx):
    embed = discord.Embed(
    title = "***Trailer Park Boy's***\nQuote Machine",
    description = 'This will allow you to select a character from Trailer Park Boys\nand then print a quote from selected character!',
    colour = 0xdd16d9
    )
    embed.add_field(name='Ricky', value='Enter `k r` for Ricky', inline=False)
    embed.add_field(name='Julian', value='Enter `k j` for Julian', inline=False)
    embed.add_field(name='Bubbles', value='Enter `k b` for Bubbles', inline=False)
    embed.add_field(name='Jim Lahey', value='Enter `k jl` for Jim Lahey', inline=False)
    embed.add_field(name='Randy', value='Enter `k ry` for Randy', inline=False)
    embed.add_field(name='Cyrus', value='Enter `k c` for Cyrus', inline=False)
    await ctx.send(embed=embed)
    @client.command(pass_context=True)
    async def r(ctx):
        rq = ["*A link is only as long as your longest strong chain*",
              "*All for all and one for one*",
              "*Al-I-Ga-tor*",
              "*Can you give me a bit of credjudice?*",
              "*Cock-a-doodle Fucking Ketchup Chips*",
              "*It's better to have a gun and need it than to not have a gun and not need it*",
              "*What comes around is all around*",
              "*What the fuck is tempus fuck it?*",
              "*One man's garbage is another man person's good ungarbage*",
              "*Keep your friends close, but your enemies toaster*",
              "*What the fuck does tempus fuckit mean?*",
              "*I dont have enough people words to make it understand you the way it understands me	*",
              "*Cock-a-doodle Fucking Ketchup Chips*",
              "*Jim Lahey is a Fuckin Drunk and he always will be*",
              "*Fuck my ass and tits!*",
              "*Will you for to be fuckin' married to me?*",
              "*Fucking slut!*"]
        await ctx.send('Getting quote.....')
        await asyncio.sleep(3)
        embed = discord.Embed(

        title = '***Kolbaser***\n**Ricky Quote**',
        description = f'{random.choice(rq)}',
        colour = 0xdd16d9
        )
        await ctx.send(embed=embed)
        return

    @client.command(pass_context=True)
    async def j(ctx):
        jq = ["*Did They Just Call Me Patrick Swayze?*",
              "*I'm Either Gonna Become An Electrician, A Meat Cutter, Or I'm Gonna Get Into Television And Radio Broadcasting.*",
              "*Would You See DeNiro Doing A Porn Flick?*",
              "*I Don't Care About Your Ass, Ricky!*",
              "*Go Mow Some Lawns Or Something, You Greasy Bastard.*",
              "*Randy, A Lot Of Barbecues Look Alike. You're Probably On Drugs Or Confused Or Something, Like You Usually Are.*",
              "*Listen, Why Don't You Try Focusing On The Weed A Bit More, OK?*",
              "*You're Here For One Reason And That's To Sell Drugs, Okay? Stay Focused, Man.*",
              "*You’re Prostituting Yourself Out For Cheeseburgers Again, Aren’t You?*",
              "*Listen, Just Pretend You're On Mushrooms, All Right? Just Go With It.*",
              "*Got a big enough of a joint there, Rick?*"]
        await ctx.send('Getting quote.....')
        await asyncio.sleep(3)
        embed = discord.Embed(

        title = '***Kolbaser***\n**Julian Quote**',
        description = f'{random.choice(jq)}',
        colour = 0xdd16d9
        )
        await ctx.send(embed=embed)
        return

    @client.command(pass_context=True)
    async def b(ctx):
        bq = ["*Well, When I Was A Little Guy, I Always Wanted To Go Up Into Space, Be A Spaceman. But You Gotta Be Able To See Really Fuckin' Good To Do That Job*",
              "*I Don't Want To Be Known As The Guy Who Walks Up And Slaps Badonkadonks*",
              "*Ricky, Can't We Just Have One Day Of No Yelling And No Horse Shit And Just Play Some Fucking Hockey?*",
              "*On Special Occasions, I Always Pound The Liquor Into Me, Julian*",
              "*...If You Love Something, Let It Go. If It Comes Back To You, You Own It. If It Doesn’t, You Don’t Own It. And If It Doesn’t You’re An Asshole, Just Like You*",
              "*Lahey, Can You Please Get The Flying Fuck Out Of Our Way? We Gotta Go Get Rush Tickets!*",
              "*I Can't Wait To Start Fuckin' Hammerin' People!*",
              "*When Somebody Like Alex Lifeson Gives You A Fuckin' T-Shirt To Put On, You're Puttin' The Fuckin' Thing On. I Don't Care If You Don't Wear Shirts*",
              "*Man, I Hope It's Not A Fucking Samsquanch...*",
              "*I Can Eat A Fuckin' Bucket Myself*",
              "*COCKSUCKER!!!*",
              "*Boys, I am so fucking hungry, I could eat the arse out of a dead skunk*"]
        await ctx.send('Getting quote.....')
        await asyncio.sleep(3)
        embed = discord.Embed(

        title = '***Kolbaser***\n**Bubbles Quote**',
        description = f'{random.choice(bq)}',
        colour = 0xdd16d9
        )
        await ctx.send(embed=embed)
        return

    @client.command(pass_context=True)
    async def jl(ctx):
        jlq = ["*Putting the word 'shit' before anything*",
                   "*I'm mowing the air Rand, i'm mowing the air!*",
                   "*I am the liquor*",
                   "*The only difference between you and me is a couple of drinks*",
                   "*I'm sober enough to know what I'm doing and drunk enough to really enjoy it*",
                   "*Clean and sober, just mean that I'm showered and heading to the liquor store*",
                   "*Just one more little drinky-poo*",
                   "*The liquor's calling the shots now, Randy!*",
                   "*Randy, I've decided to lay off the food for a bit, and go on the booze*",
                   "*Feelin' a little sluggish, think I need a snap of the white liquor*",
                   "*The liquor will do the driving, then we'll just kick back on booze control*",
                   "*You don’t cross my shit line, I don’t cross your shit line. When he told everyone I was drinking again, he crossed the goddamn shit line.*",
                   "*Lim Jahey*",
                   "*These things have a way of working themselves out. I’m gonna let the liquor do the thinking.*"]
        await ctx.send('Getting quote.....')
        await asyncio.sleep(3)
        embed = discord.Embed(

        title = '***Kolbaser***\n**Jim Lahey Quote**',
        description = f'{random.choice(jlq)}',
        colour = 0xdd16d9
        )
        await ctx.send(embed=embed)
        return

    @client.command(pass_context=True)
    async def ry(ctx):
        ryq = ["*FROZEN MIXED VEGETABLE COCKS!!!*",
              "*A man's gotta eat*",
              "*Not another night of the shit-abyss, please.*",
              "*Barb, your scalloped potatoes are FUCKED!!!*",
              "*Sweet and sour chicken balls!*",
              "*LOCH NESS MONSTER BALLS, I'VE BEEN SHOT!*",
              "*FRIG OFF!*",
              "*Joy comes from places you least expect it. It's usually the simple things, like watching my son play basketball or going through Central Park when the blossoms are blooming.*",
              "*You'll kiss his bare ass?*",
              "*Let the liquor do the thinking, right Mr. Lahey?*",
              "*ALFRED HITCHCOCK!!!*",
              "*Fuck you Mr. Lahey, I need a cheeseburger!*",
              "*No, there was a tiger and it ate 7 cheeseburgers!*"]
        await ctx.send('Getting quote.....')
        await asyncio.sleep(3)
        embed = discord.Embed(

        title = '***Kolbaser***\n**Randy Quote**',
        description = f'{random.choice(ryq)}',
        colour = 0xdd16d9
        )
        await ctx.send(embed=embed)
        return

    @client.command(pass_context=True)
    async def c(ctx):
        cq = ["*Fuck off, I've got work to do*",
              "*Told me he was proud of me once...fucking prick*",
              "*Safety, always off*",
              "*I carry a Glock, no safety, no risk of running afoul of Cyrus' Law*",
              "*Hey! That's my shit!! That's my shit!*",
              "*We don't want any trouble, BUT WHAT WE DON'T MIND MAKING SOME!*",
              "*HERE'S FUCKING CYRUS!*",
              "*Why don't we fuck on*",
              "*And it ain't over till the fat lady sings... While she's blowing me!*",
              "*Ladies! The boss is home. It's been a long time no see, dickweeds.*",
              "*Well well well... If it isn't the big, tough Julianne, the Hubble-Bubble telescope, and Helmet Head.*",
              "*And what's this, I'm a fuckhead? Huh?*"]
        await ctx.send('Getting quote.....')
        await asyncio.sleep(3)
        embed = discord.Embed(

        title = '***Kolbaser***\n**Cyrus Quote**',
        description = f'{random.choice(cq)}',
        colour = 0xdd16d9
        )
        await ctx.send(embed=embed)
        return

@client.command(pass_context=True)
async def joke(ctx):
    embed = discord.Embed(
        title = '***Kolbasers Joke Hub***',
        description = 'Хороший день для тебя!\nGood day to you!',
        colour = 0xdd16d9

    )
    jokes = ["What is 75 meters long and only eats potatoes?:\n\n\n\n||A queue of soviet workers waiting to get meat||",
         "What do you call a sick bird?:\n\n\n\n||Illegal||",
         "Stalin, during a speech: “||I am prepared to give my blood for the cause of the working class, drop by drop.||”",
         "Why did the gamer cross the road?:\n\n\n\n||To render the rock on the other side||",
         "Communism...:\n\n\n\n||Its a party||",
         "What is the difference between a capitalist fairy tale and a Marxist fairy tale?\n\n\n\n:||A capitalist fairy tale begins, 'Once upon a time, there was...''. A Marxist fairy tale begins, 'Some day, there will be....''||",
         "What is the difference between jews and pizza?:\n\n\n\n||Pizza doesn't scream when it gets put it the oven||",
         "What is the difference between a tire and 365 used-condoms?:\n\n\n\n||One is a Goodyear. The other is *great* year||",
         "What's another name for a vagina?:\n\n\n\n||The box a penis comes in||",
         "How do you circumsize a hillbilly?:\n\n\n\n||Kick his sister in the jaw||",
         "An American man, A Mexican man, and an Iranian man are in Hell, they each ask the devil if they can make one last phone call to their family, the devil complies.\n He lets the American go first. The American talks for 45 minutes and pays $125, the Mexican talks for 1 hour and pays $150,\n the Iranian man talks for 1 hour and pays $10, when the other 2 men protest, the devil tells them:\n||*A call from hell to hell is local*||",
         "A man has sex with a Lady of the Evening for 5 dollars, and when he wakes up the next morning he has crabs, so he goes back to the lady and complains, and so the lady says:\n\n\n||Well what did you expect? Lobster?||",
         "What did the penis say to the vagina?:\n\n\n||Don't make me come in there||",
         "What is the difference between a pregnant woman and a lightbulb?:\n\n\n||You can't unscrew a lightbulb||",
         "What does the sign on an out-of-business brothel say?:\n\n\n||Beat it. We’re closed||",
         "Why was the guitar teacher arrested?:\n\n\n||For fingering a minor||",
         "Know what a 6.9 is?:\n\n\n||Another good thing screwed up by a period||",
         "What did the O say to the Q?:\n\n\n||Dude, your dick is hanging out||",
         'Three men are sitting in a cell in the (KGB headquarters) Dzerzhinsky Square. The first asks the second why he has been imprisoned, who replies, "Because I criticized Karl Radek." The first man responds, "But I am here because I spoke out in favor of Radek!" They turn to the third man who has been sitting quietly in the back, and ask him why he is in jail. He answers,\n\n\n||"I am Karl Radek."||']

    await asyncio.sleep(2)
    embed = discord.Embed(
    title = '***Kolbaser*** *Joke*\n\nHere, have a joke and иди на хуй',
    description = f'{random.choice(jokes)}',
    colour = 0xdd16d9
    )
    await ctx.send(embed=embed)

@client.command(aliases=['8ball'])
async def ask(ctx, *, question):
    responses = ["It is certain",
                 "Yeah pretty much",
                 "Damn straight",
                 "Duh, blyat",
                 "You can count on it!",
                 "blin, i dont give a fuck",
                 "What was the question again?",
                 "Nah",
                 "Double Nah",
                 "I like bread",
                 "Idi nahui",
                 "Opa blja!",
                 "Yes",
                 "Blyat cyka urod",
                 "Blyat how the fuck should i know?",
                 "ERROR, 8BALL IS TEMPORAILY OUT-OF-ORDER, TRY AGAIN LATER",
                 "Da, pidoras",
                 "Better not tell you now, cyka blyat",
                 "Does a bear shit in the woods?",
                 "Invalid parameters",
                 "Why are you asking me this",
                 "I think not",
                 "Depends...",
                 "нет",
                 "Too drunk too answer your question, ask again NEVER",
                 "Why are you asking me, blin?"]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(pass_context=True)
async def hack(ctx, member: discord.Member):
    fake_passwords = ["`quertyfuck`", "`i-like-men69`", "`i_haz_small_dick111`", "`asdfghjkl69`", "`xxx6969420xXx`"]
    fake_emails = ["`xxxgay4idriselbaxxx@hotmail.com`", "`xxx_i_like_boyz@gmail.com`", "`xGay4Trump@aol.com`", "`hf6969@gmail.com`", "`x6hawtlesboactionx@hotmail.com`"]
    fake_device_names = ["`Gayfucker`", "`bond007`", "`fortnite4life`", "`dicks`", "`Idris_Elba`", "`White4Lyfe`"]
    fake_ssns = ["`666-420-6969`", "`123-419-8886`", "`069-690-8008`", "`123-456-6969`", "`420-420-1111`"]
    fake_device_passwords = ["`123456789`", "`Monk3yFuck3r`", "`penisface`", "`i_like_2_suck_dix`", "`Gay4IdrisElba`"]
    fake_addresses = ["`123 Happy Street`", "`239 Walt Whitman St.Fuckface, NJ 07006`", "`862 Wayne St.Land O Niggaz, FL 34639`", "`9631 NW. Penis licker Road, MD 21221`"]
    fake_names = ["`A.S. Muncher`", "`Amanda D. P. Throat`", "`Ben O. Verbich`", "`Anita Hanjaab`", "`Buster Himen`", "`Dick Pound`", "`Dixon B. Tweenerlegs`", "`Harry Johnson`", "`Ben Dover`", "`Miley Cyrus`", "`Hernie Clanders`"]
    if not member:
        await ctx.send("You must specifiy who you want to hack, randy")
        return
    await ctx.send(f'Hacking {member.mention}')
    await asyncio.sleep(1.5)
    await ctx.send(f'Getting discord email account name....')

    await asyncio.sleep(2.5)
    await ctx.channel.purge(limit=1)
    await ctx.send(f'Discord email account name: {random.choice(fake_emails)}')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)

    await ctx.send(f'Getting discord email account password....')
    await asyncio.sleep(2.5)
    await ctx.channel.purge(limit=1)
    await ctx.send(f'Discord email account password: {random.choice(fake_passwords)}')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)

    await ctx.send(f'Getting discord user device name....')
    await asyncio.sleep(2.5)
    await ctx.channel.purge(limit=1)
    await ctx.send(f'Discord user device name: {random.choice(fake_device_names)}')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)

    await ctx.send(f'Getting user device password....')
    await asyncio.sleep(2.5)
    await ctx.channel.purge(limit=1)
    await ctx.send(f'Discord user device password: {random.choice(fake_device_passwords)}')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)

    await ctx.send(f'Getting user social security number....')
    await asyncio.sleep(2.5)
    await ctx.channel.purge(limit=1)
    await ctx.send(f'Social security number: {random.choice(fake_ssns)}')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)

    await ctx.send(f'Getting user address....')
    await asyncio.sleep(2.5)
    await ctx.channel.purge(limit=1)
    await ctx.send(f'Address: {random.choice(fake_addresses)}')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)

    await ctx.send(f'Getting name....')
    await asyncio.sleep(2.5)
    await ctx.channel.purge(limit=1)
    await ctx.send(f'Name: {random.choice(fake_names)}')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)

    await ctx.send(f'Registering user as a sex offender....')
    await asyncio.sleep(2.5)
    await ctx.channel.purge(limit=1)
    await ctx.send(f'Successfully registered user as a sex offender')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)

    await ctx.send(f'Adding user to No-Fly list')
    await asyncio.sleep(2.5)
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(f'Successfully added user to No-Fly list')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)

    await ctx.send(f'Leaking data....')
    await asyncio.sleep(2.5)
    await ctx.channel.purge(limit=1)
    await ctx.send(f'Leaked data to FBI, CIA, DEA, ATF, NSA, KGB...')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)

    await ctx.send(f'Hack complete!')

@client.command()
async def av(ctx, member : discord.Member):
    show_avatar = discord.Embed(

        color = 0xdd16d9
    )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)

@client.command(pass_context=True)
async def dm(ctx, user: discord.Member, *, message=None):
    await ctx.channel.purge(limit=1)

    embed = discord.Embed(
        description=message,
        color=0xdd16d9
    )

    channel = await user.create_dm()
    await channel.send(embed=embed)
    channel = client.get_channel(699655178818814013)
    embed = discord.Embed(
    title = 'Direct Message Log',
    description = f'Message: `{message}`\nAuthor: `{ctx.author}`\nRecipient: `{user}`',
    colour = 0xdd16d9
    )
    await channel.send(embed=embed)

@client.command()
async def say(ctx, *, message):
    embed = discord.Embed(
        description=message,
        colour=0xdd16d9

    )
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(embed=embed)
    channel_s = client.get_channel(699655178818814013)
    embed = discord.Embed(
        description='Say Cmd Log',
        colour = 0xdd16d9
    )
    embed.add_field(name=f'Message: *{message}*\nServer: *{ctx.guild}*\nChannel: *{ctx.channel}*', value=f'Sent by: {ctx.author.mention}')
    await channel_s.send(embed=embed)

@client.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f'Dont ping me, blyat!\n\n{round(client.latency * 1000)} Milliseconds')

@client.command()
async def count(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

@client.command()
async def servers(ctx):
    await ctx.send(f'Kolbaser is in {str(len(client.guilds))} servers')

@client.command(pass_context=True)
async def temperature_info(ctx):
    embed = discord.Embed(
    title = '***Kolbaser***\n*Temperature Converter*',
    description = 'Convert Fahrenheit to Celsius/Kelvin or vice versa!',
    colour = 0xdd16d9
    )
    embed.add_field(name='How to use', value='`k temperature [OG temp] [temp value] [to temp]`', inline=False)
    embed.add_field(name='Example', value='`k temperature cels 100 fahr`', inline=False)
    embed.add_field(name='Output', value='`100 degrees celsius converted to fahrenheit is 212 degrees fahr`', inline=False)
    await ctx.send(embed=embed)

def t_converter_c(temp_var): #cels -> fahr
    c_to_f = ((temp_var * 1.8) + 32)
    return '{:.2f}'.format(c_to_f)

def t_converter_c2(temp_var): #cel -> kelv
    c_to_k = (temp_var + 273.15)
    return '{:.2f}'.format(c_to_k)

def t_converter_f(temp_var): #fahr -> cels
    f_to_c = ((temp_var - 32) * .556)
    return '{:.2f}'.format(f_to_c)

def t_converter_f2(temp_var): #fahr -> kelv
    f_to_k = ((temp_var - 32) * .556 + 273.15)
    return '{:.2f}'.format(f_to_k)

def t_converter_k(temp_var): #kelv -> cels
    k_to_c = (temp_var - 273.15)
    return '{:.2f}'.format(k_to_c)

def t_converter_k2(temp_var): #kelv -> fahr
    k_to_f = ((temp_var - 273.15) * 1.8 + 32)
    return '{:.2f}'.format(k_to_f)

@client.command(pass_context=True)
async def temperature(ctx, og_temp: str, temp_var: int, to_temp=None):
    await ctx.send('Converting.....')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)
    if og_temp == 'cels' and to_temp == 'fahr':
        c2f = t_converter_c(float(temp_var))
        await ctx.send(f'{ctx.author.mention}\n{temp_var} degrees celsius converted to fahrenheit is {c2f} degrees F')

    elif og_temp == 'cels' and to_temp == 'kelv':
        c2k = t_converter_c2(float(temp_var))
        await ctx.send(f'{ctx.author.mention}\n{temp_var} degrees celsius converted to kelvin is {c2k} degrees K')

    elif og_temp == 'fahr' and to_temp == 'cels':
        f2c = t_converter_f(float(temp_var))
        await ctx.send(f'{ctx.author.mention}\n{temp_var} degrees fahrenheit converted to celsius is {f2c} degrees C')

    elif og_temp == 'fahr' and to_temp == 'kelv':
        f2k = t_converter_f2(float(temp_var))
        await ctx.send(f'{ctx.author.mention}\n{temp_var} degrees fahrenheit converted to kelvin is {f2k} degrees K')

    elif og_temp == 'kelv' and to_temp == 'cels':
        k2c = t_converter_k(float(temp_var))
        await ctx.send(f'{ctx.author.mention}\n{temp_var} degrees kelvin converted to celsius is {k2c} degrees C')

    elif og_temp == 'kelv' and to_temp == 'fahr':
        k2f = t_converter_k2(float(temp_var))
        await ctx.send(f'{ctx.author.mention}\n{temp_var} degrees kelvin converted to fahrenheit is {k2f} degrees F')

@client.command(pass_context=True)
async def alcoholcontent_info(ctx):
    embed = discord.Embed(
    title = '***Kolbaser***\nBAC Information',
    description = 'How to use BAC calculator',
    colour = 0xdd16d9
    )

    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/690305523903758612/a79176bd0251eb2df75c143f016238ee.png?size=256')
    embed.set_author(name='KOLBASER', icon_url='https://cdn.discordapp.com/avatars/690305523903758612/6c2dfebc0f2dc4345840909ee5b68338.png?size=1024')

    embed.add_field(name='How to use', value='`k alcoholcontent [gender] [ounces of alcohol] [weight in pounds]`', inline=False)
    embed.add_field(name='Example:', value='`k alcoholcontent male 6 210 `', inline=False)
    await ctx.send(embed=embed)

def bac_calc1(d_amount, w_amount):
    c1 = float(((d_amount * 3.75) / w_amount))
    return '{:.2f}'.format(c1)

def bac_calc2(d_amount, w_amount):
    c2 = float(((d_amount * 4.7) / w_amount))
    return '{:.2f}'.format(c2)

@client.command(pass_context=True)
async def alcoholcontent(ctx, sex: str, d_amount: int, w_amount: int):
    await ctx.send('Calculating.....')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)
    if sex == 'male':
        mbac = bac_calc1(d_amount, w_amount)
        embed = discord.Embed(
        title = '***Kolbaser***\nBlood Alcohol Concentration',
        colour = 0xdd16d9
        )
        embed.add_field(name='**FORMULA**', value='(ounces of alcohol) x (men: 3.75, women: 4.7) ÷ (weight in pounds)', inline=False)
        embed.add_field(name='**Blood Alcohol Concentration**', value=f"{ctx.author.mention} A male that weighs `{w_amount}` pounds and has consumed `{d_amount}` ounces of alcohol's BAC is `{mbac}`", inline=False)
        await ctx.send(embed=embed)


    elif sex == 'female':
        fbac = bac_calc2(d_amount, w_amount)
        embed = discord.Embed(
        title = '***Kolbaser***\nBlood Alcohol Concentration',
        colour = 0xdd16d9
        )
        embed.add_field(name='**FORMULA**', value='(ounces of alcohol) x (men: 3.75, women: 4.7) ÷ (weight in pounds)', inline=False)
        embed.add_field(name='**Blood Alcohol Concentration**', value=f"{ctx.author.mention} A female that weighs `{w_amount}` pounds and has consumed `{d_amount}` ounces of alcohol's BAC is `{fbac}`", inline=False)
        await ctx.send(embed=embed)

@client.command(pass_context=True)
async def math(ctx, type: str, n1: int, n2: int):
    await ctx.send("Calculating...")
    await asyncio.sleep(.555)
    await ctx.channel.purge(limit=1)

    if type == 'add':
        answer1 = (n1 + n2)
        await ctx.send(f'`{n1}` plus `{n2}` is **{answer1}**')

    elif type == 'sub':
        answer2 = (n1 - n2)
        await ctx.send(f'`{n1}` minus `{n2}` is **{answer2}**')

    elif type == 'multi':
        answer3 = (n1 * n2)
        await ctx.send(f'`{n1}` times `{n2}` is **{answer3}**')

    elif type == 'div':
        answer4 = (n1 / n2)
        await ctx.send(f'`{n1}` divided by `{n2}` is **{answer4}**')
    else:
        await ctx.send(f'Invalid parameters {ctx.author.mention} stupid cyka')

@client.command(pass_context=True)
async def spam(ctx, spam: str, num1: int):
    r_words = spam * num1
    await ctx.send(f'{r_words}')

@client.command()
async def jack(ctx):
    embed = discord.Embed(
        colour = 0xdd16d9
    )
    embed.set_author(icon_url=last_message.author.avatar_url, name=f"{last_message.author}")
    embed.set_thumbnail(url=last_message.author.avatar_url)
    embed.add_field(name="Deleted", value=f"{messages[ctx.channel.id].content}", inline=False)
    await ctx.send(embed=embed)

@jack.error
async def jack_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Nothing to jack, stupid debil")

##########################################################################################
#client events

@client.event
async def on_member_join(member):

    await member.create_dm()
    await member.send(
        f'Привет {member.name}, Thank you for joining! ')
    server = client.get_guild(681262467229155476)
    channel = client.get_channel(751329457305813012)
    role = discord.utils.get(member.guild.roles, name=ROLE)
    await member.add_roles(role)
    embed = discord.Embed(
    title = '***Member Joined***',
    description = f'{member.mention}',
    colour = 0xdd16d9
    )
    embed.add_field(name=f'Welcome to ***From Russia With Love!***', value='Do `k kolbaser` for information', inline=False)
    await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    server = client.get_guild(681262467229155476)
    channel = client.get_channel(751329457305813012)
    embed = discord.Embed(
    title = '***Member Left***',
    description = f'{member}',
    colour = 0xdd16d9
    )
    embed.add_field(name='Until the next meeting!', value='До свидания', inline=False)
    await channel.send(embed=embed)

@client.event
async def on_message(message):
    if message.content.lower() == 'hello':
        a1 = ["Привет", "Здравствуйте", "Hey fucker!", "Добро пожаловать!", "Hello there!", "What's up boomer?", "hiya!"]
        await message.channel.send(f'{random.choice(a1)} {message.author.mention}')

    if message.content.lower() == 'yo':
        a2 = ["Yo 148, 3-to-the-3-to-the-6-to-the-9. Representin' the ABQ. What up, biatch?", "Эй", "Что происходит", "What's good bro?"]
        await message.channel.send(f'{random.choice(a2)} {message.author.mention}')

    if message.content.lower() == 'lahey':
        a3 = ["I Am The Liquor", "RANDY!", "Shit Apple"]
        await message.channel.send(f'{random.choice(a3)} {message.author.mention}')

    if message.content.lower() == 'fuck':
        a4 = ["You", "Your mother", "you're a fuck"]
        await message.channel.send(f'{random.choice(a4)} {message.author.mention}')

    if message.content.lower() == 'randy':
        a5 = ["No u", "bo-bandy!", "Cyka Blyat!", "You're the randy, not me ***RANDY!***"]
        await message.channel.send(f'{random.choice(a5)} {message.author.mention}')

    if message.content.lower() == 'opa':
        a6 = ["BLJA!", "Opa Blja!", "Opa Blyat!", "Hell yeah blyat!"]
        await message.channel.send(f'{random.choice(a6)} {message.author.mention}')

    if message.content.lower() == 'russian underground':
        a7 = ["Shake your ass no drugs with ADIDAS!", "Is it time for a Metro Party?", "*This is Russian Underground!*"]
        await message.channel.send(f'{random.choice(a7)} {message.author.mention}')

    if message.content.lower() == 'minecraft':
        a9 = ["Real slavs play *OURCRAFT*", "I would CRUSH you in PvP, blyat!", "You haven't played minecraft until you've played 2B2T"]
        await message.channel.send(f'{random.choice(a9)} {message.author.mention}')

    if message.content.lower() == 'cyka':
        a10 = ["Cyka Blyat!", "Blyat Cyka Urod", "Who you callin' cyka?", "Vadim Blyat", "I *cyka* your mother!"]
        await message.channel.send(f'{random.choice(a10)} {message.author.mention}')

    if message.content.lower() == '420':
        a11 = ["228", "420 Dank Weed THC!", "*Лето, осень, папиросим. 228, 228*", "Blaze it!"]
        await message.channel.send(f'{random.choice(a11)} {message.author.mention}')

    if message.content.lower() == '69':
        a12 = ["[69] is the best number, and if you think not, you go to gulag, BLYAT!", "I did 69 with your babushka!", "Tekashi 69 is a cyka blyat"]
        await message.channel.send(f'{random.choice(a12)} {message.author.mention}')

    if message.content.lower() == 'shit':
        a13 = ["*This is captain turdwell! We are experiencing uncontrollable explosive thrust in both engines! Prepare for water landing!*", "Дерьмо Сука"]
        await message.channel.send(f'{random.choice(a13)} {message.author.mention}')

    if message.content.lower() == 'blyat':
        a14 = ["Urod", "Урод", "Blyat Cyka Urod"]
        await message.channel.send(f'{random.choice(a14)} {message.author.mention}')

    if message.content.lower() == 'kompot':
        a15 = ["Ooh, I love me some kompot!", "The Slavic Coca-Cola", "Real slavs drink kompot", "Kompot is good for the soul"]
        await message.channel.send(f'{random.choice(a15)} {message.author.mention}')

    if message.content.lower() == 'fuck off':
        a16 = ["No u cyka!", "IDI NAHUI", "Иди на хуй!", "Meanie (▰︶︹︺▰)", "Tf did you just say to me?!"]
        await message.channel.send(f'{random.choice(a16)} {message.author.mention}')

    if message.content.lower() == 'fuck you':
        a17 = ["No I think that it's actually fuck *YOU*", "Fuck you asshole", "Go to gulag cyka blyat!", "Eбать тебя"]
        await message.channel.send(f'{random.choice(a17)} {message.author.mention}')

    if message.content.lower() == 'hardbass':
        a18 = ["The Superior form of music", "is art!", "Listen to hardbass, cyka blyat!", "I LOVE HARDBASS!!", "Wicked Noise"]
        await message.channel.send(f'{random.choice(a18)} {message.author.mention}')

    if message.content.lower() == 'cheeki':
        a19 = ["BREEKI!", "А ну, чики-брики и в дамки", "AHH NUU CHEEKI BREEKI I V DAMKE!"]
        await message.channel.send(f'{random.choice(a19)} {message.author.mention}')

    if message.content.lower() == 'nwa':
        a20 = ["*Niggaz 4 Life*", "Miss you every day Eazy E", "**EFIL4ZAGGIN**", "Findum Fuckum & Flee"]
        await message.channel.send(f'{random.choice(a20)} {message.author.mention}')

    if message.content.lower() == 'kolbasa':
        a21 = ["Бочка, Басс, Колбасер", "Bochka, Bass, Kolbaser", "Sausage Maker!"]
        await message.channel.send(f'{random.choice(a21)} {message.author.mention}')

    if message.content.lower() == 'pidoras':
        a22 = ["YOU'RE THE PIDORAS!", "Трахни тебя, пидорас", "It's not nice to refer to yourself that way!", "Don't say that in Russia, or you go to gulag!"]
        await message.channel.send(f'{random.choice(a22)} {message.author.mention}')

    if message.content.lower() == 'alan':
        a23 = ["Alan gay", "Alan bad", "Alan worst", "Alan belongs in the gulag, blyat!"]
        await message.channel.send(f'{random.choice(a23)} {message.author.mention}')

    if message.content.lower() == 'dont fuck with me':
        a69 = ["*I hope you dont mind if i fuck your face up and give you two black eyes and 6 red purpleish bruises all over your face and 2 bumps on your head and bruises all over your stomach and legs and have your dick stepped on about 12 times bro*", "*I am the last person you wanna fuck with because I WILL FUCK YOU BACK, IN WAYS YOU NEVER EVEN IMAGINED!*"]
        await message.channel.send(f'{random.choice(a69)}')

    if message.content.lower() == 'shut the fuck up':
        await message.channel.send(f"*You're a fucking* ***CUNT***")

    if message.content.lower() == 'chebureki':
        a24 = ["MMMM GOOD ЧЕБУРЕКИ", "WITH A SIDE OF KOMPOT!"]
        await message.channel.send(f'{random.choice(a24)} {message.author.mention}')

    if message.content.lower() == 'gormonalno':
        a25 = ["Hormonal, intravenous", "Blood beating in the veins", "I will enter into your genes", "Life Beyond the Universe. Silenced the strings gradually"]
        await message.channel.send(f'{random.choice(a25)} {message.author.mention}')

    if message.content.lower() == 'dick':
        a26 = ["HUI!", "At least I have dick", "You like dicks in your ass", "I know what you are but what am I"]
        await message.channel.send(f'{random.choice(a26)}')

    if message.content.lower() == 'bitch':
        a27 = ["Shit, you talking to me or your girl. Oh wait you don't have a girl", "You're a bitch nigga", "I fucked your bitch"]
        await message.channel.send(f'{random.choice(a27)} {message.author.mention}')

    if message.content.lower() == 'cheeki breeki':
        await message.channel.send('https://www.youtube.com/watch?v=BnTW6fZz-1E \nAHHHH NUUUU CHEEKI BREEKI I V DAMKE!!!')

    if message.content.lower() == 'vodka':
        a28 = ["AKA Russian Water", "VODA!", "MMM DAS GOOD WATER, COMRADE!"]
        await message.channel.send(f'{random.choice(a28)} {message.author.mention}')

    if message.content.lower() == 'nash gimn':
        a29 = ["Raz Raz Raz, eto hardbass!", "Раз, раз, раз, это хардбасс", "Everything is in the Adidas sports"]
        await message.channel.send(f'{random.choice(a29)}')

    if message.content.lower() == 'pump':
        a30 = ["LIFE IS PUMP!", "PUMPING STORM!", "PUMPING PARTY!", "PUMPING FRENZY!", "Eto Pump!"]
        await message.channel.send(f'{random.choice(a30)}')

    if message.content.lower() == 'gay':
        a31 = ["No u", "PIDORAS!"]
        await message.channel.send(f'{random.choice(a31)}')

    if message.content.lower() == 'HF the virgin':
        await message.channel.purge(limit=1)

    if message.content.lower() == 'HF':
        await message.channel.purge(limit=1)

    if message.content.lower() == 'andy the virgin':
        await message.channel.purge(limit=1)

    if message.content.lower() == 'virgin':
        await message.channel.purge(limit=1)

    if message.content.lower() == 'andy':
        await message.channel.purge(limit=1)

    if message.content.lower() == 'kvass':
        a32 = ["MMMMM GOOD!", "AHHHH GOOD KVASS!", "THE RUSSIAN COCA-COLA!"]
        await message.channel.send(f'{random.choice(a32)} {message.author.mention}')

    if message.content.lower() == 'rush':
        a33 = ["RUSH B CYKA BLYAT!", "B", "C, BLYAT!"]
        await message.channel.send(f'{random.choice(a33)} {message.author.mention}')

    if message.content.lower() == 'lada':
        a34 = ["The best car ever", "GOPNIK MOBILE!", "Cyka, don't get hit!"]
        await message.channel.send(f'{random.choice(a34)} {message.author.mention}')


    await client.process_commands(message)

PATH = r"C:\Users\HF\Desktop\F Files\Nocosteyhed\Private\F8\HYDROFLOURIC\Kolbaser[5] 2020"
#sets value in json to guild id upon the bot joining the guild
@client.event
async def on_guild_join(guild):
    #loads json file to dictionary
    with open(PATH + "\memz.json", "r") as f:
        guildInfo = json.load(f)

    guildInfo[guild.id] = guild.text_channels[0] #sets key to guilds id and value to top textchannel

    #writes dictionary to json file
    with open(PATH + "\memz.json", "w")as f:
        json.dump(guildInfo, f)

#@client.event
#async def on_member_edit_pfp(before, after):

@client.event
async def on_member_update(before, after):
    if before.nick != after.nick:
        channel = client.get_channel(723701242571784194)
        PATH = r"C:\Users\HF\Desktop\F Files\Nocosteyhed\Private\F8\HYDROFLOURIC\Kolbaser[5] 2020"
        with open(PATH + "\stuff2.json", 'r') as f:
            ac = json.load(f)
            for key in ac:
                if int(key) == after.guild.id:
                    for key in ac:

                        channel = client.get_channel(ac[key])
                        embed = discord.Embed(
                        colour = 0xdd16d9
                        )
                        embed.set_author(icon_url=after.avatar_url, name=f"{after}")
                        embed.set_thumbnail(url=after.avatar_url)
                        embed.add_field(name="Past Nickname:", value=f"`{before.display_name}`", inline=True)
                        embed.add_field(name="Current Nickname:", value=f"`{after.display_name}`", inline=True)

                        await channel.send(embed=embed)#

#@client.event
#async def on_message_edit(before, after):
#    if before.content != after.content:
#        channel = client.get_channel(699655178818814013)
#        PATH = r"C:\Users\HF\Desktop\F Files\Nocosteyhed\Private\F8\HYDROFLOURIC\Kolbaser[5] 2020"
#        with open(PATH + "\edits.json", 'r') as f:
#            ac = json.load(f)
#            for key in ac:
#                if int(key) == after.guild.id:
#                    for key in ac:
#
#                        channel = client.get_channel(ac[key])
#                        embed = discord.Embed(
#                        colour = 0xdd16d9
#                        )
#                        embed.set_author(icon_url=after.avatar_url, name=f"{after}")
#                        embed.set_thumbnail(url=after.avatar_url)
#                        embed.add_field(name="Original Message:", value=f"`{before.display_content}`", inline=True)
#                        embed.add_field(name="Edited Message:", value=f"`{after.display_content}`", inline=True)

#                        await channel.send(embed=embed)



#@client.event
#async def on_message_edit(before, after):
#    channel = client.get_channel(699655178818814013)
#    embed = discord.Embed(
#    title = 'Edited Messages Log',
#    colour = 0xdd16d9
#    )
#    embed.add_field(name="Original Message:", value=f"{before.content}", inline=False)
#    embed.add_field(name="Edited Message:", value=f"{after.content}", inline=False)
#    await channel.send(embed=embed)


@client.event
async def on_message_delete(message):
    channel = client.get_channel(699655178818814013)
    embed = discord.Embed(
    title = 'Deleted Messages Log',
    description = f'Message: `{message.content}`\nAuthor: `{message.author}`\nChannel: `{message.channel}`\nServer: `{message.guild}`',
    colour = 0xdd16d9
    )
    await channel.send(embed=embed)

################################################################################
#Admin Commands:

@client.command()
@commands.has_any_role("Overlord", "Head Of KGB", "KGB", "Moderator", "Admin")
async def specinfo(ctx):
    embed = discord.Embed(
    title = 'Help commands for mods',
    colour = 0xdd16d9
    )

    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/690305523903758612/a79176bd0251eb2df75c143f016238ee.png?size=256')
    embed.set_author(name='KOLBASER', icon_url='https://cdn.discordapp.com/avatars/690305523903758612/6c2dfebc0f2dc4345840909ee5b68338.png?size=1024')

    embed.add_field(name='Kolbaser Admin Commands', value='KGB', inline=False)
    embed.add_field(name='`k kick`', value='Kicks a user', inline=False)
    embed.add_field(name='`k tempmute`', value='Mutes a user for a specified amount of time', inline=False)
    embed.add_field(name='`k unmute`', value='Unmutes a user', inline=False)
    embed.add_field(name='`k membercount`', value='Prints the number of users in server', inline=False)
    embed.add_field(name='`k nickname`', value='Changes a users nickname[COMING SOON!]', inline=False)
    embed.add_field(name='Kolbaser Overlord Commands', value='For Overlord only', inline=False)
    embed.add_field(name='`k clear`', value='Clears a message(s)', inline=False)
    embed.add_field(name='`k log`', value='Logs shit', inline=False)
    embed.add_field(name='`k nuke`', value='Clears *many* in channel', inline=False)
    embed.add_field(name='`k permamute`', value='Mutes a user ', inline=False)
    embed.add_field(name='`k ban`', value='Bans a user', inline=False)
    embed.add_field(name='`k unban`', value='Unbans a user', inline=False)
    embed.add_field(name='`k gulag`', value='Puts a user in the gulag!', inline=False)
    embed.add_field(name='`k revoke`', value='Removes a role from mentioned user', inline=False)
    embed.add_field(name='`k idinahui`', value='Sends the bot to a magic place', inline=False)
    await ctx.send(embed=embed)

@client.command()
@commands.has_any_role("Overlord", "Head Of KGB", "Moderator", "Admin")
async def kick(ctx, member: discord.Member,* ,reason: str):
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.kick()
    await ctx.send(f"{member.mention} Fucked off")
    embed = discord.Embed(
        title = '***Kolbaser***\n*Audit Log*',
        description = f"{ctx.author.mention} kicked {member.mention}\nServer: **{ctx.guild}**\nChannel: **{ctx.channel}**\nReason: {reason}\nAt {time.strftime('%H:%M:%p')}",
        colour = 0xdd16d9
        )
    my_channel1 = client.get_channel(723701242571784194)
    await my_channel1.send(embed=embed)

@client.command()
@commands.has_any_role("Overlord", "Head Of KGB", "KGBB", "Moderator", "Admin")
async def tempmute(ctx, member: discord.Member, mute_time: int,* ,reason: str):
    if not member:
        await ctx.send("You nee to specify who you want to mute, blyat!")
        return
    mute_var = mute_time * 60
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(f"{member.mention} has been muted for {mute_var} seconds by {ctx.author.mention}")
    embed = discord.Embed(
        title = '***Kolbaser***\n*Audit Log*',
        description = f"{ctx.author.mention} TEMPORARILY muted {member.mention} for {mute_var} seconds\nServer: **{ctx.guild}**\nChannel: **{ctx.channel}**\nReason: {reason}\nAt {time.strftime('%H:%M:%p')}",
        colour = 0xdd16d9
        )
    my_channel4 = client.get_channel(723701242571784194)
    await my_channel4.send(embed=embed)

    await asyncio.sleep(mute_var)
    await member.remove_roles(role)

@tempmute.error
async def tempmute_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send('CYKA BLYAT')
        await ctx.send(f"{ctx.author.mention} tried to tempmute someone! Shame.")

@client.command()
@commands.has_any_role("Overlord", "Head Of KGB", "KGB", "Moderator", "Admin")
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            await ctx.send("{} has been unmuted" .format(member.mention,ctx.author.mention))
            embed = discord.Embed(
                title = '***Kolbaser***\n*Audit Log*',
                description = f"{ctx.author.mention} unmuted {member.mention}\nAt {time.strftime('%H:%M:%p')}",
                colour = 0xdd16d9
                )
            my_channel5 = client.get_channel(723701242571784194)
            await my_channel5.send(embed=embed)
            return

@client.command()
async def membercount(ctx):
    await ctx.send("Ok Blin")
    await asyncio.sleep(.444)
    c = 0
    for member in ctx.guild.members:
        if member.bot:
            c += 1
    a = 0
    for member in ctx.guild.members:
        if not member.bot:
            a += 1
    if a == 1:
        amount = 1
    else:
        amount = 2
    await ctx.send(f"There are {a} member{'s' * (amount > 1)}, and {c} bot{'s' * (amount > 1)} in `{ctx.guild.name}`")

#################################################################################
#Overlord Commands:

@client.command(pass_context=True)
@commands.has_any_role("Overlord", "Head Of KGB", "Moderator", "Admin")
async def clear(ctx, number: int):
    await ctx.channel.purge(limit=number)
    embed = discord.Embed(
        title = '***Kolbaser***\n*Audit Log*',
        description = f"{ctx.author.mention} cleared {number} messages\nServer: **{ctx.guild}**\nChannel: **{ctx.channel}**\nAt {time.strftime('%H:%M:%p')}",
        colour = 0xdd16d9
        )
    my_channel = client.get_channel(723701242571784194)
    await my_channel.send(embed=embed)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send('CYKA BLYAT')
        await ctx.send(f"{ctx.author.mention} Only our Overlord; HydroFlouric, can use this command you imbecile!")
        embed = discord.Embed(
            title = '***Kolbaser***\n*Audit Log*',
            description = f"{ctx.author.mention} just tried to clear messages!\nServer: **{ctx.guild}**\nChannel: **{ctx.channel}**\nAt {time.strftime('%H:%M:%p')}",
            colour = 0xdd16d9
            )
        my_channel = client.get_channel(723701242571784194)
        await my_channel.send(embed=embed)
        return

PATH = r"C:\Users\HF\Desktop\F Files\Nocosteyhed\Private\F8\HYDROFLOURIC\Kolbaser[5] 2020"
@client.command(administrator=True)
async def log(ctx):
    with open(PATH + "\stuff2.json", 'r') as f:
        ac = json.load(f)

    ac[str(ctx.guild.id)] = ctx.channel.id

    with open(PATH + "\stuff2.json", 'w') as f:
        json.dump(ac, f, indent=4)
    await ctx.send("Member edits will now be sent in this channel")

PATH = r"C:\Users\HF\Desktop\F Files\Nocosteyhed\Private\F8\HYDROFLOURIC\Kolbaser[5] 2020"
#allows server members to set channel for welcome messages to send to
@client.command()
async def wlog(ctx):
    with open(PATH + "\memz.json", "r") as f:
        guildInfo = json.load(f)

    guildInfo[ctx.message.guild.id] = ctx.message.channel.id #sets channel to send message to as the channel the command was sent to

    with open(PATH + "\memz.json", "w") as f:
        json.dump(guildInfo, f, indent=4)
    await ctx.send("Member joins/leaves will be logged to this channel")


@client.command()
async def unlog(ctx):
    with open(PATH + "\stuff2.json", 'r') as f:
        prefixes = json.load(f)


    prefixes.pop(str(ctx.guild.id))

    with open(PATH + "\stuff2.json", 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send("Logs will no longer be sent in this channel")

@client.command()
@commands.is_owner()
async def nuke(ctx):
    await ctx.channel.purge(limit=1000000)
    embed = discord.Embed(
        title = '***Kolbaser***\n*Audit Log*',
        description = f"**{ctx.channel}** in **{ctx.guild}** just got nuked!",
        colour = 0xdd16d9
        )
    my_channel1 = client.get_channel(723701242571784194)
    await my_channel1.send(embed=embed)

@client.command()
@commands.has_any_role("Overlord", "Head Of KGB")
async def permamute(ctx, member : discord.Member,* ,reason: str):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)
            await ctx.send("{} has been muted" .format(member.mention,ctx.author.mention))
            embed = discord.Embed(
                title = '***Kolbaser***\n*Audit Log*',
                description = f"{ctx.author.mention} PERMANENTLY muted {member.mention}\nServer: **{ctx.guild}**\nChannel: **{ctx.channel}**\nReason: {reason}\nAt {time.strftime('%H:%M:%p')}",
                colour = 0xdd16d9
                )
            my_channel3 = client.get_channel(723701242571784194)
            await my_channel3.send(embed=embed)
            return

            overwrite = discord.PermissionsOverwrite(send_messages=False)
            newRole = await guild.create_role(name="Muted")

            for channel in guild.text_channels:
                await channel.set_permissions(newRole,overwrite=overwrite)

            await member.add_roles(newRole)
            await ctx.send("{} has been muted" .format(member.mention,ctx.author.mention))

@client.command()
@commands.has_any_role("Overlord", "Head Of KGB", "Moderator", "Admin")
async def ban(ctx, member: discord.Member,* ,reason: str):
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.ban()
    await ctx.send(f"{member.mention} До свидания")
    embed = discord.Embed(
        title = '***Kolbaser***\n*Audit Log*',
        description = f"{ctx.author.mention} banished {member.mention} to magic place!\nServer: **{ctx.guild}**\nChannel: **{ctx.channel}**\nReason: {reason}\nAt {time.strftime('%H:%M:%p')}",
        colour = 0xdd16d9
        )
    my_channel2 = client.get_channel(723701242571784194)
    await my_channel2.send(embed=embed)

@client.command()
@commands.has_any_role("Overlord", "Head Of KGB", "Moderator", "Admin")
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return

@client.command()
@commands.has_any_role("Overlord", "Head Of KGB", "KGB Тайная Полиция")
async def gulag(ctx, member: discord.Member, r: int,* ,rez: str):
    channel = client.get_channel(681262467229155476)
    role66 = discord.utils.get(ctx.guild.roles, name="Gulag Prisoner")
    if r == 1:
        role1p = discord.utils.get(ctx.guild.roles, name="1 poloski")
        await member.add_roles(role66)
        await member.remove_roles(role1p)
        await ctx.send(f'{member.mention} has been sent to the GULAG! May Stalin have mercy on them.')
        embed = discord.Embed(
            title = '***Kolbaser***\n*Audit Log*',
            description = f"{ctx.author.mention} sent {member.mention} to the GULAG!\nServer: **{ctx.guild}**\nChannel: **{ctx.channel}**\nReason: {rez}\nAt {time.strftime('%H:%M:%p')}",
            colour = 0xdd16d9
            )
        my_channel4 = client.get_channel(723701242571784194)
        await my_channel4.send(embed=embed)
        return
    elif r == 2:
        role2p = discord.utils.get(ctx.guild.roles, name="2 poloski")
        await member.add_roles(role66)
        await member.remove_roles(role2p)
        await ctx.send(f'{member.mention} has been sent to the GULAG! May Stalin have mercy on them.')
        embed = discord.Embed(
            title = '***Kolbaser***\n*Audit Log*',
            description = f"{ctx.author.mention} sent {member.mention} to the GULAG!\nServer: **{ctx.guild}**\nChannel: **{ctx.channel}**\nReason: {rez}\nAt {time.strftime('%H:%M:%p')}",
            colour = 0xdd16d9
            )
        my_channel4 = client.get_channel(723701242571784194)
        await my_channel4.send(embed=embed)
        return
    elif r == 3:
        role3p = discord.utils.get(ctx.guild.roles, name="TRI POLOSKI")
        await member.add_roles(role66)
        await member.remove_roles(role3p)
        await ctx.send(f'{member.mention} has been sent to the GULAG! May Stalin have mercy on them.')
        embed = discord.Embed(
            title = '***Kolbaser***\n*Audit Log*',
            description = f"{ctx.author.mention} sent {member.mention} to the GULAG!\nServer: **{ctx.guild}**\nChannel: **{ctx.channel}**\nReason: {rez}\nAt {time.strftime('%H:%M:%p')}",
            colour = 0xdd16d9
            )
        my_channel4 = client.get_channel(723701242571784194)
        await my_channel4.send(embed=embed)
        return

@client.command()
@commands.has_any_role("Overlord", "Head Of KGB", "KGB Тайная Полиция")
async def free(ctx, member: discord.Member, r: int, rez=None):
    role66 = discord.utils.get(ctx.guild.roles, name="Gulag Prisoner")
    if r == 1:
        role1p = discord.utils.get(ctx.guild.roles, name="1 poloski")
        await member.add_roles(role1p)
        await member.remove_roles(role66)
        embed = discord.Embed(
            title = '***Kolbaser***\n*Audit Log*',
            description = f"{member.mention} has been freed from the GULAG!",
            colour = 0xdd16d9
            )
        my_channel4 = client.get_channel(723701242571784194)
        await my_channel4.send(embed=embed)
        return
    elif r == 2:
        role2p = discord.utils.get(ctx.guild.roles, name="2 poloski")
        await member.add_roles(role2p)
        await member.remove_roles(role66)
        embed = discord.Embed(
            title = '***Kolbaser***\n*Audit Log*',
            description = f"{member.mention} has been freed from the GULAG!",
            colour = 0xdd16d9
            )
        my_channel4 = client.get_channel(723701242571784194)
        await my_channel4.send(embed=embed)
        return
    elif r == 3:
        role3p = discord.utils.get(ctx.guild.roles, name="TRI POLOSKI")
        await member.add_roles(role3p)
        await member.remove_roles(role66)
        embed = discord.Embed(
            title = '***Kolbaser***\n*Audit Log*',
            description = f"{member.mention} has been freed from the GULAG!",
            colour = 0xdd16d9
            )
        my_channel4 = client.get_channel(723701242571784194)
        await my_channel4.send(embed=embed)
        return

@client.command()
@commands.has_any_role("Overlord", "Head Of KGB", "KGB Тайная Полиция")
async def revoke(ctx, member: discord.Member, role: str):
    if not member:
        await ctx.send("You need to specify a member and/or role, blyat!")

    elif role == 'KGB':
        roleKGB = discord.utils.get(ctx.guild.roles, name="KGB")
        await member.remove_roles(roleKGB)
        await ctx.send(f'{member.mention} has been stripped of KGB role')
        embed = discord.Embed(
            title = '***Kolbaser***\n*Audit Log*',
            description = f"{member.mention} has been stripped of KGB role!",
            colour = 0xdd16d9
            )
        my_channel4 = client.get_channel(723701242571784194)
        await my_channel4.send(embed=embed)
        return
    elif role == '1p':
        role2po = discord.utils.get(ctx.guild.roles, name="1 poloski")
        await member.remove_roles(role2po)
        await ctx.send(f'{member.mention} has been stripped of 1 poloski role')
        embed = discord.Embed(
            title = '***Kolbaser***\n*Audit Log*',
            description = f"{member.mention} has been stripped of 1 poloski role!",
            colour = 0xdd16d9
            )
        my_channel4 = client.get_channel(723701242571784194)
        await my_channel4.send(embed=embed)

    elif role == '2p':
        role2po = discord.utils.get(ctx.guild.roles, name="2 poloski")
        await member.remove_roles(role2po)
        await ctx.send(f'{member.mention} has been stripped of 2 poloski role')
        embed = discord.Embed(
            title = '***Kolbaser***\n*Audit Log*',
            description = f"{member.mention} has been stripped of 2 poloski role!",
            colour = 0xdd16d9
            )
        my_channel4 = client.get_channel(723701242571784194)
        await my_channel4.send(embed=embed)

    elif role == '3p':
        role3po = discord.utils.get(ctx.guild.roles, name="TRI POLOSKI")
        await member.remove_roles(role3po)
        await ctx.send(f'{member.mention} has been stripped of TRI POLOSKI role')
        embed = discord.Embed(
            title = '***Kolbaser***\n*Audit Log*',
            description = f"{member.mention} has been stripped of TRI POLOSKI role!",
            colour = 0xdd16d9
            )
        my_channel4 = client.get_channel(723701242571784194)
        await my_channel4.send(embed=embed)

@client.command()
@commands.is_owner()
async def idinahui(ctx):
    await ctx.send("Bye Blyat")
    await client.close()

@idinahui.error
async def idinahui_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send('CYKA BLYAT')
        await ctx.send(f"{ctx.author.mention} tried to send me to magic place!")
        embed = discord.Embed(
            title = '***Kolbaser***\n*Audit Log*',
            description = f"{ctx.author.mention} just tried to send me to magic place!\nServer: **{ctx.guild}**\nChannel: **{ctx.channel}**\nAt {time.strftime('%H:%M:%p')}",
            colour = 0xdd16d9
            )
        my_channel = client.get_channel(723701242571784194)
        await my_channel.send(embed=embed)
        return
