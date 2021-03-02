import discord
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def play(self, ctx, channel="Rk"):
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
        connectVoice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        await voiceChannel.connect()

def setup(client):
    client.add_cog(Music(client))