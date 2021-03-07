import discord
from discord.ext import commands


offensive_words = ["lmao", "rofl"]

class Security(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.counter = 0
		self.kick_check = False

	@commands.Cog.listener()
	async def on_message(self, msg):
		for words in offensive_words:
			if words in msg.content:
				await msg.delete()
				self.counter += 1
				print(f"{msg.author} + {self.counter}")
				print(self.counter)
				await msg.channel.send(f"Warning!.{msg.author.mention} don't use offensive words or you will be kicked from the server!")

				if self.counter > 2:
					self.kick_check = True
					await self.kick(member=msg.author)
					await msg.channel.send(f"{msg.author} has been kicked from the server for using offensive words.")

		await self.client.process_commands(msg)
		#  explain this please



	async def kick(self, member:discord.Member, reason=None):
		if self.kick_check:
			await member.kick()

def setup(client):
	client.add_cog(Security(client))