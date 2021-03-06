import discord
from discord.ext import commands
import youtube_dl
import os

music_bot = commands.Bot(command_prefix=".")

@music_bot.command()
async def play(ctx, url=""):
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

@music_bot.command()
async def stop(ctx):
    voice = discord.utils.get(music_bot.voice_clients, guild=ctx.guild)
    if voice.is_palying():
        await voice.stop()

@music_bot.command()
async def resume(ctx):
    voice = discord.utils.get(music_bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        await voice.resume()

@music_bot.command()
async def pause(ctx):
    voice = discord.utils.get(music_bot.voice_clients, guild=ctx.guild)
    if voice.is_palying():
        await voice.pause()
with open("D:\\Programming stuff\\Pycharm projects\\Other stuff\DISCORD\\musictoken.txt") as f:
    t = f.readline()
music_bot.run(t)