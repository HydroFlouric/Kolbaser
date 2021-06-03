import discord
from discord.ext import commands, tasks
from pathlib import Path
from typing import Union
import asyncio
from datetime import datetime
import json
import random
HF = 273255595509809162
Kolbaser = 690305523903758612


class SHIT(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command(aliases=['fuck'])
    async def shit(self, ctx, m: discord.Member = None):
        if not m:
            await ctx.send("Who do you want me to shit?")
            return
        elif m == HF or Kolbaser:
            return
        else:
            shits = ["eats pochki",
                     "puts on a furry bunny suit at night",
                     "watches gay bird porn",
                     "has dementia",
                     "is gay",
                     "GreenSnakeDude sucks at Base Wars",
                     "plays Adopt Me! on roblox",
                     "builds dirt houses in minecraft",
                     "is stupid",
                     "has 2 babushkas!",
                     "huffs paint",
                     "huffs fresh manure",
                     "swallows toothpaste after brushing, yuck!",
                     "can't do simple mental math",
                     "is a n00b"]
            await ctx.send(f"{m.mention} {random.choice(shits)}")
            return



def setup(client):
    client.add_cog(SHIT(client))
