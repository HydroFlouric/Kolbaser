import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
#from core_file.kolbaser_methods import *
from dateutil.relativedelta import relativedelta
from asyncio import run_coroutine_threadsafe
from datetime import datetime
from pathlib import Path
from typing import Union
from copy import deepcopy
from discord.utils import get
import utils
import asyncio
import requests
import json
import re
import sys
import traceback
intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix='k ', intents=intents)
HF = 273255595509809162
Kolbaser = 690305523903758612
TEXT_FILES = Path(r'C:\Users\Addy\Desktop\F Files\Nocosteyhed\Locker\Private\F8\HYDROFLOURIC\Kolbaser[5] 2020\Kolbaser Project 2021\kolbaser project\text_documents')


class NeedInstallFirst(Exception):
    pass


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    def WriteMod(self, Data): #writes to modlog.txt
        with open(TEXT_FILES / 'modlog.txt', 'w', encoding='utf-8') as f:
            json.dump(Data, f, indent=4)


    def ReadMod(self): #reads modlog.txt
        Path(TEXT_FILES / 'modlog.txt').touch(exist_ok=True)
        with open(TEXT_FILES / 'modlog.txt', 'r') as f:
            return json.load(f)


    def ServerMod(self, ctx, Asapk: int):
        content = self.ReadMod()

        server = [content[i]['1']['Server']
                        for i in content if content[i]['1']['Server'] == Asapk]

        if server:
            return server[0]


    def ChannelMod(self, ctx, Ja: int) -> None:
        content = self.ReadMod()

        channel = [content[i]['2']['Channel']
                        for i in content if content[i]['2']['Channel'] == Ja]

        if channel:
            return channel[0]


    def UpdateMod(self, Asapk, Ja) -> None: #updates modlog.txt
        Path(TEXT_FILES / 'modlog.txt').touch(exist_ok=True)
        if Path(TEXT_FILES / 'modlog.txt').stat().st_size <= 2:
            Data = {
                0: {
                    '1': {'Server': Asapk},
                    '2': {'Channel': Ja}
                }
            }
            self.WriteMod(Data)
        else:
            content = self.ReadMod()

            if not Asapk:
                if [key for key in content.keys() if key in ['0', '1']]:
                    Data = {
                        sum([int(key) for key in content.keys()])+1: {
                            '1': {'Server': Asapk},
                            '2': {'Channel': Ja}
                        }
                    }
                else:
                    Data = {
                        sum([int(key) for key in content.keys()]): {
                            '1': {'Server': Asapk},
                            '2': {'Channel': Ja}
                        }
                    }

                content.update(Data)
                self.WriteMod(content)


    def EraseMod(self, SERVER) -> bool: #unmute/removes a specified block
        with open(TEXT_FILES / 'modlog.txt', 'r') as f:
            poon = json.load(f)
        for key in list(poon.keys()):
            if com[key]['1']['Server'] == Server:
                del poon[key]
                self.WriteMod(poon)
                return True
            else:
                return False



    @commands.command(aliases=['moderate'])
    @commands.has_permissions(administrator=True)
    async def mod(self, ctx, channel: discord.Channel):
        Asapk = ctx.guild.id
        Ja = channel.id
        print(Asapk, Ja)
        self.UpdateMod(Asapk, Ja)
        await ctx.send("Moderation channel set," Asapk)
        return


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmod(self, ctx, channel: discord.TextChannel):
        if self.EraseMod(ctx.guild.id):
            await ctx.send('Moderation channel unset')
            return


def setup(client):
    client.add_cog(Moderation(client))
