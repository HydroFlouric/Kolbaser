import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from pathlib import Path
from typing import Union
import asyncio
from datetime import datetime
import json

TEXT_FILES = Path(r'C:\Users\Addy\Desktop\F Files\Nocosteyhed\Locker\Private\F8\HYDROFLOURIC\Kolbaser[5] 2020\Kolbaser Project 2021\kolbaser project\text_documents')



class InfoCommand(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command(aliases=["info"])
    async def kolbaser(self, ctx):
        embed=discord.Embed(
            description='*Kolbaser Information*\nI am a multi-purpose discord bot. I am able to do moderation, utility, memes, complex math, and other fun!',
            colour=0xdd16d9
        )
        embed.set_author(name='I AM KOLBASER', icon_url='https://cdn.discordapp.com/avatars/690305523903758612/6c2dfebc0f2dc4345840909ee5b68338.png?size=1024')
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/690305523903758612/6c2dfebc0f2dc4345840909ee5b68338.png?size=1024')
        embed.set_image(url='https://cdn.discordapp.com/attachments/693639674841006101/700129506773565520/kolbaser.png')
        embed.set_footer(text='Made by: HydroFlouric#7119\nSpecial Contributors: alekos#5235, The_Storm135#8326')
        embed.add_field(name='To view public commands:', value='`k cmd` or `k cmds`', inline=False)
        #embed.add_field(name='To view admin commands:', value='`k administrator` or `k admin`', inline=False)
        #embed.add_field(name='Number of servers: ', value=f'{CServersBlyat()}')
        embed.add_field(name='Enlightening video',value='https://www.youtube.com/watch?v=VLW1ieY4Izw', inline=False)
        #embed.add_field(name='Kolbaser Donation Information',value='`k donate[UNAVAILABLE]`', inline=False)
        #embed.add_field(name='Kolbaser support server link:',value='Do` k invite`', inline=False)
        #embed.add_field(name='Kolbaser invite link:',value='`https://discord.com/api/oauth2/authorize?client_id=690305523903758612&permissions=8&scope=bot`', inline=False)
        await ctx.send(embed=embed)



    @commands.command(aliases=['cmd'])
    async def cmds(self, ctx):
        embed=discord.Embed(
            description='*Kolbaser Commands*',
            colour=0xdd16d9
        )
        embed.set_author(name='KOLBASER Public Commands', icon_url='https://cdn.discordapp.com/avatars/690305523903758612/6c2dfebc0f2dc4345840909ee5b68338.png?size=1024')
        embed.set_footer(text='Made by: HydroFlouric#7119\nSpecial Contributors: alekos#5235, The_Storm135#8326')
        embed.add_field(name='`k serverinfo` aliases=`k server`', value='Displays server information', inline=False)
        embed.add_field(name='`k userinfo` aliases=`k user`', value='Displays member information\nExample: `k userinfo @mention`', inline=False)
        embed.add_field(name='`k stats` aliases=`k statistics`', value='Displays internal information', inline=False)
        embed.add_field(name='`k invite`', value='Invite information', inline=False)
        embed.add_field(name='`k translate` aliases=`k trans`', value='Google Translator, may not work all the time\nExample: `k translate [message] tolang [lang abbreviation]`\n(do `k trans langs` for the list)', inline=False)
        embed.add_field(name='`k define` aliases=`k def`', value='Urban Dictionary command\nExample:`k define [word]`', inline=False)
        embed.add_field(name='`k code`', value='Code Compiler!\nExample: `k code [code]` Type `k code` and then 3 tildes and then py and then space and then type your code and then 3 more tildes', inline=False)
        embed.add_field(name='`k temperature_info` aliases=`k temp_info`', value='Temperature Converter, convert between 8 different temperatures', inline=False)
        embed.add_field(name='`k alcoholcontent_info` aliases=`k bac_info`', value='Calculate B.A.C., blood alcohol concentration!', inline=False)
        embed.add_field(name='`k math`', value='Simple math command! (Addition: add, Subtraction: sub, Multiplication: multi, Division: div, Exponents: power. Do math equations with 2 inputs\nExample: `k math add 1 1`', inline=False)
        embed.add_field(name='`k quadratic` aliases=`k quad`', value='Do quadratic equations with 3 inputs\nExample: `k quadratic 69 69 69`', inline=False)
        embed.add_field(name='`k interest` aliases=`k simpint, k intcalc`', value='Calculate Interest! Modes: Daily, Weekly, Monthly, Yearly, Continuously, or Normal\nExample: `k interest [principal] [rate] [time in years] [mode]`', inline=False)
        embed.add_field(name='`k spam`', value='Spam command!\nExample: `k spam [message] [amount]`', inline=False)
        embed.add_field(name='`k kolbasa`', value='Prints a picture of Russian suasage!', inline=False)
        embed.add_field(name='`k meme`', value='Meme command! Oooo blyat, good memes!', inline=False)
        #embed.add_field(name='`k flbp`', value='FUTURE LOWER BACK PROBLEMS(nsfw)', inline=False)
        embed.add_field(name='`k vid`', value='Prints a random funny video! (Could possibly offend)', inline=False)
        embed.add_field(name='`k roulette`', value='Play Russian Roulette with Kolbaser!', inline=False)
        embed.add_field(name='`k ask`', value='Ask Kolbaser yes or no questions\nExample: `k ask is ur mom gay`', inline=False)
        embed.add_field(name='`k hack`', value='Hack someone\nExample: `k hack @mention`', inline=False)
        embed.add_field(name='`k kill`', value='Kill someone\nExample: `k kill @mention`', inline=False)
        embed.add_field(name='`k avatar` aliases=`k av`', value='Enlarge a users avatar\nExample: `k avatar @mention`', inline=False)
        embed.add_field(name='`k say`', value='Make the bot say something, anything you want!\nExample: `k say fuck`', inline=False)
        embed.add_field(name='`k ping`', value='Ping the bot and returns the latency', inline=False)
        embed.add_field(name='`k count`', value='Argument counter\nExample: `k count my name is jeff`', inline=False)
        embed.add_field(name='`k servers`', value='Returns how many servers Kolbaser is in', inline=False)
        embed.add_field(name='`k users` aliases=`k c_users`', value='Returns number of members in **all** servers', inline=False)
        embed.add_field(name='`k suggest`', value='If you have a suggestion: `k suggest [suggestion]` dont abuse pls', inline=False)
        embed.add_field(name='`k membercount`', value='Returns how many members are in a server', inline=False)
        embed.add_field(name='`k rps`', value='Rock Paper Scissors command! Do `k rps [rock or paper or scissors] to play!`', inline=False)
        #embed.add_field(name='``', value='``', inline=False)
        #embed.add_field(name='``', value='``', inline=False)
        #embed.add_field(name='``', value='``', inline=False)


        await ctx.send(embed=embed)



    @commands.command(aliases=['admin', 'administrator'])
    @commands.has_permissions(administrator=True)
    async def specinfo(self, ctx):
        embed=discord.Embed(
            description='*Kolbaser Commands*',
            colour=0xdd16d9
        )
        embed.add_field(name='`k clear [2+]`', value='Clears a specified amount of messages', inline=False)
        embed.add_field(name='`k warn [member mention]`', value='Warn a user', inline=False)
        embed.add_field(name='`k nuke`', value='Deletes ALL messages in a channel, may take a while to complete', inline=False)
        embed.add_field(name='`k mute [member mention] [time]`', value='Mute a user for a specified amount of time', inline=False)
        embed.add_field(name='`k unmute [member mention]`', value='Unmutes a user', inline=False)
        embed.add_field(name='`k kick [member mention]`', value='N/A', inline=False)
        embed.add_field(name='`k ban`', value='Bans a user', inline=False)
        embed.add_field(name='`k unban`', value='N/A', inline=False)
        embed.add_field(name='`k gulag [member mention]`', value='Send a user to GULAG!', inline=False)
        embed.add_field(name='`k free [member mention]`', value='Free a user from GULAG!', inline=False)
        embed.add_field(name='`k moderate`', value='Sets channel (where cmd was invoked) where moderation updates will be sent', inline=False)
        embed.add_field(name='`k install_spy`', value='Lets you see deleted/edited messages', inline=False)
        embed.add_field(name='`k uninstall_spy`', value='Self-explanatory', inline=False)
        embed.add_field(name='`k install_welcome`', value='Sets welcome channel', inline=False)
        embed.add_field(name='`k uninstall_welcome`', value='Unsets welcome channel', inline=False)
        embed.add_field(name='`k install_goodbye`', value='Sets goodbye channel', inline=False)
        embed.add_field(name='`k uninstall_goodbye`', value='Unsets goodbye channel', inline=False)
        embed.add_field(name='`k install_updates`', value='Lets you see member updates (nickname change, role change, etc)', inline=False)
        embed.add_field(name='`k uninstall_updates`', value='Self-explanatory', inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(InfoCommand(client))
