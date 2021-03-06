import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Bot is ready")


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, *, member : discord.Member):
    """
    i passed in memeber as a discord member so that we get a mentioned user instead of a string
    i could also have passed it simply as member but that thing would give me a string of userid instead of actual user
    """
    await member.kick()
    await ctx.send(f"{member} has been kicked from the server")


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, *, member : discord.Member):
    await member.ban()


@client.command()
@commands.has_permissions(administrator=True)
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
@commands.has_permissions(manage_roles=True)
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"{user.mention} has been given the role of: {role.name}")


@client.command()
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, user:discord.Member, role:discord.Role):
    await user.remove_roles(role)
    await ctx.send(f"{user.mention} has been removed from {role} role")


@client.command()
async def load(extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(extension):
    client.unload_extension(f"cogs.{extension}")

for files in os.listdir("./cogs"):
    if files.endswith(".py"):
        client.load_extension(f"cogs.{files[:-3]}")

# ERROR HANDLING
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Sorry, only admins have access to that command")


client.run('ODE1OTgxNTc0OTY4ODM2MTA3.YD0UDw.FzgCJqTL-NMQMAKB0MU1kMQTFnY')
