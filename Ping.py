from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pong(self, ctx):
        await ctx.send("{}, Die nigger!".format(ctx.author.name))

def setup(client):
    client.add_cog(Ping(client))
