import discord
from discord.ext import commands
import random
import os

client = commands.Bot(command_prefix='.')


@client.command()
async def ping(ctx):
    await ctx.send(f"Latency : {round(client.latency*1000)}ms")

@client.command(aliases=['ques'])
async def Ques(ctx, *, question):
    responses = ['hello',
                 'yes you are right',
                 'definitely no!',
                 'retard get your ass outta here',
                 'go to hell']

    await ctx.send(f"Question : {question}\n Answer : {random.choice(responses)}")

@client.command()
async def kick(ctx, *, member : discord.Member, reason="promoting pornography"):
    """
    i passed in memeber as a discord member so that we get a mentioned user instead of a string
    i could also have passed it simply as member but that thing would give me a string of userid instead of actual user
    """
    await member.kick(reason=reason)
    await ctx.send(f"{member} got kicked because of {reason}")

@client.command()
async def ban(ctx, *, member : discord.Member, reason="promoting pornography"):
    await member.ban(reason=reason)

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans() # generates a list of all banned members
    mem_name, mem_discriminator = member.split('#')

    for ban_entries in banned_users:
        user = ban_entries.user

        if (user.name, user.discriminator) == (mem_name, mem_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} has been unbanned because he bribed the owner ::)")
            return

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for files in os.listdir("./cogs"):
    if files.endswith(".py"):
        client.load_extension(f"cogs.{files[:-3]}")

client.run('ODE1OTgxNTc0OTY4ODM2MTA3.YD0UDw.9X5vCsfw48-TqCPeHJGHx78GEx8')