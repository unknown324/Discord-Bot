import discord
from discord.ext import commands
import youtube_dl
import os

music_bot = commands.Bot(command_prefix=".")

class Music:
    def __init__(self, client):
        self.client = client
        # self.token = "ODE3NDcwMTIyODM0MjY0MDk1.YEJ-YQ.BJWRH74TeV1qgvulPHRtuPZtn0A"
        # music_bot.run(self.token)

    @commands.command()
    async def play(self, ctx, url=""):

        song = os.path.isfile("song.mp3")
        try:
            if song:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait...")

        channel = discord.utils.get(ctx.guild.voice_channels, name="Rk")
        await channel.connect()
        voice = discord.utils.get(music_bot.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            file = ydl.extract_info(url, download=True)
            path = str(file['title']) + "-" + str(file['id'] + ".mp3")

        voice.play(discord.FFmpegPCMAudio(path))
        voice.source = discord.PCMVolumeTransformer(voice.source, 1)


def setup(client):
    client.add_cog(Music(client))