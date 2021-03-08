import discord
import asyncio
from discord.ext import commands


class Spam(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.count = 0
		self.spammer = []

	@commands.Cog.listener()
	async def on_message(self, msg):
		self.count += 1
		print(self.count)

		if self.count > 4:
			await msg.guild.ban(msg.author, reason="spamming")
			await msg.channel.send(f"{msg.author} has been banned for spamming")

		await asyncio.sleep(3)
		self.count = 0

	@commands.Cog.listener()
	async def on_error_command(self, error):
		if isinstance(error, command.MissingPermissions):
			print("perm err")

def setup(client):
	client.add_cog(Spam(client))